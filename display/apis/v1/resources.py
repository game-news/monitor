import math
import os
from flask import jsonify
from display.extensions import Resource, mongo, MethodResource, reqparse
import redis

parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('per_page', type=int)


class Entity(MethodResource):
    """
    各种实体的接口
    应该将这些实体特地的有规则地命名
    """

    def get(self):
        args = parser.parse_args()
        if args.page:
            page = args.page
        else:
            page = 1

        if args.per_page:
            per_page = args.per_page
        else:
            per_page = 16

        results = []
        coll = mongo.db.get_collection('entity')
        count = coll.find({}).count()

        for i in list(coll.find({}).skip((page - 1) * per_page).limit(per_page)):
            i['_id'] = str(i['_id'])
            results.append(dict(i))

        if page > 1:
            previous = "http://plrom.niracler.com:5555/api/entity?page={}".format(page-1)
        else:
            previous = None

        if page < math.ceil(count/per_page):
            next = "http://plrom.niracler.com:5555/api/entity?page={}".format(page+1)
        else:
            next = None

        return jsonify({
            'next': next,
            'previous': previous,
            'results': results,
            'count': count,
        })


class HelloWorld(MethodResource):
    def get(self):
        return {'hello': 'world'}


class MongoMonitor(MethodResource):
    def get(self):
        """
        :return:
        """
        names = mongo.db.collection_names()
        results = []

        for name in names:
            item = {}

            item['name'] = name
            item['count'] = mongo.db.command("collstats", name)['count']

            results.append(item)

        return jsonify({
            'results': results,
            'count': len(results),
        })


class RedisMonitor(MethodResource):
    def get(self):
        client = redis.Redis(host='plrom.niracler.com', port='6379', password='123456')
        keys = client.keys()
        results = []

        for key in keys:
            item = {
                'key': key.decode('utf-8'),
                'type': client.type(key).decode('utf-8')
            }

            if item['type'] == 'set':
                item['length'] = client.scard(key)
            elif item['type'] == 'list':
                item['length'] = client.llen(key)
            elif item['type'] == 'zset':
                item['length'] = client.zcard(key)
            elif item['type'] == 'set':
                item['length'] = client.scard(key)
            else:
                item['length'] = 1

            results.append(item)

        return jsonify({
            'results': results,
            'count': len(results),
        })

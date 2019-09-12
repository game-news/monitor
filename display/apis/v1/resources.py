import os
from flask import jsonify
from display.extensions import Resource, mongo, MethodResource
import redis


class Entity(MethodResource):
    """
    各种实体的接口
    应该将这些实体特地的有规则地命名
    """

    def get(self):
        names = [
            'games_3dm_ol',
            'games_3dm_console',
            'games_3dm_shouyou',
            'gamesky',
        ]
        results = []

        for name in names:
            coll = mongo.db.get_collection(name)

            for i in list(coll.find({})):
                i['_id'] = str(i['_id'])
                results.append(dict(i))

        return jsonify({
            'results': results,
            'count': len(results),
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
            mongo.db.get_collection(name)

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

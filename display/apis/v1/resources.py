import os
from flask import jsonify
from display.extensions import Resource, mongo, MethodResource
import redis


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
            if item['type'] == 'list':
                item['length'] = client.llen(key)
            if item['type'] == 'zset':
                item['length'] = client.zcard(key)
            if item['type'] == 'set':
                item['length'] = client.scard(key)

            results.append(item)

        return jsonify({
            'results': results,
            'count': len(results),
        })

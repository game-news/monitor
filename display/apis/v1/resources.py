from display.extensions import Resource, mongo
import redis


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class MongoMonitor(Resource):
    def get(self):
        collections = mongo.db.collection_names()
        collection = mongo.db.get_collection(collections[0])
        keys = mongo.db.command("collstats", 'gnn_game')

        return dict(keys)


class RedisMonitor(Resource):
    def get(self):
        return {'redis': 'redis'}

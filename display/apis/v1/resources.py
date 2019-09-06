from display.extensions import Resource
from flask import Blueprint

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

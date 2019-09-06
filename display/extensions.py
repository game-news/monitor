from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_mongoengine import MongoEngine  # 引入monogodb引擎
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_cors import CORS

bootstrap = Bootstrap()
db = MongoEngine()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
toolbar = DebugToolbarExtension()
mongo = PyMongo()
api = Api()
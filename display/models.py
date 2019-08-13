from datetime import datetime
from display.extensions import db


class Article(db.Document):
    meta = {
        'collection': 'gnn_articles',
    }

    website = db.StringField()  # 所爬取的网站的名称
    url = db.StringField()  # 文章链接
    title = db.StringField()  # 文章标题
    content = db.StringField()  # 文章内容
    category = db.StringField()  # 文章类型
    publish_time = db.StringField()  # 发布时间

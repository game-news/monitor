from flask import Blueprint, render_template
from display.models import Article

article_bp = Blueprint('article', __name__)

@article_bp.route('/')
def index():
    page = 0
    per_page = 10
    articles = Article.objects.order_by('-create_at').skip(page * per_page).limit(per_page)
    return render_template('article/index.html', articles=articles)

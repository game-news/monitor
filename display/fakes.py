from faker import Faker
from display.models import Article

fake = Faker()


def fake_article(count=50):
    for i in range(count):
        article = Article(
            title=fake.sentence(),
            body=fake.text(2000),
            timestamp=fake.date_time_this_year()
        )
        article.save()

import click


def register_commands(app):
    @app.cli.command()
    @click.option('--article', default=10, help='Quantity of article, default is 10')
    def forge(article):
        """用于生成假数据的命令"""
        from display.fakes import fake_article

        click.echo('Generating the article...')
        fake_article(article)

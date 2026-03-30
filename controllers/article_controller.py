from controllers.controller import Controller
from models.article import Article


class ArticlesController(Controller):
    def index (self, request, response):
      articles = Article.findAll(Article)
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework - articles',
        'h1' : 'articles on site'
      })
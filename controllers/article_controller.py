from controllers.controller import Controller
from models.article import Article


class ArticlesController(Controller):
    def index (self, request, response):
      articles = Article.find_all()
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework - articles',
        'h1' : 'articles on site',
        'articles' : articles
      })

    def view(self, request, response, id):
       article = Article.get_by_id(id)
       response.text = self.view.render_html('articles/view.html', 
      {
        'title': f'MVC Framework - {article.name}',
        'h1' : f'article: {article.name}',
        'article' : article
      })
       print(article.name, article.text)
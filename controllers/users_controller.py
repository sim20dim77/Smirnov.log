from controllers.controller import Controller
# from models.article import Article
from models.user import User
from exceptions import NotFoundException

class UsersController(Controller):
    def sign_up (self, request, response):

      if request.method == 'POST':
         print(request.POST)
         return
       
      response.text = self.view.render_html('users/sign_up.html', 
      {
        'title': 'MVC Framework - регистрация'
      })

   
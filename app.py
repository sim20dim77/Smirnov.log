# from webob import Request, Response

# class API:
#     def __init__(self):
#           self.route = {}
#     def __call__(self, environ, start_response):
#             request = Request(environ)
#             response = self.handle_request(request)

#             return response(environ, start_response)
#     def handle_request(self, request):
#           response = Response()
#           request_url = request.environ.get("REQUEST_URI")
#           response.text = f"Привет, ты запросил страницу {request_url}"
#           return response
#     def route(self, path):
#           def wrapper(handler):
#                 self.routes[path] = handler
#                 return handler
#           return wrapper
          

# app = API()

# @app.route('/home')
# def home (request, response):
#       response.text = "Привет с главной страницы"

# @app.route('/about')
# def about (request, response):
#       response.text = "Привет со страницы about"

import os 
import re
import route

from webob import Request, Response
from whitenoise import WhiteNoise

class API:
    def __init__(self, static_dir="assets"):
        self.routes = route.routes
        self.whitenoise = WhiteNoise(self.wsgi_app,
        root=static_dir)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):

        return self.whitenoise(environ, start_response)
    
    def handle_request(self, request):
        response = Response()
        result = self.find_handler_re(request_path=request.path)
        
        if result is not None:
            handler, params = result
            controller = handler[0]()
            action = handler[1]
            action(controller, request, response, *params)
        else:
            self.default_response(response)
        # response.text = f"ПРивет, ты запростл страницу {requset_url}"
        return response

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler

    def find_handler_re(self, request_path):
        for path, handler in self.routes.items():
            match = re.search(path, request_path)
            if match is not None:
                return handler, match.groups()

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found"

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

app = API()












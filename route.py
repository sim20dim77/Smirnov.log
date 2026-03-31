from controllers.site_controller import SiteController
from controllers.test_controller import TestController
from controllers.article_controller import ArticlesController

routes = {
    r'^/article/(\d+)$': [ArticlesController, ArticlesController.view],
    r'^/article/(\d+)/edit$': [ArticlesController, ArticlesController.edit],
    r'^/articles$': [ArticlesController, ArticlesController.index],
    r'^/home$': [SiteController, SiteController.index],
    r'^/about$': [SiteController, SiteController.about],
    r'^/hello/(.*)$': [SiteController, SiteController.hello],
    r'^/test$': [TestController, TestController.test],
    r'^/action$': [TestController, TestController.action],
}
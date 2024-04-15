from ckan.lib.base import BaseController

class HelloController(BaseController):
    def dispatch_get(self, *args, **kwargs):
        return "Hello %s" % kwargs['names']

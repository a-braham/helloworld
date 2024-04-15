from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes

class HelloPlugin(SingletonPlugin):
    """Plugin to add my hello world"""
    implements(IRoutes, inherit=True)
    def bef_map(self, map):
        """Override all other mappings."""
        controller = "helloworld.helloworld.hello:HelloController"
        map.connect('hello-world','/hello:names',controller=controller,action="dispatch_get",conditions={"method": ["GET"]})
        return map

    def aft_map(self, map):
        """Add fall-back handlers."""
        return map


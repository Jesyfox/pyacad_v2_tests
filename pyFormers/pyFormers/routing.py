from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import app_tests.routing as test_routing
from app_tests.token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": TokenAuthMiddlewareStack(
        URLRouter(
            test_routing.websocket_urlpatterns
        )
    )
})

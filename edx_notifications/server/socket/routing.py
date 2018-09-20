from channels.routing import route
from edx_notifications.server.socket.consumers import NotificationCountConsumer

channel_routing = [
    route("websocket.receive", NotificationCountConsumer, path=r"^/notifications/(?P<user_id>\w+)/$")
]
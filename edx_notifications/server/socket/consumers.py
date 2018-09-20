import json
from channels.generic.websockets import WebsocketConsumer
from edx_notifications.lib.consumer import get_notifications_count_for_user


class NotificationCountConsumer(WebsocketConsumer):
    channel_session = True
    http_user = True
    http_user_and_session = True
    strict_ordering = False

    def connection_groups(self, **kwargs):
        return []

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, user_id=None, text=None, bytes=None, **kwargs):
        cnt = get_notifications_count_for_user(
            int(user_id),
            filters={'read': False, 'unread': True}
        )

        self.message.reply_channel.send({
            'text': json.dumps({"count": cnt}),
        })

    def disconnect(self, message, **kwargs):
        pass

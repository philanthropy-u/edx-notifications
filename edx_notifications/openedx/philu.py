"""
Notification types that will be used in common use cases for notifications around
Group Projects
"""

from edx_notifications.data import (
    NotificationType
)
from edx_notifications.lib.publisher import register_notification_type
from edx_notifications.signals import perform_type_registrations
from edx_notifications.renderers.basic import UnderscoreStaticFileRenderer

from django.dispatch import receiver

PHILU_NOTIFICATION_PREFIX = u'philu.nodebb'


class NodeBBNotificationMessageTypes(object):
    """
    Message type constants
    """
    NEW_TOPIC = 'new-topic'
    NEW_REPLY = 'new-reply'
    NEW_CHAT = 'new-chat'
    FOLLOW = 'follow'
    UPVOTE = 'upvote'
    NEW_POST_FLAG = 'new-post-flag'
    MY_FLAGS = 'my-flags'
    BAN = 'ban'
    MENTION = 'mention'
    MESSAGE = 'message'


@receiver(perform_type_registrations)
def register_notification_types(sender, **kwargs):  # pylint: disable=unused-argument
    """
    Register some standard NotificationTypes.
    This will be called automatically on the Notification subsystem startup (because we are
    receiving the 'perform_type_registrations' signal)
    """

    mapping = {key: value for key, value in NodeBBNotificationMessageTypes.__dict__.items() if not key.startswith('__')}
    for notification_type in mapping.values():
        register_notification_type(
            NotificationType(
                name=u"{prefix}.{type}".format(prefix=PHILU_NOTIFICATION_PREFIX,
                                               type=notification_type),
                renderer='edx_notifications.renderers.basic.JsonRenderer',
            )
        )
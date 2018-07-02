# """
# One time initialization of the Notification subsystem
# """

from edx_notifications import startup


def start_up():
    """
    Initialize the Notification subsystem
    """
    startup.initialize()

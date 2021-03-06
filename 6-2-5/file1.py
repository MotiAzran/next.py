class GreetingCard(object):
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(self._sender)
        print(self._recipient)

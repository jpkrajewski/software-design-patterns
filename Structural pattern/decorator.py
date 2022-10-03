class Notification:
    def __init__(self, message: str, to: list[str]):
        self.message = message
        self.to = to

    def send(self):
        print(f'Message {self.message} to {self.to}.\n')


class NotifierDecorator:
    _notification: Notification = None

    def __init__(self, notification: Notification):
        self._notification = notification

    def send(self):
        pass


class FacebookNotifier(NotifierDecorator):
    def send(self):
        print('Message send through fb api.')
        return self._notification.send()


class SMSNotifier(NotifierDecorator):
    def send(self):
        print('Message send through SMS.')
        return self._notification.send()


class SlackNotifier(NotifierDecorator):
    def send(self):
        print('Message send through Slack.')
        return self._notification.send()


message = Notification('Hello everyone, welcome to new team!', ['Bartek', 'Kuba', 'Maciej'])
slack_message = SlackNotifier(message)
slack_message.send()

super_urgent_message = SMSNotifier(SlackNotifier(FacebookNotifier(Notification('SERVERS ARE DOWN!', ['CEO', 'CFO']))))
super_urgent_message.send()

# Message send through Slack.
# Message Hello everyone, welcome to new team! to ['Bartek', 'Kuba', 'Maciej'].
#
# Message send through SMS.
# Message send through Slack.
# Message send through fb api.
# Message SERVERS ARE DOWN! to ['CEO', 'CFO'].

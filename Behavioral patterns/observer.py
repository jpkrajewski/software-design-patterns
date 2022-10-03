from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        ...


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        ...

    @abstractmethod
    def detach(self, observer: Observer):
        ...

    @abstractmethod
    def notify(self):
        ...


class NewProductEvent(Subject):
    def __init__(self):
        self.observers = []
        self.product_name = ''

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def set_new_product(self, product):
        self.product_name = product

    def notify(self):
        for o in self.observers:
            o.update(self.product_name)


class EmailSender(Observer):
    def update(self, product_name):
        print(f'New {product_name} marketing emails send.')


class SMSSender(Observer):
    def update(self, product_name):
        print(f'New {product_name} marketing SMS send.')


class CompanyWebsiteMessageSender(Observer):
    def update(self, product_name):
        print(f'New {product_name} marketing messages send.')


new_product_event = NewProductEvent()

email = EmailSender()
sms = SMSSender()
message = CompanyWebsiteMessageSender()

new_product_event.attach(email)
new_product_event.attach(sms)
new_product_event.attach(message)
new_product_event.set_new_product('IPhone X10')
new_product_event.notify()
new_product_event.detach(email)
new_product_event.set_new_product('Laptop Dell ProX1232')
new_product_event.notify()

# New IPhone X10 marketing emails send.
# New IPhone X10 marketing SMS send.
# New IPhone X10 marketing messages send.
# New Laptop Dell ProX1232 marketing SMS send.
# New Laptop Dell ProX1232 marketing messages send.
from abc import ABC, abstractmethod


class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def get_total(self):
        return self.amount

    def get_order_type(self):
        return "Regular Order"


class DiscountedOrder(Order):
    def __init__(self, order_id, customer_name, amount, discount_percent):
        super().__init__(order_id, customer_name, amount)
        self.discount_percent = discount_percent

    def get_total(self):
        discount = self.amount * self.discount_percent / 100
        return self.amount - discount

    def get_order_type(self):
        return "Discounted Order"


class PriorityOrder(Order):
    def __init__(self, order_id, customer_name, amount, priority_fee):
        super().__init__(order_id, customer_name, amount)
        self.priority_fee = priority_fee

    def get_total(self):
        return self.amount + self.priority_fee

    def get_order_type(self):
        return "Priority Order"


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[Credit Card] Payment of Rs.{amount} successful")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[UPI] Payment of Rs.{amount} successful")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[Wallet] Payment of Rs.{amount} successful")


class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):

    def send_notification(self, message):
        print(f"[Email] {message}")


class SMSNotification(NotificationService):

    def send_notification(self, message):
        print(f"[SMS] {message}")


class PushNotification(NotificationService):

    def send_notification(self, message):
        print(f"[Push Notification] {message}")


class Storage(ABC):

    @abstractmethod
    def save_order(self, order):
        pass


class DatabaseStorage(Storage):

    def save_order(self, order):
        print(f"Order {order.order_id} saved to Database")


class FileStorage(Storage):

    def save_order(self, order):
        print(f"Order {order.order_id} saved to File")


class OrderService:

    def __init__(self, payment_method, notification_service, storage):
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage = storage

    def place_order(self, order):

        total = order.get_total()

        print("\n========================")
        print("ORDER DETAILS")
        print("========================")
        print(f"Order ID      : {order.order_id}")
        print(f"Customer Name : {order.customer_name}")
        print(f"Order Type    : {order.get_order_type()}")
        print(f"Total Amount  : Rs.{total}")

        self.payment_method.pay(total)

        self.storage.save_order(order)

        self.notification_service.send_notification(
            f"Order {order.order_id} placed successfully!"
        )


if __name__ == "__main__":

    regular_order = Order("ORD101", "Alice", 5000)

    discounted_order = DiscountedOrder(
        "ORD102",
        "Bob",
        4000,
        10
    )

    priority_order = PriorityOrder(
        "ORD103",
        "Charlie",
        3000,
        500
    )

    payment = UPIPayment()
    notification = EmailNotification()
    storage = DatabaseStorage()

    order_service = OrderService(
        payment,
        notification,
        storage
    )

    order_service.place_order(regular_order)
    order_service.place_order(discounted_order)
    order_service.place_order(priority_order)
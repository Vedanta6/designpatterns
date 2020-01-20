class DeliveryOption:

    def get_price(self):
        pass


class InternationalDelivery(DeliveryOption):

    def get_price(self):
        return 50


class LocalDelivery(DeliveryOption):

    def get_price(self):
        return 5


class NoDelivery(DeliveryOption):

    def get_price(self):
        return 0

class BuyingOption:

    def get_price(self):
        pass


class PaperBook(BuyingOption):

    def get_price(self):
        return 20


class CD(BuyingOption):

    def get_price(self):
        return 80

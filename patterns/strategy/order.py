from patterns.strategy.buying_options import BuyingOption
from patterns.strategy.condition_options import ConditionOption
from patterns.strategy.delivery_options import DeliveryOption


class Order:
    __buying_choice = None
    __condition_choice = None
    __delivery_choice = None

    def __init__(
            self,
            buying_choice: BuyingOption,
            condition_choice: ConditionOption,
            delivery_choice: DeliveryOption,
    ):
        self.__buying_choice = buying_choice
        self.__condition_choice = condition_choice
        self.__delivery_choice = delivery_choice

    def calculate_price(self):
        return self.__buying_choice.get_price() * self.__condition_choice.get_discount() \
               + self.__delivery_choice.get_price()

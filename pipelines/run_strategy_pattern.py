from patterns.strategy.buying_options import PaperBook, CD
from patterns.strategy.condition_options import NewCondition, UsedCondition
from patterns.strategy.delivery_options import InternationalDelivery, LocalDelivery, NoDelivery
from patterns.strategy.order import Order


def main():
    print('Let\'s complete your order')

    buying_choices = {
        '1': PaperBook,
        '2': CD
    }
    condition_choices = {
        '1': NewCondition,
        '2': UsedCondition
    }
    delivery_choices = {
        '1': InternationalDelivery,
        '2': LocalDelivery,
        '3': NoDelivery
    }
    buying_idx = None
    condition_idx = None
    delivery_idx = None
    while buying_idx not in buying_choices.keys():
        buying_idx = input('Choose item: [1] Paper book, [2] CD, [0] Cancel > ')
        if int(buying_idx) == 0:
            break

        condition_idx = None
        while condition_idx not in condition_choices.keys():
            condition_idx = input('Choose item\'s condition: [1] new, [2] used, [0] Prev > ')
            if int(condition_idx) == 0:
                buying_idx = None
                break

            delivery_idx = None
            while delivery_idx not in delivery_choices.keys():
                delivery_idx = input('Choose delivery: [1] International, [2] Local, [3] Skip, [0] Prev > ')
                if int(delivery_idx) == 0:
                    condition_idx = None
                    break

    try:
        order = Order(
            buying_choice=buying_choices[buying_idx](),
            condition_choice=condition_choices[condition_idx](),
            delivery_choice=delivery_choices[delivery_idx]()
        )
        price = order.calculate_price()
        print(f'The total price is: {price}')
    except KeyError as err:
        print(f'Incorrect option chosen: {err}\n')


if __name__ == "__main__":
    main()

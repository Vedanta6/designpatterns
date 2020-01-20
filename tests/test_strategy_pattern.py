from patterns.strategy.buying_options import PaperBook, CD
from patterns.strategy.condition_options import NewCondition, UsedCondition
from patterns.strategy.delivery_options import InternationalDelivery, LocalDelivery, NoDelivery
from patterns.strategy.order import Order


def test_order_options():
    new_book_price = Order(
        buying_choice=PaperBook(),
        condition_choice=NewCondition(),
        delivery_choice=NoDelivery()
    ).calculate_price()
    assert NoDelivery().get_price() == 0
    assert InternationalDelivery().get_price() >= LocalDelivery().get_price()
    assert NewCondition().get_discount() == 1
    assert NewCondition().get_discount() >= UsedCondition().get_discount()
    assert new_book_price == (PaperBook().get_price() * NewCondition().get_discount() + NoDelivery().get_price())

    new_cd_price = Order(
        buying_choice=CD(),
        condition_choice=NewCondition(),
        delivery_choice=NoDelivery()
    ).calculate_price()
    assert new_cd_price == (CD().get_price() * NewCondition().get_discount() + NoDelivery().get_price())

    old_book_local = Order(
        buying_choice=PaperBook(),
        condition_choice=UsedCondition(),
        delivery_choice=LocalDelivery()
    ).calculate_price()
    assert old_book_local == (PaperBook().get_price() * UsedCondition().get_discount() + LocalDelivery().get_price())

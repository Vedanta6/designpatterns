class ConditionOption:

    def get_discount(self):
        pass


class NewCondition(ConditionOption):

    def get_discount(self):
        return 1.


class UsedCondition(ConditionOption):

    def get_discount(self):
        return 1. - max(0., min(1., 0.2))

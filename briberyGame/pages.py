from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction1(Page):
    pass


class Instruction21(Page):
    pass


class Instruction22(Page):
    pass


class Instruction3(Page):
    pass


class Instruction4(Page):
    pass


class CheckFirst(Page):
    form_model = "player"
    form_fields = ['check_1', 'check_2', 'check_3', 'check_4']
    pass


class CheckSecond(Page):
    form_model = "player"
    form_fields = ['check_5', 'check_6', 'check_7', 'check_8']
    pass


class CheckThird(Page):
    form_model = "player"
    form_fields = ['check_9', 'check_10', 'check_11', 'check_12']
    pass


class CheckForth(Page):
    form_model = "player"
    form_fields = ['check_13', 'check_14']

    pass


page_sequence = [
    Instruction1,
    Instruction21,
    Instruction22,
    Instruction3,
    Instruction4,
    CheckFirst,
    CheckSecond,
    CheckThird,
    CheckForth,
]

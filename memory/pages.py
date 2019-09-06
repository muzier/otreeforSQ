from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class High_Manipulation(Page):
    # form_model = 'player'
    # form_fields = ['keyword_1', 'keyword_2', 'keyword_3', 'keyword_4', 'statement']

    def is_displayed(self):
        return self.player.id_in_group == 1
    pass


class Low_Manipulation(Page):
    # form_model = 'player'
    # form_fields = ['keyword_1', 'keyword_2', 'keyword_3', 'keyword_4', 'statement']

    def is_displayed(self):
        return self.player.id_in_group == 2
    pass

class Control(Page):
    # form_model = 'player'
    # form_fields = ['keyword_1', 'keyword_2', 'keyword_3', 'keyword_4', 'statement']

    def is_displayed(self):
        return self.player.id_in_group == 3
    pass


class Check(Page):
    form_model = 'player'
    form_fields = ['check_1', 'check_2', 'check_3', 'check_4', 'check_5', 'check_6',
                   'check_7', 'check_8', 'check_9', 'check_10', 'check_11', 'check_12']
    pass


page_sequence = [
    High_Manipulation,
    Low_Manipulation,
    Control,
    Check
]

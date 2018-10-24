from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class End(Page):
    def vars_for_template(self):
        totlepoints = self.participant.payoff + 250
        return{
            'totleGain': self.participant.payoff,
            'totlePoints': totlepoints,
            'totleMoney': self.participant.payoff_plus_participation_fee()
            }

page_sequence = [
    End
]

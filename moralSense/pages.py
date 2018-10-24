from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class MoralSense(Page):
    form_model = 'player'
    form_fields = ['m_1', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7','m_8','m_9']
    random.shuffle(form_fields)
    pass


page_sequence = [
    MoralSense,
]

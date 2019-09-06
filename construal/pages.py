from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

lists = ['ind1', 'ind2', 'ind3', 'ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9', 'ind10',
         'ind11', 'ind12', 'ind13', 'ind14', 'ind15', 'ind16', 'ind17', 'ind18', 'ind19',
         'ind20', 'ind21', 'ind22', 'ind23', 'ind24', 'ind25', 'ind26', 'ind27', 'ind28'
         ]

list_01 = lists[0:14]

list_02 = lists[14:28]


class Construal_01(Page):
    form_model = 'player'
    form_fields = list_01
    random.shuffle(form_fields)
    pass


class Construal_02(Page):
    form_model = 'player'
    form_fields = list_02
    random.shuffle(form_fields)
    pass


page_sequence = [
    Construal_01,
    Construal_02
]

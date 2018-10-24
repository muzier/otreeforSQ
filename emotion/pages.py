from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

lists = [
            'E_1', 'E_2', 'E_3', 'E_4', 'E_5', 'E_6', 'E_7', 'E_8', 'E_9', 'E_10',
            'E_11', 'E_12', 'E_13', 'E_14', 'E_15', 'E_16', 'E_17', 'E_18', 'E_19', 'E_20'
        ]

list_01 = lists[0:10]

list_02 = lists[10:20]



class Emotion_01(Page):
    form_model = 'player'
    form_fields = list_01
    random.shuffle(form_fields)
    pass

class Emotion_02(Page):
    form_model = 'player'
    form_fields = list_02
    random.shuffle(form_fields)
    pass


page_sequence = [
    Emotion_01,
    Emotion_02,
]

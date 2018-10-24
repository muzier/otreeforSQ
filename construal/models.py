from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Cong Wei'

doc = """
Describe your belives
"""

construal_lists = [
    "当我给其他人一些东西时，我通常期待有所回报。",
    "当别人送我一个礼物，我会尽量送对方一个等值的礼物。",
    "我不认为人们有义务去回报他人的帮助。",
    "当别人无法回报我的帮助时，我不会感觉被剥削。",
    "我不会去记录我给他人的好处。",
    "当人们收到从别人那里得到的好处，他们应该尽快回报对方。",
    "最好保证一段关系中的双方保持“收支平衡”。",
    "我通常只会给曾经送我礼物的人送礼物。",
    "当我认识的人在一个项目上帮助我，我不觉得我需要回报他。",
]


def set_model_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


class Constants(BaseConstants):
    name_in_url = 'construal'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ind1 = set_model_field(construal_lists[0])
    ind2 = set_model_field(construal_lists[1])
    ind3 = set_model_field(construal_lists[2])
    ind4 = set_model_field(construal_lists[3])
    ind5 = set_model_field(construal_lists[4])
    ind6 = set_model_field(construal_lists[5])
    ind7 = set_model_field(construal_lists[6])
    ind8 = set_model_field(construal_lists[7])
    ind9 = set_model_field(construal_lists[8])
    pass

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Cong Wei'

doc = """
This part is designed for measuring participants' sense of moral!
There are seven items.
The items should be randomly assigned.
"""


class Constants(BaseConstants):
    name_in_url = 'moralSense'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def set_model_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


moral_items = [
    '如果亲人或朋友帮助了我，在回报时我会把亲人或朋友的需求和感受考虑在内。',
    '如果亲人或朋友帮助了我，在回报时我不关注亲人或朋友的感受。',
    '如果亲人或朋友帮助了我，我认为在回报时应该竭尽所能帮助亲人或朋友。',
    '当我需要亲人或朋友帮助时，我的需要被亲人或朋友忽视时，我会感觉受伤。',
    '我不是那种总是帮助亲人或朋友的人。',
    '如果亲人或朋友帮助了我，在回报时我会优先考虑亲人和朋友的个人需求。',
    '我不认为我是一个特别乐于帮助亲人或朋友的人。',
    '如果亲人或朋友帮助了我，我忽略亲人或朋友的需求和感受，我会觉得焦躁不安。',
    '当我需要帮助时，我会向我熟悉的人（亲人或朋友）寻求帮助。',
]


class Player(BasePlayer):
    m_1 = set_model_field(moral_items[0])
    m_2 = set_model_field(moral_items[1])
    m_3 = set_model_field(moral_items[2])
    m_4 = set_model_field(moral_items[3])
    m_5 = set_model_field(moral_items[4])
    m_6 = set_model_field(moral_items[5])
    m_7 = set_model_field(moral_items[6])
    m_8 = set_model_field(moral_items[7])
    m_9 = set_model_field(moral_items[8])
    pass

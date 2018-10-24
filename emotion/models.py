from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This Part is designed for emotion measurement!
There are totally 12 items which should be randomly present.
"""

emotion_lists = [
    "感兴趣的",
    "沮丧的",
    "激动的",
    "不安的",
    "有力的",
    "内疚的",
    "恐惧的",
    "敌对的",
    "热情的",
    "自豪的",
    "生气的",
    "警惕的",
    "惭愧的",
    "受鼓舞的",
    "紧张的",
    "坚定的",
    "关注的",
    "紧张不安的",
    "主动的",
    "害怕的",
]


def set_moral_field(label):
    return models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label=label
    )


class Constants(BaseConstants):
    name_in_url = 'emotion'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    E_1 = set_moral_field(emotion_lists[0])
    E_2 = set_moral_field(emotion_lists[1])
    E_3 = set_moral_field(emotion_lists[2])
    E_4 = set_moral_field(emotion_lists[3])
    E_5 = set_moral_field(emotion_lists[4])
    E_6 = set_moral_field(emotion_lists[5])
    E_7 = set_moral_field(emotion_lists[6])
    E_8 = set_moral_field(emotion_lists[7])
    E_9 = set_moral_field(emotion_lists[8])
    E_10 = set_moral_field(emotion_lists[9])
    E_11 = set_moral_field(emotion_lists[10])
    E_12 = set_moral_field(emotion_lists[11])
    E_13 = set_moral_field(emotion_lists[12])
    E_14 = set_moral_field(emotion_lists[13])
    E_15 = set_moral_field(emotion_lists[14])
    E_16 = set_moral_field(emotion_lists[15])
    E_17 = set_moral_field(emotion_lists[16])
    E_18 = set_moral_field(emotion_lists[17])
    E_19 = set_moral_field(emotion_lists[18])
    E_20 = set_moral_field(emotion_lists[19])
    pass

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Cong Wei'

doc = """
This part id designed for Nostalgia priming.
There are two group, the priming group & the control group.
First, Each group complete a memory task.
Then, each participant complete the manipulation check items.
"""


class Constants(BaseConstants):
    name_in_url = 'memory'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'manipulation'
        if self.id_in_group == 2:
            return 'control'
    # keyword_1 = models.StringField()
    # keyword_2 = models.StringField()
    # keyword_3 = models.StringField()
    # keyword_4 = models.StringField()
    # statement = models.LongStringField()
    check_1 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="如果我真的下定决心要做，我可以做成任何一件事情。"
    )
    check_2 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="当我真的要做成某件事情的时候，我通常能找到办法。"
    )
    check_3 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="我是否能得到我想要的东西取决于我。"
    )
    check_4 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="未来我会遇到的事情多数取决于我自己。"
    )
    check_5 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="多数我能做和不能做的事情取决于我。"
    )
    check_6 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="在应对我生活中的问题时，我经常会感到无助。"
    )
    check_7 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="我很少能改变发生在我生活中的重要事件。"
    )
    check_8 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="发生在我生活中的事情多数超出我自己的控制范围。"
    )
    check_9 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="我想做的事情会受到其他许多事情的干扰。"
    )
    check_10 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="对于发生在我身上的事情，我很少能控制。"
    )
    check_11 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="我不可能解决我面临的所有问题。"
    )
    check_12 = models.IntegerField(
        choices=range(1, 8, 1),
        widget=widgets.RadioSelect,
        label="有时候，我感觉我被生活驱赶着前行。"
    )
    pass

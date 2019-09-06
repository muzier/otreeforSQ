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
    '为了他人能在未来帮助我，我会先帮助他人。',
    '为了他人将来能对我友善，我会先对他人友善。',
    '如果我以前没有好好对待他人，我会害怕他将来如何对待我。',
    '我期望我的努力工作会得到回报。',
    '为了他人将来能帮助我，我会先赞美他。',
    '我希望他人对我礼貌，所以我会先对他人礼貌。',
    '如果我帮助游客，我期望他们之后可以对我道谢。',
    '很明显，如果我对他人不好，他人以后会报复我。',
    '如果我在饭店就餐时不提供小费，我猜想未来我在这个餐厅不会得到一个很好的服务。',
    '为了帮助那些以前帮助过我的人，我准备好付出一些个人代价。',
    '如果他人帮了我，我会回报他的帮助。',
    '如果他人在工作时帮助我，我很乐意以后去帮助他。',
    '为了回报他人之前的帮助，我愿意去做一些单调乏味的工作。',
    '当他人帮助了我，我认为有义务回报他的帮助。',
    '如果他人很有礼貌地向我询问信息，我会乐于帮助他。',
    '如果他人为了帮助我而借给我钱，那么，我认为我对他的回报应该远远超出我当初所得。',
    '如果他人建议我投注的赛马赢了，我肯定会给他我的一部分奖金。',
    '遇到此题，请选择数字5。',
    '我会想尽办法去帮助那些以前对我好的人。',
    '如果我遭受了严重损失，不管代价是什么，我都会立刻报复。',
    '我很愿意投入时间和精力去报复他人对我的不公平行为。',
    '如果他人对我好，我也会对他好；否则就以牙还牙。',
    '如果他人让我陷入困难的处境，我也会同样这么对待他。',
    '如果他人冒犯我，我也会以其人之道还治其人之身。',
    '如果他人对我不公平，我倾向于让他自食恶果，而不接受道歉。',
    '即便可以得到一些好处，我也不会帮助那些之前恶意对我的人。',
    '如果他人对我无礼，我也会以其人之道还治其人之身。',
    '我如何对待他人取决于他人如何对待我。'
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
    ind10 = set_model_field(construal_lists[9])
    ind11 = set_model_field(construal_lists[10])
    ind12 = set_model_field(construal_lists[11])
    ind13 = set_model_field(construal_lists[12])
    ind14 = set_model_field(construal_lists[13])
    ind15 = set_model_field(construal_lists[14])
    ind16 = set_model_field(construal_lists[15])
    ind17 = set_model_field(construal_lists[16])
    ind18 = set_model_field(construal_lists[17])
    ind19 = set_model_field(construal_lists[18])
    ind20 = set_model_field(construal_lists[19])
    ind21 = set_model_field(construal_lists[20])
    ind22 = set_model_field(construal_lists[21])
    ind23 = set_model_field(construal_lists[22])
    ind24 = set_model_field(construal_lists[23])
    ind25 = set_model_field(construal_lists[24])
    ind26 = set_model_field(construal_lists[25])
    ind27 = set_model_field(construal_lists[26])
    ind28 = set_model_field(construal_lists[27])
    pass

from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.05,
    'participation_fee': 12.50,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'BriberyGame',
        'display_name': "决策研究",
        'num_demo_participants': 100,
        'app_sequence': [
                         'introduction',
                         'briberyGame',
                         'memory',
                         'emotion',
                         'construal',
                         # 'moralSense',
                         'gameStart',
                         'main',
                         'demographic',
                         'end',
                         ]
    },
    # {
    #     'name': 'memory',
    #     'display_name': '回忆任务',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['introduction', 'memory', 'emotion']
    # },
    # {
    #     'name': 'emotion',
    #     'display_name': '情绪状态',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['emotion']
    # },
    # {
    #     'name': 'main',
    #     'display_name': '游戏',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['main', 'end']
    # },
    # {
    #     'name': 'moralSense',
    #     'display_name': '道德感知',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['moralSense']
    # },
    # {
    #     'name': 'demographic',
    #     'display_name': '个人信息',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['demographic', 'end']
    # },

    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'
POINTS_CUSTOM_NAME = '代币'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True

ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'Study_01',
        'display_name': '决策研究——实验室',
    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

#AUTH_LEVEL = 'DEMO'
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

# environ['DATABASE_URL'] = 'postgres://postgres@localhost/django_db'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
# ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'jelly@jenny1314'

# Consider '', None, and '0' to be empty/false
# DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})



DEMO_PAGE_INTRO_HTML ="""
                        决策研究！
                      """

# don't share this with anybody.
SECRET_KEY = 'ht=a)ncph2hh9&)h#34avg8j0(rdjujbtxloq^*7b8!5-t+*2a'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

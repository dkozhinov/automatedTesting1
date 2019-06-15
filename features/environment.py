# -*- coding: UTF-8 -*-


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_scenario(context, scenario):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_all(context):
    context.config.setup_logging()

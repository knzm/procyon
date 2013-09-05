# -*- coding: utf-8 -*-

import venusian

from procyon.base import get_base_model

from .interfaces import IUserModel
from .model import UserModelMixin


def create_user_model(registry, user_tablename='user'):
    base = get_base_model(registry)

    class UserModel(UserModelMixin, base):
        __tablename__ = user_tablename

    return UserModel


def get_user_model(registry):
    return registry.queryUtility(IUserModel)


def set_user_model(registry, user_model):
    registry.registerUtility(user_model, IUserModel)


def set_default_user_model(registry, user_tablename='user'):
    user_model = create_user_model(registry)
    set_user_model(registry, user_model)


def user_model(wrapped):
    def callback(context, name, ob):
        set_user_model(context.config.registry, ob)

    info = venusian.attach(wrapped, callback, category='procyon')

    return wrapped


def includeme(config):
    config.scan('.event')

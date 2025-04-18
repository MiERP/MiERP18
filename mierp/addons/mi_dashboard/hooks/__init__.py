# -*- coding: utf-8 -*-
# Copyright 2022 MiERP

from mierp import api, SUPERUSER_ID


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    return True


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    return True

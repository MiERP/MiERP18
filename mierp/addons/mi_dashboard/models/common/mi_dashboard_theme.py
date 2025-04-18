# -*- coding: utf-8 -*-
# Copyright 2022 MiERP
from mierp import models, fields


class miDashboardTheme(models.Model):
    _name = 'mi.dashboard.theme'
    _description = 'mi Dashboard Theme'

    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Dashboard Theme Name Already Exist.')
    ]

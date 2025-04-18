# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import models, fields


class AvataxConnectionTestResult(models.TransientModel):
    _name = "avatax.connection.test.result"
    _description = 'Test connection with avatax'

    server_response = fields.Html(string='Server Response')

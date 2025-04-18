# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class ResGroups(models.Model):
    _name = "res.groups"
    _inherit = ["res.groups", "bus.listener.mixin"]

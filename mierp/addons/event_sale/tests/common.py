# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta

from mierp import fields
from mierp.addons.event_product.tests.common import TestEventProductCommon
from mierp.addons.sales_team.tests.common import TestSalesCommon


class TestEventSaleCommon(TestEventProductCommon, TestSalesCommon):

    @classmethod
    def setUpClass(cls):
        super(TestEventSaleCommon, cls).setUpClass()

        cls.event_0 = cls.env['event.event'].create({
            'name': 'TestEvent',
            'date_begin': fields.Datetime.to_string(datetime.today() + timedelta(days=1)),
            'date_end': fields.Datetime.to_string(datetime.today() + timedelta(days=15)),
            'date_tz': 'Europe/Brussels',
        })

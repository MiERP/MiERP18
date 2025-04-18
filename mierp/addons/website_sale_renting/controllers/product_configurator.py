# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp.http import route

from mierp.addons.sale_renting.controllers.product_configurator import (
    SaleRentingProductConfiguratorController,
)
from mierp.addons.sale_renting.controllers.utils import _convert_rental_dates
from mierp.addons.website_sale.controllers.product_configurator import (
    WebsiteSaleProductConfiguratorController,
)


class WebsiteSaleRentingProductConfiguratorController(
    WebsiteSaleProductConfiguratorController, SaleRentingProductConfiguratorController
):

    @route()
    def website_sale_product_configurator_get_values(self, *args, **kwargs):
        _convert_rental_dates(kwargs)
        return super().website_sale_product_configurator_get_values(*args, **kwargs)

    @route()
    def website_sale_product_configurator_update_combination(self, *args, **kwargs):
        _convert_rental_dates(kwargs)
        return super().website_sale_product_configurator_update_combination(*args, **kwargs)

    @route()
    def website_sale_product_configurator_get_optional_products(self, *args, **kwargs):
        _convert_rental_dates(kwargs)
        return super().website_sale_product_configurator_get_optional_products(*args, **kwargs)

    @route()
    def website_sale_product_configurator_update_cart(self, *args, **kwargs):
        _convert_rental_dates(kwargs)
        return super().website_sale_product_configurator_update_cart(*args, **kwargs)

import { Component, whenReady } from "@mierp/owl";
import { Orders } from "@pos_order_tracking_display/app/components/orders/orders";
import { mierpLogo } from "@point_of_sale/app/generic_components/mierp_logo/mierp_logo";
import { useOrderStatusDisplay } from "./order_tracking_display_service";
import { mountComponent } from "@web/env";

export class OrderStatusDisplay extends Component {
    static template = "pos_order_tracking_display.OrderStatusDisplay";
    static components = { Orders, mierpLogo };
    static props = {};
    setup() {
        this.orders = useOrderStatusDisplay();
    }
}
whenReady(() => mountComponent(OrderStatusDisplay, document.body));

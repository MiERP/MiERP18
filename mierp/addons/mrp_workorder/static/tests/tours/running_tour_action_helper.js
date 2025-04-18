/** @mierp-module **/

import { animationFrame } from "@mierp/hoot-dom";
import { patch } from "@web/core/utils/patch";
import { TourHelpers } from "@web_tour/tour_service/tour_helpers";

patch(TourHelpers.prototype, {
    async scan(barcode) {
        mierp.__WOWL_DEBUG__.root.env.services.barcode.bus.trigger("barcode_scanned", { barcode });
        await animationFrame();
    },
});

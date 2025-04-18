import { router } from "@web/core/browser/router";
import { patch } from "@web/core/utils/patch";


/* if you guys at framework-js read this, we are sorry, bigram-request */
patch(router, {
    stateToUrl(state) {
        const url = super.stateToUrl(state);
        if (url.startsWith("/mierp/documents") && state.access_token) {
            return `/mierp/documents/${state.access_token}` + (
                mierp.debug ? `?debug=${mierp.debug}` : ''
            );
        }
        return url;
    },
});

/** @mierp-module **/

import { Component } from "@mierp/owl";

export class NewContentRefreshBanner extends Component {
    static template = "social.NewContentRefreshBanner";
    static props = [
        "refreshRequired",
        "onClickRefresh",
    ];
}

/** @mierp-module **/
import { BankRecFinishButtons } from "./finish_buttons";
import { Component, onWillUnmount } from "@mierp/owl";

export class BankRecRainbowContent extends Component {
    static template = "account_accountant.BankRecRainbowContent";
    static components = { BankRecFinishButtons };
    static props = {};

    setup() {
        onWillUnmount(() => {
            this.env.methods.initReconCounter();
        });
    }
}

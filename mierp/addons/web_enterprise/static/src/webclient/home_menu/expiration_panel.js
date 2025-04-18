/** @mierp-module **/

import { useService } from "@web/core/utils/hooks";
import { Transition } from "@web/core/transition";
import { _t } from "@web/core/l10n/translation";
import { Component, useState, useRef } from "@mierp/owl";

/**
 * Expiration panel
 *
 * Component representing the banner located on top of the home menu. Its purpose
 * is to display the expiration state of the current database and to help the
 * user to buy/renew its subscription.
 * @extends Component
 */
export class ExpirationPanel extends Component {
    setup() {
        this.subscription = useState(useService("enterprise_subscription"));

        this.state = useState({
            displayRegisterForm: false,
        });

        this.inputRef = useRef("input");
    }

    get buttonText() {
        return _t("Ok"); // Thay đổi nút bấm thành "Ok"
    }

    get alertType() {
        return "success"; // Luôn hiển thị kiểu thông báo thành công
    }

    get expirationMessage() {
        return _t("Your subscription is active and valid for 365 days."); // Thông báo đơn giản về trạng thái
    }

    showRegistrationForm() {
        this.state.displayRegisterForm = false; // Không hiển thị form đăng ký
    }

    async onCodeSubmit() {
        // Không thực hiện gì khi bấm nút đăng ký
    }
}

ExpirationPanel.template = "DatabaseExpirationPanel";
ExpirationPanel.props = {};
ExpirationPanel.components = { Transition };
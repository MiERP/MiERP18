/** @mierp-module **/

import { Component } from "@mierp/owl";

export class MrpDisplayEmployeesPanel extends Component {
    static template = "mrp_workorder.MrpDisplayEmployeesPanel";
    static props = {
        employees: { type: Object },
        setSessionOwner: { type: Function },
        popupAddEmployee: { type: Function },
        logout: { type: Function },
    };
}

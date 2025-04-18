import { Component } from "@mierp/owl";

export class mierpLogo extends Component {
    static template = "point_of_sale.mierpLogo";
    static props = {
        class: { type: String, optional: true },
        style: { type: String, optional: true },
        monochrome: { type: Boolean, optional: true },
    };
    static defaultProps = {
        class: "",
        style: "",
        monochrome: false,
    };
}

/** @mierp-module */

import { Component } from "@mierp/owl";

export class ChatterMessageCounter extends Component {
    static template = "project.ChatterMessageCounter";
    static props = {
        count: Number,
    };
}

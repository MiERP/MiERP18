/* @mierp-module */

import { Component } from "@mierp/owl";

export class SnailmailNotificationPopover extends Component {
    static template = "snailmail.SnailmailNotificationPopover";
    static props = ["message", "close?"];
}

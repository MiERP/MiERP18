/** @mierp-module */
import { Component } from "@mierp/owl";

export class ViewEditorSnackbar extends Component {
    static template = "web_studio.ViewEditor.Snackbar";
    static props = {
        operations: Object,
        saveIndicator: Object,
    };
}

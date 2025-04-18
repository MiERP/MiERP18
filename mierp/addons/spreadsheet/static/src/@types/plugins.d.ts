declare module "@spreadsheet" {
    import { CommandResult, CorePlugin, UIPlugin } from "@mierp/o-spreadsheet";
    import { CommandResult as CR } from "@spreadsheet/o_spreadsheet/cancelled_reason";
    type mierpCommandResult = CommandResult | typeof CR;

    export interface mierpCorePlugin extends CorePlugin {
        getters: mierpCoreGetters;
        dispatch: mierpCoreDispatch;
        allowDispatch(command: AllCoreCommand): string | string[];
        beforeHandle(command: AllCoreCommand): void;
        handle(command: AllCoreCommand): void;
    }

    export interface mierpCorePluginConstructor {
        new (config: unknown): mierpCorePlugin;
    }

    export interface mierpUIPlugin extends UIPlugin {
        getters: mierpGetters;
        dispatch: mierpDispatch;
        allowDispatch(command: AllCommand): string | string[];
        beforeHandle(command: AllCommand): void;
        handle(command: AllCommand): void;
    }

    export interface mierpUIPluginConstructor {
        new (config: unknown): mierpUIPlugin;
    }
}

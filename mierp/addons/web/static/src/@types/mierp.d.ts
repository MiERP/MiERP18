interface mierpModuleErrors {
    cycle?: string | null;
    failed?: Set<string>;
    missing?: Set<string>;
    unloaded?: Set<string>;
}

interface mierpModuleFactory {
    deps: string[];
    fn: mierpModuleFactoryFn;
    ignoreMissingDeps: boolean;
}

class mierpModuleLoader {
    bus: EventTarget;
    checkErrorProm: Promise<void> | null;
    /**
     * Mapping [name => factory]
     */
    factories: Map<string, mierpModuleFactory>;
    /**
     * Names of failed modules
     */
    failed: Set<string>;
    /**
     * Names of modules waiting to be started
     */
    jobs: Set<string>;
    /**
     * Mapping [name => module]
     */
    modules: Map<string, mierpModule>;

    constructor(root?: HTMLElement);

    addJob: (name: string) => void;

    define: (
        name: string,
        deps: string[],
        factory: mierpModuleFactoryFn,
        lazy?: boolean
    ) => mierpModule;

    findErrors: (jobs?: Iterable<string>) => mierpModuleErrors;

    findJob: () => string | null;

    reportErrors: (errors: mierpModuleErrors) => Promise<void>;

    sortFactories: () => void;

    startModule: (name: string) => mierpModule;

    startModules: () => void;
}

type mierpModule = Record<string, any>;

type mierpModuleFactoryFn = (require: (dependency: string) => mierpModule) => mierpModule;

declare const mierp: {
    csrf_token: string;
    debug: string;
    define: mierpModuleLoader["define"];
    loader: mierpModuleLoader;
};

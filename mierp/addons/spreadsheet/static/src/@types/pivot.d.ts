import { mierpPivotRuntimeDefinition } from "@spreadsheet/pivot/pivot_runtime";
import { ORM } from "@web/core/orm_service";
import { PivotMeasure } from "@spreadsheet/pivot/pivot_runtime";
import { ServerData } from "@spreadsheet/data_sources/server_data";
import { Pivot, CommonPivotCoreDefinition, PivotCoreDefinition } from "@mierp/o-spreadsheet";

declare module "@spreadsheet" {
    interface SortedColumn {
        groupId: number;
        measure: string;
        order: string;
    }

    export interface mierpPivotCoreDefinition extends CommonPivotCoreDefinition {
        type: "mierp";
        model: string;
        domain: Array;
        context: Object;
        sortedColumn: SortedColumn | null;
        actionXmlId: string;
    }

    export type ExtendedPivotCoreDefinition = PivotCoreDefinition | mierpPivotCoreDefinition;

    interface mierpPivot<T> extends Pivot<T> {
        type: ExtendedPivotCoreDefinition["type"];
    }
    export interface GFLocalPivot {
        id: string;
        fieldMatching: Record<string, any>;
    }

    export interface mierpField {
        name: string;
        type: string;
        string: string;
        relation?: string;
        searchable?: boolean;
        aggregator?: string;
        store?: boolean;
    }

    export type mierpFields = Record<string, Field | undefined>;

    export interface PivotMetaData {
        colGroupBys: string[];
        rowGroupBys: string[];
        activeMeasures: string[];
        resModel: string;
        fields?: Record<string, Field | undefined>;
        modelLabel?: string;
        sortedColumn: SortedColumn | null;
        fieldAttrs: any;
    }

    export interface PivotSearchParams {
        groupBy: string[];
        orderBy: string[];
        domain: Array;
        context: Object;
    }

    /* Params used for the mierp pivot model */
    export interface WebPivotModelParams {
        metaData: PivotMetaData;
        searchParams: PivotSearchParams;
    }

    export interface mierpPivotModelParams {
        fields: mierpFields;
        definition: mierpPivotRuntimeDefinition;
        searchParams: {
            domain: Array;
            context: Object;
        };
    }

    export interface PivotModelServices {
        serverData: ServerData;
        orm: ORM;
    }
}

import { beforeEach, describe, expect, test } from "@mierp/hoot";
import { getService, makeMockEnv } from "@web/../tests/web_test_helpers";

describe.current.tags("headless");

let titleService;

beforeEach(async () => {
    await makeMockEnv();
    titleService = getService("title");
});

test("simple title", () => {
    titleService.setParts({ one: "Mymierp" });
    expect(titleService.current).toBe("Mymierp");
});

test("add title part", () => {
    titleService.setParts({ one: "Mymierp", two: null });
    expect(titleService.current).toBe("Mymierp");
    titleService.setParts({ three: "Import" });
    expect(titleService.current).toBe("Mymierp - Import");
});

test("modify title part", () => {
    titleService.setParts({ one: "Mymierp" });
    expect(titleService.current).toBe("Mymierp");
    titleService.setParts({ one: "Zopenerp" });
    expect(titleService.current).toBe("Zopenerp");
});

test("delete title part", () => {
    titleService.setParts({ one: "Mymierp" });
    expect(titleService.current).toBe("Mymierp");
    titleService.setParts({ one: null });
    expect(titleService.current).toBe("mierp");
});

test("all at once", () => {
    titleService.setParts({ one: "Mymierp", two: "Import" });
    expect(titleService.current).toBe("Mymierp - Import");
    titleService.setParts({ one: "Zopenerp", two: null, three: "Sauron" });
    expect(titleService.current).toBe("Zopenerp - Sauron");
});

test("get title parts", () => {
    expect(titleService.current).toBe("");
    titleService.setParts({ one: "Mymierp", two: "Import" });
    expect(titleService.current).toBe("Mymierp - Import");
    const parts = titleService.getParts();
    expect(parts).toEqual({ one: "Mymierp", two: "Import" });
    parts.action = "Export";
    expect(titleService.current).toBe("Mymierp - Import"); // parts is a copy!
});

import mermaid from "https://unpkg.com/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({ startOnLoad: false });

await mermaid.run({ querySelector: ".mermaid" });

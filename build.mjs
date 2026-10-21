import { cp, mkdir, rm, writeFile } from "node:fs/promises";

const staticFiles = [
  "index.html",
  "index-en.html",
  "styles.css",
  "resume.pdf",
  "resume-en.pdf",
  "1641814386890.jpg",
  "media",
];

await rm("dist", { recursive: true, force: true });
await mkdir("dist/client", { recursive: true });
await mkdir("dist/server", { recursive: true });

await Promise.all(
  staticFiles.map((file) => cp(file, `dist/client/${file}`, { recursive: true })),
);

await writeFile(
  "dist/server/index.js",
  `export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  },
};
`,
);

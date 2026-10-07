# ship-ready

**English** · [Türkçe](README.tr.md)

ship-ready is a collection of Turkish checklists, guides, and a GitHub repository catalog for preparing personal projects built with AI for release.
It provides a public Astro Starlight site and a separate local view for project audit reports.

## What it includes

- Pre-release, App Store, Google Play, and paywall checklists with stable item IDs.
- Guides on AI development, UI/UX, analytics, and hosting, plus a catalog of verified GitHub repositories.
- A local view with audit reports and offline search, and a Python MCP server that exposes the content and reports to coding agents.
- A public site build that excludes audit reports and other local data.

## Stack and local use

The content and catalog use Markdown and JSON; the generators and MCP server use the Python standard library.
The site uses Astro and Starlight with Node.js and npm.
Run these commands from the repository root unless the command changes into `site/`:

| Task | Command |
|---|---|
| Install site dependencies | `cd site; npm ci` |
| Start the development server | `cd site; npm run dev` |
| Build the public site in `site/dist/` | `cd site; npm run build` |
| Preview the public build | `cd site; npm run preview` |
| Regenerate content and build the local view in `sayfa/` | `python uygulama/guncelle.py` |
| Validate item IDs, references, and reports | `python uygulama/katalog.py dogrula` |
| Refresh GitHub data and check content links | `python uygulama/guncelle.py --github` |

Install the site dependencies before building the local view.
After generating it, open the root `index.html` to reach `sayfa/`.

## Project structure

| Path | Contents |
|---|---|
| `icerik/` | Source checklists and guides. |
| `veri/` | Repository catalog, link check results, and local audit reports. |
| `uygulama/` | Catalog parser, site generator, update command, and MCP server. |
| `site/` | Astro Starlight site, components, styles, and live guide examples. |
| `skills/` | Audit skills for pre-release, App Store, and Google Play reviews. |
| `docs/proje-referansi.md` | Detailed reference for content formats, catalog data, reports, and site behavior. |

## Deployment and documentation

`site/dist/` is the public build output; this repository does not define a live deployment for it.
Audit reports appear only in the local view and MCP interface.
See the [project reference](docs/proje-referansi.md) for generation rules and site behavior, and the [hosting guide](icerik/yayina-alma-barindirma.md) for general release and hosting guidance.

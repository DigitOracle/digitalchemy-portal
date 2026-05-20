# DigitAlchemy® — Capabilities Portal

**Status:** v0.1 scaffold · Static site + Vercel Edge Middleware (HTTP Basic Auth)
**Owner:** DigitAlchemy® Tech Limited (ADGM 35004) · contact@digitalabbot.io
**Confidentiality:** Confidential preview. NDA required. Do not distribute.

## Layout

```
digitalchemy-portal/
├── index.html              Single-file portal (17 capability sections + grids + charts)
├── middleware.js           Vercel Edge Middleware — reads SITE_ACCESS_PASSWORD env var
├── vercel.json             Security headers (CSP, X-Frame-Options, noindex)
├── robots.txt              Disallow all (served without auth)
├── package.json            Minimal (static project, no framework)
├── public/
│   ├── videos/             Drop section videos here (see public/videos/README.md)
│   ├── data/               Corpus JSON for charts (auto-loaded)
│   └── img/                Brand assets, founder portrait
└── README.md               This file
```

## Local preview

The portal is a static `index.html` — but `fetch()` (used to probe video files) requires a server, so a `file://` double-click won't fully work.

From this folder:

```powershell
# Python
python -m http.server 8765

# OR Node
npx serve

# OR PHP
php -S localhost:8765
```

Then open <http://localhost:8765>.

## Adding videos

Drop MP4s into `public/videos/` using these exact filenames (auto-bind to each section):

| Section | File |
|---|---|
| Hero (full-bleed loop) | `hero.mp4` |
| 01 Periodichotomy® | `periodichotomy.mp4` |
| 02 DigitOracle® | `digitoracle.mp4` |
| 03 VIPER® | `viper.mp4` |
| 04 Digital Twin | `digital-twin.mp4` |
| 05 2D → Digital Twin Evolution | `2d-to-twin.mp4` |
| 06 SketchUp Front-End | `sketchup.mp4` |
| 07 BIM Front-End | `bim.mp4` |
| 08 AAS / Interoperability | `aas.mp4` |
| 09 AI Video Generator | `ai-video.mp4` |
| 10 Sovereign Domain Experts | `domain-experts.mp4` |
| 11 Digital Avatar / Concierge | `digital-concierge.mp4` |
| 12 Transparent Asset | `transparent-asset.mp4` |
| 13 15-Agent Ecosystem | `agent-ecosystem.mp4` |
| 14 Governance Dashboards | `governance.mp4` |
| 15 BaselineAudit | `baseline-audit.mp4` |
| 16 Smart City Consultancy | `smart-city.mp4` |
| 17 Education & Curriculum | `education.mp4` |

The page probes each file at load via `HEAD` and auto-replaces the placeholder if found. No code change needed — just drop the file.

Recommended specs: H.264 MP4, 1920×1080 (16:9), <10 MB, muted-friendly (no critical audio), 30–120 sec loop, web-optimised (`-movflags faststart`).

## Environment variables (set in Vercel dashboard — never commit)

| Name | Purpose | Deploy fallback |
|---|---|---|
| `SITE_ACCESS_PASSWORD` | HTTP Basic Auth password (any username accepted) | `DIGITALCHEMY-2026-CHANGE-ME` — **change before sharing URL** |

## Access

HTTP Basic Auth prompt appears on every route. Any username is accepted; only the password must match `SITE_ACCESS_PASSWORD`.

## Deploy

```powershell
vercel link            # link to DigitAlchemy projects team
vercel --prod          # deploy
```

Then in Vercel dashboard → Project Settings → Environment Variables, set `SITE_ACCESS_PASSWORD` to the shared passphrase.

## Content status

The 17 capability cards currently show placeholder text for **Problem** and **Differentiator** while the deep research pass runs. Solution copy is in place. When research returns the Problem and Differentiator blocks will be populated and the placeholder italic styling removed.

# Plug-in Roadmap · Vendor Icon Manifest

Save each vendor's official icon-mark (NOT wordmark) in this folder using the exact filename below. SVG preferred; transparent PNG acceptable as fallback.

Once a file lands here, tell me and I'll wire it into the matching chip on the portal.

## Source rule

Only pull from the vendor's **official brand portal / press / media kit / "brand resources" page** — never from third-party icon repackagers, never from Google Image search thumbnails. If the vendor's brand page only offers ZIP downloads, extract just the icon/symbol/mark variant (not the full wordmark with lockup).

## Filename manifest (matches plug-in roadmap chips on portal)

### Tier 01 · Production
- `revit.svg` — Autodesk Revit
- `sketchup.svg` — Trimble SketchUp

### Tier 02 · Beta
- `bluebeam.svg` — Nemetschek Bluebeam Revu
- `tekla.svg` — Trimble Tekla Structures
- `navisworks.svg` — Autodesk Navisworks Manage
- `autocad.svg` — Autodesk AutoCAD

### Tier 03 · 12-month roadmap
- `civil3d.svg` — Autodesk Civil 3D
- `infraworks.svg` — Autodesk Infraworks
- `solibri.svg` — Nemetschek Solibri
- `archicad.svg` — Graphisoft / Nemetschek Archicad
- `rhino.svg` — McNeel Rhino + Grasshopper
- `trimble-connect.svg` — Trimble Connect
- `projectsight.svg` — Trimble ProjectSight
- `aconex.svg` — Oracle Aconex
- `procore.svg` — Procore

### Tier 04 · 24-month strategic
- `arcgis-pro.svg` — Esri ArcGIS Pro
- `cityengine.svg` — Esri ArcGIS CityEngine
- `cesium.svg` — Cesium
- `lumion.svg` — Act-3D Lumion
- `twinmotion.svg` — Epic Games Twinmotion
- `enscape.svg` — Chaos Enscape
- `vray.svg` — Chaos V-Ray
- `unreal.svg` — Epic Games Unreal Engine
- `vectorworks.svg` — Nemetschek Vectorworks
- `allplan.svg` — Nemetschek Allplan
- `primavera.svg` — Oracle Primavera P6
- `blender.svg` — Blender Foundation (BlenderBIM)
- `speckle.svg` — Speckle
- `maximo.svg` — IBM Maximo
- `tririga.svg` — IBM TRIRIGA
- `dtwin.svg` — Nemetschek dTwin
- `spacewell.svg` — Nemetschek Spacewell

## Sizing

Each chip's icon slot is **44 × 44 px** with **4px padding** when an image is present (the badge background becomes white automatically via CSS `:has()` selector). SVGs scale natively. PNGs should be at least 88×88 (2× retina) for crisp rendering.

## Fallback

If a file is missing, the chip keeps its current brand-colored letter-mark — no broken state. So you can drop files in batches and the portal updates incrementally.

## Direct links to where these should come from

- **Trimble brand portal** (SketchUp, Tekla, Trimble Connect, ProjectSight): https://www.trimble.com → "Our Company" → "News" → "Media resources" / brand-assets request form
- **Nemetschek brand center** (Bluebeam, Archicad, Solibri, Vectorworks, Allplan, dTwin, Spacewell): https://www.nemetschek.com/en/media-and-publications
- **Graphisoft brand assets** (Archicad specifically): https://graphisoft.com/about-graphisoft/brand-assets
- **Autodesk brand center** (Revit, AutoCAD, Civil 3D, Infraworks, Navisworks): https://www.autodesk.com/company/legal-notices-trademarks (requires partner login for marks — third-party use restricted)
- **Oracle brand portal** (Aconex, Primavera): https://www.oracle.com/legal/trademarks.html
- **Esri brand center** (ArcGIS Pro, CityEngine): https://www.esri.com/en-us/legal/trademarks/about-trademarks
- **Cesium brand assets**: https://cesium.com/about/brand
- **Speckle**: their GitHub `speckle-design` repo or speckle.systems brand page
- **Blender Foundation logo**: https://www.blender.org/about/logo
- **Unreal Engine + Twinmotion (Epic Games)**: https://www.unrealengine.com/en-US/branding
- **Chaos brand assets** (V-Ray, Enscape): https://www.chaos.com/brand-resources
- **Lumion** (Act-3D): https://lumion.com/press
- **Procore**: https://www.procore.com/brand
- **IBM brand assets** (Maximo, TRIRIGA): https://www.ibm.com/brand/

## Trademark / brand-compliance reminder

For vendors where DigitAlchemy® has an authorized channel relationship (Trimble + Nemetschek brands via Medialogic), logo use is straightforward.

For vendors where DigitAlchemy® has no formal partnership (Autodesk, Oracle, Esri, Epic Games, Chaos, Act-3D, McNeel, Procore, IBM), logo use sits under **nominative fair use** — i.e., "we build plug-ins that integrate with this software." Most tech vendors permit this as long as the usage:
1. Doesn't imply endorsement or authorized-partner status you don't have
2. Doesn't alter the mark
3. Uses the mark only as much as needed to identify the product

Best practice for an investor-facing portal: keep a small "trademarks" footer line acknowledging that all vendor marks are property of their respective owners.

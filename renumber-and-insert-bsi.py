#!/usr/bin/env python3
"""
1. Renumber all existing capability cards (#02–#22) to (#03–#23) — done in reverse to avoid conflicts.
2. Insert new Card #02 · buildingSMART International — Open-Data Foundation.
3. Update the global '22 Capabilities' count to '23 Capabilities'.
4. Update Group 01 header to reflect the second card.
"""
import re

PORTAL = r"C:\Users\kwils\OneDrive\Desktop\DigitAlchemy\digitalchemy-portal\index.html"

with open(PORTAL, 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)
print(f"Original file: {original_len:,} chars")

# ============================================================
# STEP 1 · Renumber cap-NN-... in DESCENDING order (22 → 02)
# This shifts every card by +1. Existing #02 becomes #03, etc.
# ============================================================
total_replacements = 0
for n in range(22, 1, -1):  # 22, 21, ..., 2
    new_n = n + 1
    # Replace cap-XX- identifiers (anchors, hrefs)
    old_id = f'cap-{n:02d}-'
    new_id = f'cap-{new_n:02d}-'
    count = html.count(old_id)
    html = html.replace(old_id, new_id)
    total_replacements += count
    # Replace card-num label like "02 · Core Platform" — only when N appears with " · " suffix
    # We do these specifically because of risk of false positives. Inspect first.

print(f"Step 1 · cap-NN- renumbering: {total_replacements} replacements (#02→#03 through #22→#23)")

# ============================================================
# STEP 2 · Update card-num text labels (e.g., "02 · Core Platform" → "03 · Core Platform")
# These appear as <div class="card-num">NN · ...</div> in each card body.
# Also reverse order to avoid double-shifting.
# ============================================================
card_num_replacements = 0
for n in range(22, 1, -1):
    new_n = n + 1
    # Match patterns like '<div class="card-num">02 · Core Platform</div>'
    # The text is "NN · " followed by group name
    # Use regex to be safe: match `card-num">NN ·` and replace NN
    pattern = rf'(<div class="card-num">){n:02d}( · )'
    replacement = rf'\g<1>{new_n:02d}\g<2>'
    new_html, count = re.subn(pattern, replacement, html)
    html = new_html
    card_num_replacements += count

print(f"Step 2 · card-num labels: {card_num_replacements} replacements")

# ============================================================
# STEP 3 · Update mega-menu number chips and dropdown numbers
# Patterns: <span class="num">NN</span> for mega-items
#           "NN · " in dropdown <a> links
# ============================================================
mega_replacements = 0
for n in range(22, 1, -1):
    new_n = n + 1
    # Mega menu: <span class="num">NN</span>
    pattern1 = rf'(<span class="num">){n:02d}(</span>)'
    repl1 = rf'\g<1>{new_n:02d}\g<2>'
    html, c1 = re.subn(pattern1, repl1, html)
    mega_replacements += c1
    # Dropdown links: ">NN · " inside <a>
    # Be more specific: look for the pattern in nav contexts
    pattern2 = rf'(>){n:02d}( · )'
    repl2 = rf'\g<1>{new_n:02d}\g<2>'
    html, c2 = re.subn(pattern2, repl2, html)
    mega_replacements += c2

print(f"Step 3 · mega-menu + dropdown numbers: {mega_replacements} replacements")

# ============================================================
# STEP 4 · Update '22 Capabilities' references → '23 Capabilities'
# ============================================================
patterns_22 = [
    ('22 Capabilities', '23 Capabilities'),
    ('22 capabilities', '23 capabilities'),
    ('Twenty-Two Capabilities', 'Twenty-Three Capabilities'),
    ('the 22 ', 'the 23 '),
    ('22-capability', '23-capability'),
]
for old, new in patterns_22:
    c = html.count(old)
    if c > 0:
        html = html.replace(old, new)
        print(f"  · '{old}' → '{new}': {c} replacements")

# ============================================================
# STEP 5 · References to specific card numbers in body text
# (e.g., "Card 02 DigitOracle Enterprise" should become "Card 03 DigitOracle Enterprise")
# Patterns to match: "Card NN", "Cards NN", "Card N", "Cards N"
# ============================================================
# Only do this carefully — match "Card NN " with space after (avoids matching "Card NN.")
body_ref_replacements = 0
for n in range(22, 1, -1):
    new_n = n + 1
    patterns_card_ref = [
        (rf'\bCard {n:02d}\b', f'Card {new_n:02d}'),
        (rf'\bCard {n} ', f'Card {new_n} '),
    ]
    for pat, repl in patterns_card_ref:
        html, c = re.subn(pat, repl, html)
        body_ref_replacements += c

print(f"Step 5 · 'Card NN' body references: {body_ref_replacements} replacements")

# ============================================================
# STEP 6 · Insert new Card #02 · buildingSMART after the Group 1 header but before Card #03
# Find: '<article class="cap-card" id="cap-03-digitoracle">' (was cap-02 before renumber)
# Insert NEW card immediately before it, after the existing Periodichotomy card closing.
# Also rename Group 01 header to reflect dual nature.
# ============================================================

# First, update Group 01 header to reflect dual content
old_group01 = '<div class="group-header"><div class="group-num">Group 01 · Foundation</div><h3>The Regulatory Ontology Engine</h3></div>'
new_group01 = '<div class="group-header"><div class="group-num">Group 01 · Foundation</div><h3>The Regulatory Ontology Engine + Open-Data Standards</h3></div>'
if old_group01 in html:
    html = html.replace(old_group01, new_group01)
    print(f"Step 6a · Group 01 header updated")
else:
    print(f"Step 6a · Group 01 header NOT FOUND — may have already changed")

# Inline SVG icons matching the infographic brand style
# bSDD (violet), IFC (light blue), IDS (violet), Validation (green check)
BSI_CARD_HTML = '''
  <!-- 02. buildingSMART · Open-Data Foundation -->
  <article class="cap-card" id="cap-02-buildingsmart">
    <div class="inner">
      <div class="video-slot" data-video="buildingsmart">
        <div class="placeholder-icon"></div>
        <div class="placeholder-label">Video · buildingsmart.mp4</div>
      </div>
      <div class="body">
        <div class="card-num">02 · Foundation</div>
        <h4>buildingSMART International — Open-Data Foundation</h4>
        <div class="ps-block" data-field="problem"><span class="lbl">The Problem</span><div class="text">The AECO industry has a digital-thread problem. Asset classifications live in vendor silos. Sensor properties have no shared dictionary. Information requirements aren't formalized. Without a standardized open-data foundation, every digital twin becomes a custom integration project — expensive, fragile, non-portable.</div></div>
        <div class="ps-block" data-field="solution"><span class="lbl">The Solution</span><div class="text">DigitAlchemy® integrates the full buildingSMART stack. <strong>bSDD</strong> (Data Dictionary) classifies assets, spaces, and sensor properties. <strong>IFC 4.3 / ISO 16739-1:2024</strong> carries geometry and metadata. <strong>IDS</strong> (Information Delivery Specifications) formalizes what must be delivered. VIPER™ sensor placement maps directly to bSDD-typed properties.</div></div>
        <div class="ps-block" data-field="differentiator"><span class="lbl">What Makes Us Different</span><div class="text">Most platforms claim openness; few ship it. Every DigitAlchemy® plug-in exports schema-valid IFC 4.3 with bSDD-typed properties. VIPER™ sensor logic maps directly to bSDD. IDS formalizes what must be delivered — making compliance auditable end-to-end. Our corpus is trained on the bSI standards stack.</div></div>
        <div class="meta">
          <span><strong class="agent-tag">Relationship:</strong> Open-Standards Integration · buildingSMART International (bSI)</span>
          <span><strong>Scope:</strong> bSDD · IFC 4.3 ADD2 · IDS · ISO 16739-1:2024 · BCF · IDM/MVD</span>
          <span><strong>Roadmap:</strong> bSI Software Certification target Q3 2027 (Revit + SketchUp plug-ins)</span>
        </div>
        <div class="diagram">
          <div class="diagram-label">The Open-Data Substrate · bSDD + IFC + IDS</div>
          <div class="bsi-stack">
            <div class="bsi-icon bsi-bsdd">
              <span class="bsi-icon-text">bSDD</span>
              <span class="bsi-icon-cap">Data Dictionary</span>
            </div>
            <div class="bsi-icon-plus">+</div>
            <div class="bsi-icon bsi-ifc">
              <span class="bsi-icon-text">IFC</span>
              <span class="bsi-icon-cap">ISO 16739-1:2024</span>
            </div>
            <div class="bsi-icon-plus">+</div>
            <div class="bsi-icon bsi-ids">
              <span class="bsi-icon-text">IDS</span>
              <span class="bsi-icon-cap">Info Delivery Specs</span>
            </div>
          </div>
          <div class="bsi-outcomes">
            <span>Global Standards Interoperability</span>
            <span>Trusted Data Exchange</span>
            <span>Higher Quality Information</span>
            <span>Better Decisions, Better Outcomes</span>
          </div>
          <div class="diagram-note">Open-Data Foundation. Not a product. Not a partner. Included in every DigitAlchemy® plug-in seat and platform tier by architecture.</div>
        </div>
      </div>
    </div>
  </article>

'''

# Insert the new card BEFORE the renumbered DigitOracle card
target = '<!-- 03. DigitOracle™ -->\n  <article class="cap-card" id="cap-03-digitoracle">'
if target in html:
    # Insert the buildingSMART card before the DigitOracle comment
    new_target = BSI_CARD_HTML.strip() + '\n\n  <!-- 03. DigitOracle™ -->\n  <article class="cap-card" id="cap-03-digitoracle">'
    html = html.replace(target, new_target)
    print(f"Step 6b · Inserted buildingSMART card before DigitOracle (now Card #03)")
else:
    print(f"Step 6b · WARNING: Target DigitOracle anchor not found. Manual insert needed.")

# Also need to update the OLD comment line "<!-- 02. DigitOracle™ -->" that exists
# Hmm wait — that comment was BEFORE step 1 renumbering. After renumbering, the
# anchor is cap-03-digitoracle but the COMMENT "<!-- 02. DigitOracle™ -->" remains.
# Let me check that.
# Actually the comments are static text — they didn't get touched by step 1 (which only
# renumbered cap-NN- ids). Let me also update comments.
comment_replacements = 0
# Match patterns like <!-- 02. DigitOracle --> and shift all by +1 (already done above for cap-NN-, but comments are separate)
for n in range(22, 1, -1):
    new_n = n + 1
    pattern = rf'<!-- {n:02d}\. ([A-Z])'
    replacement = rf'<!-- {new_n:02d}. \g<1>'
    html, c = re.subn(pattern, replacement, html)
    comment_replacements += c

print(f"Step 7 · HTML comments renumbered: {comment_replacements}")

# ============================================================
# Write back
# ============================================================
with open(PORTAL, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nFinal file: {len(html):,} chars (+{len(html) - original_len:,})")
print(f"Saved: {PORTAL}")

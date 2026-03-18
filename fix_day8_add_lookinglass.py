#!/usr/bin/env python3
"""
Fix: Add Looking Glass Falls to Day 8 (DuPont/Brevard day).

Looking Glass Falls is roadside on US-276, ~15 min north of Brevard.
Perfect first stop on the way to DuPont State Forest.
After yesterday's storms, the waterfall will be roaring!

Run from the trip-plan repo root: python fix_day8_add_lookinglass.py
(Run AFTER fix_day7_waterfalls.py)
"""
import os
import re

HTML_FILE = "index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

LOOKING_GLASS_SECTION = """
<div class="alert" style="background:#e8f5e9;border:2px solid #4caf50;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong>&#127786;&#65039; BONUS: Looking Glass Falls (moved from Day 7)</strong><br>
<a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a> is a stunning 60-ft waterfall right off US-276, just 15 min north of Brevard. It&rsquo;s a quick roadside stop &mdash; walk down ~60 steps to the base, snap photos, and you&rsquo;re done in 15&ndash;20 min. <strong>After Monday&rsquo;s storms, this waterfall will be absolutely roaring.</strong> FREE, no hike required.
<ul style="margin:8px 0 0 0;">
<li><strong>Location:</strong> US-276 N, Pisgah Forest (between Brevard and Pisgah NF)</li>
<li><strong>When to stop:</strong> On the way TO DuPont (morning) or on the way BACK (afternoon) &mdash; it&rsquo;s right on the route</li>
<li><strong>Add ~25 min to your day</strong> (15 min detour + 10 min at the falls)</li>
</ul>
</div>

"""

def main():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: {HTML_FILE} not found. Run from the trip-plan repo root.")
        return

    html = read_html()

    day8_start = html.find('<h2 id="day-8">')
    day9_start = html.find('<h2 id="day-9">')

    if day8_start == -1:
        print("ERROR: Could not find Day 8 section header.")
        return

    if day9_start == -1:
        print("ERROR: Could not find Day 9 section header (needed as boundary).")
        return

    day8_section = html[day8_start:day9_start]

    # Strategy: Insert the Looking Glass Falls box right after the Day 8
    # intro paragraph(s) and before the first <h3> subsection.
    # This puts it prominently near the top of the day.
    first_h3 = day8_section.find('<h3')
    if first_h3 == -1:
        # No h3 found - insert after the first </p> or </table> instead
        first_p_end = day8_section.find('</p>')
        if first_p_end != -1:
            insert_pos = first_p_end + len('</p>')
        else:
            # Just insert after the h2 line
            h2_end = day8_section.find('</h2>')
            insert_pos = h2_end + len('</h2>')
    else:
        insert_pos = first_h3

    # Build the new Day 8 section with Looking Glass Falls inserted
    new_day8 = day8_section[:insert_pos] + LOOKING_GLASS_SECTION + day8_section[insert_pos:]

    html = html[:day8_start] + new_day8 + html[day9_start:]

    write_html(html)

    old_len = len(day8_section)
    new_len = len(new_day8)
    print("Done! Looking Glass Falls added to Day 8.")
    print(f"  Section size: {old_len} -> {new_len} chars (+{new_len - old_len})")
    print("")
    print("Looking Glass Falls details:")
    print("  - 60-ft waterfall, roadside on US-276")
    print("  - ~15 min north of Brevard")
    print("  - Walk down 60 steps, photos, 15-20 min total")
    print("  - FREE, no hike required")
    print("  - After Monday's storms = roaring water flow!")
    print("")
    print("Preview: python -m http.server 8000")
    print("Then open http://localhost:8000 in your browser")
    print("")
    print("When ready:")
    print('  git add index.html && git commit -m "Update Day 7 & 8: move Looking Glass Falls to DuPont day" && git push')

if __name__ == "__main__":
    main()

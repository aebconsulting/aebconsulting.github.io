#!/usr/bin/env python3
"""
Fix script: Update Day 6 (3/16) and Day 7 (3/17) in trip-plan index.html

Day 6: Chimney Rock + Black Mountain -> Cabin Day (storms & snow)
Day 7: St. Patrick's Day + Pisgah Waterfalls -> Chimney Rock AM + Looking Glass Falls PM

Run from the trip-plan repo root:
  python fix_day6_day7.py
"""
import re
import os

HTML_FILE = "index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

# ============================================================
# NEW DAY 6 CONTENT — Cabin Day (Storms & Snow)
# ============================================================
NEW_DAY6 = """<h2 id="day-6">Day 6 &mdash; Monday, March 16th: Cabin Day &mdash; Storms &amp; Snow</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#127783;&#65039; Rest &amp; Recharge &mdash; Storms kept us cozy at the cabin</p>

<div class="alert" style="background:#fff3e0;border:2px solid #ff9800;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong style="color:#e65100;">&#9888;&#65039; Weather Alert:</strong> Storms and snow rolled through western NC all day. Roads through Hickory Nut Gorge and mountain passes had hazardous conditions. Chimney Rock State Park visit postponed to Day 7 (March 17).
</div>

<p><strong>What happened:</strong> Bad storms and snow hit the area throughout the day. We made the smart call to stay in and enjoy the cabin rather than risk mountain driving in poor conditions.</p>

<p><strong>How we spent the day:</strong></p>
<ul>
<li>Slept in and enjoyed a slow breakfast at the rental</li>
<li>Watched the snow fall from the cabin &mdash; beautiful mountain scenery</li>
<li>Indoor play, movies, and family downtime</li>
<li>Regrouped and replanned: moved Chimney Rock to tomorrow morning, added Looking Glass Falls for the afternoon</li>
</ul>

<p><strong>Revised plan for Day 7:</strong> With Chimney Rock pushed to tomorrow, we combined it with a stop at Looking Glass Falls on the way back &mdash; turning Day 7 into a full hiking day: Chimney Rock in the morning + Looking Glass Falls in the afternoon.</p>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Silver lining:</strong> A rest day before two hikes was the right call. The storm brought fresh snow to the mountain peaks, making for stunning scenery at Chimney Rock and Looking Glass Falls the next day. Plus, everyone was well-rested and energized for a big hiking day.
</div>

<p><strong>Scouting note:</strong> Even on a rest day, we noticed how the cabin neighborhood handled winter weather &mdash; road maintenance, power reliability, and the general preparedness of mountain living. Good data point for the relocation scouting.</p>

"""

# ============================================================
# NEW DAY 7 CONTENT — Chimney Rock AM + Looking Glass Falls PM
# ============================================================
NEW_DAY7 = """<h2 id="day-7">Day 7 &mdash; Tuesday, March 17th: Chimney Rock + Looking Glass Falls</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#9968;&#65039; Summit + Waterfalls &mdash; Chimney Rock Views + Looking Glass Falls</p>

<p><strong>&#128205; Route &amp; Distances:</strong> <a href="https://www.google.com/maps/dir/35.612841,-82.665031/Chimney+Rock+State+Park,+NC/Lake+Lure,+NC/Looking+Glass+Falls,+Pisgah+Forest,+NC/35.612841,-82.665031">Day 7 Google Map</a></p>

<table>
<thead><tr><th>#</th><th>Segment</th><th>Miles</th><th>Drive Time</th><th>Route</th></tr></thead>
<tbody>
<tr><td>1</td><td>Candler rental &rarr; <a href="https://www.chimneyrockpark.com" target="_blank" rel="noopener noreferrer">Chimney Rock State Park</a></td><td>~45 mi</td><td>~1 hr 10 min</td><td>I-40 E &rarr; I-26 E &rarr; <strong>Exit 49A</strong> &rarr; US-64 E (18 mi) &rarr; NC-9 S through Lake Lure</td></tr>
<tr><td>2</td><td>Chimney Rock &rarr; Lake Lure (town center)</td><td>~3 mi</td><td>~7 min</td><td>NC-9 / US-64 along the gorge</td></tr>
<tr><td>3</td><td>Lake Lure &rarr; Looking Glass Falls</td><td>~55 mi</td><td>~1 hr 15 min</td><td>US-64 W &rarr; Bat Cave &rarr; I-26 W &rarr; NC-280 E &rarr; US-276 N</td></tr>
<tr><td>4</td><td>Looking Glass Falls &rarr; Candler rental</td><td>~40 mi</td><td>~50 min</td><td>US-276 S &rarr; NC-280 W &rarr; NC-191 N</td></tr>
<tr><td></td><td><strong>Day 7 Total</strong></td><td><strong>~143 mi</strong></td><td><strong>~3 hr 22 min</strong></td><td><em>Chimney Rock via NC-9/Lake Lure ONLY open route</em></td></tr>
</tbody>
</table>

<div class="alert" style="background:#fef3cd;border:2px solid #ffc107;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong>&#9888;&#65039; ROUTE WARNING &mdash; READ BEFORE DRIVING:</strong><br>
The ONLY open route into Chimney Rock is <strong>NC-9 through Lake Lure</strong> (from the south/east). All other routes are CLOSED to non-local traffic:
<ul style="margin:8px 0 0 0;">
<li>US-74A from Asheville &mdash; <strong>CLOSED</strong></li>
<li>US-64 from Hendersonville &mdash; <strong>CLOSED</strong></li>
<li>NC-9 from Black Mountain &mdash; <strong>CLOSED</strong></li>
</ul>
<strong>GPS WARNING:</strong> Your GPS will likely try to route you via CLOSED roads. Override it and follow this route:
Take I-40 E &rarr; I-26 E &rarr; <strong>Exit 49A</strong> &rarr; US-64 East (18 mi through Bat Cave) &rarr; NC-9 South into Lake Lure &rarr; Chimney Rock. ~1 hr 10 min. Check DriveNC.gov the morning of for any updates.
</div>

<p><strong>Post-storm trail conditions:</strong> After yesterday&rsquo;s storms and snow, expect trails to be wet with possible icy patches at higher elevations. Wear waterproof boots and dress in layers. Downed branches are possible. The fresh snow on the peaks should make for spectacular views!</p>

<h3>Morning &mdash; Chimney Rock State Park</h3>

<p><strong>HIKE &mdash; <a href="https://www.chimneyrockpark.com" target="_blank" rel="noopener noreferrer">Chimney Rock State Park</a>:</strong></p>
<ul>
<li><strong><a href="https://www.chimneyrockpark.com/view_trail/outcroppings-trail/" target="_blank" rel="noopener noreferrer">Outcroppings Trail</a></strong> &mdash; 0.25 miles, paved, to a stunning overlook. Easy for little legs.</li>
<li><strong><a href="https://www.chimneyrockpark.com/view_trail/hickory-nut-falls-trail/" target="_blank" rel="noopener noreferrer">Hickory Nut Falls Trail</a></strong> &mdash; 1.4 miles round trip to 400-ft waterfall. Moderate but doable for a motivated kid.</li>
<li>Option: Take the <strong>elevator</strong> to the top instead of hiking (26-story elevator inside the mountain!)</li>
<li><strong>Exclamation Point Trail</strong> &mdash; 1.4 mi round trip. Moderate. Best panoramic views of Lake Lure &amp; Hickory Nut Gorge.</li>
<li><strong>Four Seasons Trail</strong> &mdash; 0.6 mi. Easy nature walk through forest canopy back toward parking.</li>
<li><strong style="color:#15803d;">Chimney Rock reservation (moved from 3/16).</strong> Check with park about using timed-entry ticket on 3/17 &mdash; call <a href="tel:8286259611">(828) 625-9611</a> to confirm.</li>
</ul>

<p><strong>Suggested Morning Schedule:</strong></p>
<ul>
<li><strong>8:30 AM</strong> &mdash; Arrive at park entrance, buy tickets / confirm reservation</li>
<li><strong>9:00 AM</strong> &mdash; Take elevator or stairs to Chimney summit viewpoint</li>
<li><strong>9:30 AM</strong> &mdash; Hike Skyline&ndash;Cliff Trail to Exclamation Point</li>
<li><strong>10:15 AM</strong> &mdash; Hike Hickory Nut Falls Trail to waterfall overlook</li>
<li><strong>11:30 AM</strong> &mdash; Walk Four Seasons Trail back toward parking</li>
<li><strong>12:00 PM</strong> &mdash; Lunch in Chimney Rock Village or Lake Lure</li>
</ul>

<p><strong>Midday:</strong></p>
<ul>
<li><strong>Lake Lure</strong> &mdash; scenic lakeside town, skip rocks, grab ice cream</li>
</ul>

<h3>Afternoon &mdash; Looking Glass Falls (Pisgah National Forest)</h3>

<p><strong>Drive:</strong> Depart Chimney Rock / Lake Lure ~1:30 PM. Drive ~1 hr 15 min via US-64 W &amp; US-276 to Looking Glass Falls.</p>

<ul>
<li><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></strong> &mdash; 60-ft waterfall right off US-276. Visible from the roadside pull-off. Short paved staircase (~60 steps) down to the base. FREE. Allow 30&ndash;45 minutes.</li>
<li><strong>Post-storm bonus:</strong> March water levels after yesterday&rsquo;s storms should make the falls especially impressive and powerful.</li>
</ul>

<table>
<thead><tr><th>Trail</th><th>Distance</th><th>Difficulty</th><th>Highlight</th></tr></thead>
<tbody>
<tr><td><strong>Looking Glass Falls</strong></td><td>Roadside (steps only)</td><td>Easy</td><td>60-ft waterfall right off the road. Quick and stunning.</td></tr>
</tbody>
</table>

<p><strong>Nearby Bonus Stops:</strong></p>
<ul>
<li><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></strong> &mdash; 7 min drive. Natural 60-ft rock waterslide (seasonal &mdash; may be closed in March, but worth a quick look)</li>
<li><strong>Brevard</strong> &mdash; 15 min drive. Charming downtown with shops, coffee, and ice cream</li>
</ul>

<p><strong>Suggested Afternoon Schedule:</strong></p>
<ul>
<li><strong>1:30 PM</strong> &mdash; Depart Chimney Rock / Lake Lure</li>
<li><strong>2:45 PM</strong> &mdash; Arrive at Looking Glass Falls pull-off</li>
<li><strong>2:50 PM</strong> &mdash; Walk down staircase to falls base, explore &amp; take photos</li>
<li><strong>3:30 PM</strong> &mdash; Optional: Drive to Sliding Rock for a quick look</li>
<li><strong>4:00 PM</strong> &mdash; Head to Brevard for snacks or back to the cabin</li>
</ul>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Tip:</strong> Arrive at Chimney Rock when the park opens at 8:30 AM to beat crowds and have time for both locations. The elevator to the top saves energy for the trails. Looking Glass Falls is a quick 30&ndash;45 min stop &mdash; the drive from Chimney Rock is scenic through the mountains. Bring a jacket &mdash; the mist at the falls is cold, especially after yesterday&rsquo;s storm!
</div>

<p><strong>Evening &mdash; St. Patrick&rsquo;s Day!</strong></p>
<ul>
<li>Family-friendly St. Patrick&rsquo;s Day dinner (green everything!)</li>
<li>Parents&rsquo; option: Brewery crawl if kid goes to bed at lodging</li>
<li>Look for <strong>Random Acts of Fringe</strong> pop-ups around downtown (free, all-ages)</li>
</ul>

<p><strong>Backup if kid is tired after Chimney Rock:</strong></p>
<ul>
<li>Skip Looking Glass Falls &mdash; head back to the rental for rest</li>
<li><strong>Mountain Play Lodge</strong> or movie night at lodging &mdash; recharge for DuPont tomorrow</li>
</ul>

<p><strong>Scouting note &mdash; Chimney Rock &amp; Pisgah area:</strong> Notice the post-Helene recovery along NC-9 and through Hickory Nut Gorge. The drive to Looking Glass Falls via US-276 gives you a feel for what &ldquo;outdoor living&rdquo; means here &mdash; world-class nature close to town.</p>

"""

def apply_fixes(html):
    # =============================================
    # 1. Replace Day 6 section (from <h2 id="day-6"> to <h2 id="day-7">)
    # =============================================
    day6_start = html.find('<h2 id="day-6">')
    day7_start = html.find('<h2 id="day-7">')
    if day6_start == -1 or day7_start == -1:
        print("ERROR: Could not find Day 6 or Day 7 headers")
        return html

    html = html[:day6_start] + NEW_DAY6 + html[day7_start:]

    # =============================================
    # 2. Replace Day 7 section (from <h2 id="day-7"> to <h2 id="day-8">)
    # =============================================
    day7_start = html.find('<h2 id="day-7">')
    day8_start = html.find('<h2 id="day-8">')
    if day7_start == -1 or day8_start == -1:
        print("ERROR: Could not find Day 7 or Day 8 headers")
        return html

    html = html[:day7_start] + NEW_DAY7 + html[day8_start:]

    # =============================================
    # 3. Update flexibility guide references
    # =============================================
    html = html.replace(
        '<li><strong>Day 6 (Mon, March 16) &mdash; Chimney Rock</strong> &mdash; timed-entry reservation (book for this date, open Thu&ndash;Mon)</li>',
        '<li><strong>Day 6 (Mon, March 16) &mdash; Cabin Day</strong> &mdash; storms &amp; snow forced a rest day (Chimney Rock moved to Day 7)</li>'
    )
    # Try encoded version too
    html = html.replace(
        'Day 6 (Mon, March 16) ΓÇö Chimney Rock</strong> ΓÇö timed-entry reservation',
        'Day 6 (Mon, March 16) ΓÇö Cabin Day</strong> ΓÇö storms &amp; snow (Chimney Rock moved to Day 7)'
    )

    html = html.replace(
        '<li><strong>Day 7 (Tue, March 17) &mdash; St. Patrick&rsquo;s Day</strong> &mdash; date-specific</li>',
        '<li><strong>Day 7 (Tue, March 17) &mdash; Chimney Rock + Looking Glass Falls</strong> &mdash; moved from Day 6 + afternoon waterfall</li>'
    )
    html = html.replace(
        'Day 7 (Tue, March 17) ΓÇö St. PatrickΓÇÖs Day</strong> ΓÇö date-specific',
        'Day 7 (Tue, March 17) ΓÇö Chimney Rock + Looking Glass Falls</strong> ΓÇö moved from Day 6'
    )

    # =============================================
    # 4. Update Events Calendar table
    # =============================================
    # Day 6 row
    html = html.replace(
        '<td>Chimney Rock + Black Mountain</td>\n<td>Chimney Rock / Black Mtn</td>',
        '<td><strong>Cabin Day</strong> &mdash; storms &amp; snow, stayed in</td>\n<td>Cabin (Candler rental)</td>'
    )
    # Also try without newline
    html = html.replace(
        'Chimney Rock + Black Mountain</td>',
        'Cabin Day &mdash; storms &amp; snow</td>',
        1  # only first occurrence in events calendar
    )

    # Day 7 row in events calendar
    html = html.replace(
        'St. Patrick&rsquo;s Day + <strong>Pisgah Waterfalls</strong>',
        'Chimney Rock AM + Looking Glass Falls PM + St. Patrick&rsquo;s Day evening'
    )

    # =============================================
    # 5. Update Driving Summary table
    # =============================================
    html = html.replace(
        'Chimney Rock + Black Mountain (heavy',
        'Cabin Day &mdash; no driving (storms'
    )
    html = html.replace(
        '<td>~117 mi</td>',
        '<td>0 mi</td>',
        1  # only first occurrence
    )

    # =============================================
    # 6. Update weather API coordinates
    # =============================================
    # Day 6: change from Chimney Rock to cabin location
    html = html.replace(
        '{ day: 6, date: "2026-03-16", lat: 35.439, lon: -82.2462, name: "Chimney Rock NC" }',
        '{ day: 6, date: "2026-03-16", lat: 35.6128, lon: -82.665, name: "Cabin (Candler NC)" }'
    )
    # Day 7: change from Pisgah to Chimney Rock (morning location)
    html = html.replace(
        '{ day: 7, date: "2026-03-17", lat: 35.2716, lon: -82.7717, name: "Pisgah Forest NC" }',
        '{ day: 7, date: "2026-03-17", lat: 35.439, lon: -82.2462, name: "Chimney Rock + Looking Glass Falls" }'
    )

    # =============================================
    # 7. Update booking checklist
    # =============================================
    html = html.replace(
        'Chimney Rock</strong> timed-entry',
        'Chimney Rock</strong> timed-entry (rescheduled from 3/16 due to storms)'
    )

    # =============================================
    # 8. Update the day nav link text for day 6
    # =============================================
    html = html.replace(
        '<a href="#day-6">6</a>',
        '<a href="#day-6">6 &#127783;</a>'
    )

    # =============================================
    # 9. Update county reference for Day 6 driving
    # =============================================
    # Henderson, Rutherford (Chimney Rock) -> Cabin day, no driving
    html = html.replace(
        '6: [45, 80],  // Henderson, Rutherford (Chimney Rock)',
        '6: [11, 11],  // Cabin day - Buncombe (stayed in)'
    )

    return html

def main():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: {HTML_FILE} not found. Run this script from the trip-plan repo root.")
        return

    print("Reading index.html...")
    html = read_html()
    original_len = len(html)

    print("Applying Day 6 & Day 7 fixes...")
    html = apply_fixes(html)

    if len(html) == original_len:
        print("WARNING: No changes detected. Patterns may not have matched.")
    else:
        diff = len(html) - original_len
        print(f"Changes applied (size diff: {diff:+d} chars)")

    write_html(html)
    print(f"Updated {HTML_FILE} successfully!")
    print("\nChanges made:")
    print("  Day 6 (3/16): Chimney Rock + Black Mountain -> Cabin Day (storms & snow)")
    print("  Day 7 (3/17): St. Patrick's Day + Pisgah -> Chimney Rock AM + Looking Glass Falls PM")
    print("  Updated: flexibility guide, events calendar, driving summary,")
    print("           weather API coords, booking checklist, nav links")
    print("\nNext: review changes, then git add/commit/push")

if __name__ == "__main__":
    main()

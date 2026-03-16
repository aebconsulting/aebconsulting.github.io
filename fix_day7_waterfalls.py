#!/usr/bin/env python3
"""
Fix: Update Day 7 with optimal waterfall route after Chimney Rock.

Route: Chimney Rock -> US-64 W -> US-276 N through Pisgah NF
All waterfalls are sequential along US-276 heading north:
  1. Looking Glass Falls (roadside)
  2. Moore Cove Falls (1.2 mi RT - walk BEHIND a waterfall)
  3. Sliding Rock (roadside - quick look)
  4. Skinny Dip Falls (BRP MP 417 - if time/energy)
Then home via BRP north -> NC-191

Run from the trip-plan repo root: python fix_day7_waterfalls.py
"""
import os

HTML_FILE = "index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

# The entire Day 7 section from <h2 id="day-7"> to <h2 id="day-8">
NEW_DAY7 = """<h2 id="day-7">Day 7 &mdash; Tuesday, March 17th: Chimney Rock + Waterfall Trail</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#9968;&#65039; Elevator to the Summit + Pisgah Waterfall Trail &mdash; up to 4 waterfalls in one afternoon</p>

<p><strong>&#128205; Route &amp; Distances:</strong> <a href="https://www.google.com/maps/dir/35.612841,-82.665031/Chimney+Rock+State+Park,+NC/Looking+Glass+Falls,+Pisgah+Forest,+NC/Moore+Cove+Falls,+NC/Sliding+Rock,+Pisgah+Forest,+NC/Skinny+Dip+Falls,+NC/35.612841,-82.665031" target="_blank" rel="noopener noreferrer">Day 7 Google Map</a></p>

<table>
<thead><tr><th>#</th><th>Segment</th><th>Miles</th><th>Drive Time</th><th>Route</th></tr></thead>
<tbody>
<tr><td>1</td><td>Candler rental &rarr; <a href="https://www.chimneyrockpark.com" target="_blank" rel="noopener noreferrer">Chimney Rock State Park</a></td><td>~45 mi</td><td>~1 hr 10 min</td><td>I-40 E &rarr; I-26 E &rarr; <strong>Exit 49A</strong> &rarr; US-64 E (18 mi) &rarr; NC-9 S through Lake Lure</td></tr>
<tr><td>2</td><td>Chimney Rock &rarr; Looking Glass Falls</td><td>~55 mi</td><td>~1 hr 15 min</td><td>US-64 W through Bat Cave &rarr; I-26 W &rarr; NC-280 E &rarr; US-276 N into Pisgah NF</td></tr>
<tr><td>3</td><td>Looking Glass Falls &rarr; Moore Cove Falls</td><td>~1 mi</td><td>~2 min</td><td>Continue north on US-276</td></tr>
<tr><td>4</td><td>Moore Cove Falls &rarr; Sliding Rock</td><td>~3 mi</td><td>~5 min</td><td>Continue north on US-276</td></tr>
<tr><td>5</td><td>Sliding Rock &rarr; Skinny Dip Falls (BRP MP 417)</td><td>~11 mi</td><td>~20 min</td><td>US-276 N &rarr; BRP at MP 411.8 &rarr; south to MP 417</td></tr>
<tr><td>6</td><td>Skinny Dip Falls &rarr; Candler rental</td><td>~23 mi</td><td>~45 min</td><td>BRP north &rarr; NC-191 exit near NC Arboretum</td></tr>
<tr><td></td><td><strong>Day 7 Total</strong></td><td><strong>~138 mi</strong></td><td><strong>~3 hr 37 min driving</strong></td><td><em>All waterfalls are sequential along US-276 &mdash; no backtracking!</em></td></tr>
</tbody>
</table>

<div class="alert" style="background:#fef3cd;border:2px solid #ffc107;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong>&#9888;&#65039; CHIMNEY ROCK ROUTE WARNING:</strong><br>
The ONLY open route into Chimney Rock is <strong>NC-9 through Lake Lure</strong> (from the south/east). All other routes are CLOSED:
<ul style="margin:8px 0 0 0;">
<li>US-74A from Asheville &mdash; <strong>CLOSED</strong></li>
<li>US-64 from Hendersonville &mdash; <strong>CLOSED</strong></li>
<li>NC-9 from Black Mountain &mdash; <strong>CLOSED</strong></li>
</ul>
<strong>GPS WARNING:</strong> Override GPS! Take I-40 E &rarr; I-26 E &rarr; <strong>Exit 49A</strong> &rarr; US-64 E (18 mi through Bat Cave) &rarr; NC-9 S into Lake Lure &rarr; Chimney Rock. Check DriveNC.gov morning of.
</div>

<p><strong>Post-storm trail conditions:</strong> After yesterday&rsquo;s storms and snow, expect wet trails with possible icy patches at higher elevations. Wear waterproof boots and layers. The fresh snow on peaks = spectacular views, and the heavy rain means the waterfalls will be roaring!</p>

<h3>Morning &mdash; Chimney Rock State Park (10:00&ndash;11:45 AM)</h3>

<p><strong>The Plan:</strong> Elevator to the top, short hike to Exclamation Point for panoramic views, then move on to the waterfalls.</p>

<ul>
<li><strong>Elevator to the top</strong> &mdash; 26-story elevator inside the mountain takes you straight to the Chimney summit. No hiking needed to reach the top!</li>
<li><strong>Skyline&ndash;Cliff Trail to Exclamation Point</strong> &mdash; 0.4 mi, easy. Short walk from the Chimney to the highest publicly accessible point. Best panoramic views of Lake Lure &amp; Hickory Nut Gorge. <strong>This is the main hike.</strong></li>
<li><em>Skip Hickory Nut Falls Trail (1.4 mi) to save legs for the afternoon waterfalls.</em></li>
<li><strong style="color:#15803d;">Chimney Rock reservation (moved from 3/16).</strong> Check with park about using timed-entry ticket on 3/17 &mdash; call <a href="tel:8286259611">(828) 625-9611</a> to confirm.</li>
</ul>

<h3>Lunch (11:45 AM&ndash;12:30 PM)</h3>
<ul>
<li>Quick lunch in <strong>Chimney Rock Village</strong> (restaurants right at the park entrance) or <strong>Lake Lure</strong> (7 min south)</li>
</ul>

<h3>Afternoon &mdash; Pisgah Waterfall Trail (1:45&ndash;4:30 PM)</h3>

<p><strong>The Route:</strong> All four waterfalls are <strong>sequential along US-276 heading north</strong> through Pisgah National Forest &mdash; no backtracking. Drive ~1 hr 15 min from Chimney Rock, then hit them in order:</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Distance</th><th>Difficulty</th><th>Time Needed</th><th>Highlight</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></strong></td><td>Roadside (steps only)</td><td>Easy</td><td>15&ndash;20 min</td><td>60-ft waterfall right off US-276. Walk down ~60 steps to the base. Start here always. FREE.</td></tr>
<tr><td>2</td><td><strong><a href="https://www.alltrails.com/trail/us/north-carolina/moore-cove-falls-trail" target="_blank" rel="noopener noreferrer">Moore Cove Falls</a></strong></td><td>1.2 mi RT</td><td>Easy</td><td>30&ndash;45 min</td><td>Walk <strong>BEHIND</strong> a 50-ft waterfall through lush forest! Kid favorite &mdash; magical experience.</td></tr>
<tr><td>3</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></strong></td><td>Roadside</td><td>Easy</td><td>10&ndash;15 min</td><td>Natural 60-ft rock waterslide. Too cold to slide in March but fun to watch. Quick stop.</td></tr>
<tr><td>4</td><td><strong>Skinny Dip Falls</strong> &#9200;</td><td>1 mi RT</td><td>Moderate</td><td>30&ndash;45 min</td><td>Cascading falls with wading pools in deep forest. <strong>Only if time &amp; energy.</strong> BRP MP 417.</td></tr>
</tbody>
</table>

<p><strong>Recommended combos based on energy:</strong></p>
<ul>
<li><strong>Easy (tired kid):</strong> Looking Glass Falls (roadside) &rarr; Moore Cove (1.2 mi) = 2 waterfalls, minimal effort, home by 3:30</li>
<li><strong>Moderate (good energy):</strong> Looking Glass &rarr; Moore Cove &rarr; Sliding Rock (quick stop) = 3 falls, ~1.5 mi hiking, home by 4:00</li>
<li><strong>Full send (everyone fired up):</strong> All 4 &mdash; Looking Glass &rarr; Moore Cove &rarr; Sliding Rock &rarr; Skinny Dip = 4 falls, ~2.5 mi total hiking, home by 5:00</li>
</ul>

<h3>Full Day Timeline</h3>
<ul>
<li><strong>8:45 AM</strong> &mdash; Depart cabin (~1 hr 10 min drive to Chimney Rock)</li>
<li><strong>10:00&ndash;10:30 AM</strong> &mdash; Arrive at Chimney Rock, park, tickets</li>
<li><strong>10:30 AM</strong> &mdash; Elevator to the summit</li>
<li><strong>10:45 AM</strong> &mdash; Hike Skyline&ndash;Cliff Trail to Exclamation Point (0.4 mi, ~30 min with photos)</li>
<li><strong>11:15 AM</strong> &mdash; Head back down, browse Chimney Rock Village</li>
<li><strong>11:45 AM</strong> &mdash; Lunch in the Village or Lake Lure</li>
<li><strong>12:30 PM</strong> &mdash; Depart for Pisgah waterfalls (~1 hr 15 min via US-64 W &rarr; US-276 N)</li>
<li><strong>1:45 PM</strong> &mdash; <strong>Looking Glass Falls</strong> &mdash; stairs down to base, photos (15&ndash;20 min)</li>
<li><strong>2:10 PM</strong> &mdash; Drive 1 mi north on US-276</li>
<li><strong>2:15 PM</strong> &mdash; <strong>Moore Cove Falls</strong> &mdash; hike 1.2 mi RT through forest, walk behind the falls (30&ndash;45 min)</li>
<li><strong>3:00 PM</strong> &mdash; Drive 3 mi north on US-276</li>
<li><strong>3:05 PM</strong> &mdash; <strong>Sliding Rock</strong> &mdash; quick roadside stop, watch the water (10 min)</li>
<li><strong>3:15 PM</strong> &mdash; <em>Decision point: head home or continue to Skinny Dip Falls?</em></li>
<li><strong>3:35 PM</strong> &mdash; &#9200; <strong>Skinny Dip Falls</strong> (if time) &mdash; 1 mi RT, cascading falls with pools (30&ndash;45 min)</li>
<li><strong>4:15&ndash;4:30 PM</strong> &mdash; Head home via BRP north &rarr; NC-191 (~45 min to cabin)</li>
<li><strong>5:00&ndash;5:15 PM</strong> &mdash; Back at the cabin</li>
</ul>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Tip:</strong> The waterfalls are all along one road (US-276 north) so there&rsquo;s zero backtracking &mdash; just keep driving north and stop at each one. After yesterday&rsquo;s storms, water flow will be spectacular. Moore Cove Falls is the star &mdash; walking behind a waterfall is a core memory for Ethan. Bring a jacket for the mist!
</div>

<p><em>Note: BRP speed limit is 45 mph max; expect 30&ndash;35 mph on curves. Skinny Dip Falls (MP 417) is within the OPEN BRP section (MP 393.6&ndash;420.2) but you cannot continue south past MP 420.</em></p>

<p><strong>Evening &mdash; St. Patrick&rsquo;s Day!</strong></p>
<ul>
<li>Family-friendly St. Patrick&rsquo;s Day dinner (green everything!)</li>
<li>Parents&rsquo; option: Brewery crawl if kid goes to bed at lodging</li>
<li>Look for <strong>Random Acts of Fringe</strong> pop-ups around downtown (free, all-ages)</li>
</ul>

<p><strong>Backup if kid is tired after Chimney Rock:</strong></p>
<ul>
<li><strong>Easy mode:</strong> Just do Looking Glass Falls (roadside, 15 min) &rarr; head home. Still see one waterfall with almost no effort.</li>
<li><strong>Skip waterfalls entirely:</strong> Head back to the cabin for rest, or <strong>Mountain Play Lodge</strong> for indoor play.</li>
</ul>

<p><strong>Scouting note:</strong> The drive from Chimney Rock through Bat Cave and into Pisgah NF gives you a feel for the full range of WNC geography &mdash; from the gorge to the deep forest. Notice how close world-class waterfalls are to Asheville. The US-276 corridor through Pisgah is everyone&rsquo;s backyard playground.</p>

"""

def main():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: {HTML_FILE} not found. Run from the trip-plan repo root.")
        return

    html = read_html()

    day7_start = html.find('<h2 id="day-7">')
    day8_start = html.find('<h2 id="day-8">')

    if day7_start == -1 or day8_start == -1:
        print("ERROR: Could not find Day 7 or Day 8 section headers.")
        return

    html = html[:day7_start] + NEW_DAY7 + html[day8_start:]

    write_html(html)
    print("Done! Day 7 updated with full waterfall route.")
    print("")
    print("Schedule:")
    print("  8:45 AM   - Depart cabin")
    print("  10:00 AM  - Arrive Chimney Rock -> elevator + Exclamation Point")
    print("  11:45 AM  - Lunch in the Village")
    print("  12:30 PM  - Drive to Pisgah (~1h15m)")
    print("  1:45 PM   - Looking Glass Falls (roadside, 15-20 min)")
    print("  2:15 PM   - Moore Cove Falls (1.2 mi RT, walk BEHIND the falls)")
    print("  3:05 PM   - Sliding Rock (quick stop)")
    print("  3:35 PM   - Skinny Dip Falls (if time & energy, 1 mi RT)")
    print("  ~5:00 PM  - Back at cabin")
    print("")
    print("Preview: python -m http.server 8000")
    print("Then open http://localhost:8000 in your browser")
    print("")
    print("When ready: git add index.html && git commit -m \"Update Day 7: elevator + full waterfall route\" && git push")

if __name__ == "__main__":
    main()

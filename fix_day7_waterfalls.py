#!/usr/bin/env python3
"""
Fix: Update Day 7 - Chimney Rock + Lake Lure + Brooks Tavern dinner.
Waterfalls moved to Day 8 (Looking Glass Falls with DuPont/Brevard).

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
NEW_DAY7 = """<h2 id="day-7">Day 7 &mdash; Tuesday, March 17th: Chimney Rock + Lake Lure + Hendersonville</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#9968;&#65039; Elevator to the Summit &bull; Lake Lure afternoon &bull; Brooks Tavern dinner</p>

<p><strong>&#128205; Route &amp; Distances:</strong> <a href="https://www.google.com/maps/dir/35.612841,-82.665031/Chimney+Rock+State+Park,+NC/Lake+Lure,+NC/142+3rd+Ave+W,+Hendersonville,+NC/35.612841,-82.665031" target="_blank" rel="noopener noreferrer">Day 7 Google Map</a></p>

<table>
<thead><tr><th>#</th><th>Segment</th><th>Miles</th><th>Drive Time</th><th>Route</th></tr></thead>
<tbody>
<tr><td>1</td><td>Candler rental &rarr; <a href="https://www.chimneyrockpark.com" target="_blank" rel="noopener noreferrer">Chimney Rock State Park</a></td><td>~45 mi</td><td>~1 hr 10 min</td><td>I-40 E &rarr; I-26 E &rarr; <strong>Exit 49A</strong> &rarr; US-64 E (18 mi) &rarr; NC-9 S through Lake Lure</td></tr>
<tr><td>2</td><td>Chimney Rock &rarr; Lake Lure</td><td>~3 mi</td><td>~7 min</td><td>NC-9 S / Main St south along the river</td></tr>
<tr><td>3</td><td>Lake Lure &rarr; <a href="https://brookstavern.com/" target="_blank" rel="noopener noreferrer">Brooks Tavern</a> (Hendersonville)</td><td>~28 mi</td><td>~40 min</td><td>US-64 W &rarr; I-26 S &rarr; Exit 49B &rarr; 3rd Ave W</td></tr>
<tr><td>4</td><td>Brooks Tavern &rarr; Candler rental</td><td>~26 mi</td><td>~30 min</td><td>I-26 W &rarr; US-74 W</td></tr>
<tr><td></td><td><strong>Day 7 Total</strong></td><td><strong>~102 mi</strong></td><td><strong>~2 hr 27 min driving</strong></td><td><em>Relaxed day &mdash; half the driving of the original plan!</em></td></tr>
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

<p><strong>Post-storm trail conditions:</strong> After yesterday&rsquo;s storms and snow, expect wet trails with possible icy patches at higher elevations. Wear waterproof boots and layers. The fresh snow on peaks = spectacular views!</p>

<h3>Morning &mdash; Chimney Rock State Park (10:00&ndash;11:45 AM)</h3>

<p><strong>The Plan:</strong> Elevator to the top, short hike to Exclamation Point for panoramic views.</p>

<ul>
<li><strong>Elevator to the top</strong> &mdash; 26-story elevator inside the mountain takes you straight to the Chimney summit. No hiking needed to reach the top!</li>
<li><strong>Skyline&ndash;Cliff Trail to Exclamation Point</strong> &mdash; 0.4 mi, easy. Short walk from the Chimney to the highest publicly accessible point. Best panoramic views of Lake Lure &amp; Hickory Nut Gorge. <strong>This is the main hike.</strong></li>
<li><em>Skip Hickory Nut Falls Trail (1.4 mi) &mdash; save legs for tomorrow&rsquo;s waterfall hikes at DuPont + Looking Glass Falls.</em></li>
<li><strong style="color:#15803d;">Chimney Rock reservation (moved from 3/16).</strong> Check with park about using timed-entry ticket on 3/17 &mdash; call <a href="tel:8286259611">(828) 625-9611</a> to confirm.</li>
</ul>

<h3>Lunch &mdash; RiverWatch Bar &amp; Grill (11:45 AM&ndash;12:30 PM)</h3>
<p><strong><a href="https://www.riverwatchbarandgrill.com/" target="_blank" rel="noopener noreferrer">RiverWatch Bar &amp; Grill</a></strong> &mdash; 379 Main St, Chimney Rock, NC &mdash; right at the park entrance on the Rocky Broad River.</p>
<ul>
<li>Burgers, wings, tacos, wraps &mdash; solid casual food with <strong>outdoor deck overlooking the river</strong></li>
<li>Kid-friendly, quick service. Reopened post-Helene and back in action.</li>
</ul>

<h3>Afternoon &mdash; Lake Lure (12:45&ndash;3:00 PM)</h3>

<p>After lunch, head 7 min south to <strong>Lake Lure</strong> for a relaxed afternoon by the water. Options:</p>

<ul>
<li><strong>Lake Lure Beach &amp; Water Park</strong> &mdash; sandy beach area, splash zone (weather permitting), great for Ethan to run around</li>
<li><strong>Lake Lure Flowering Bridge</strong> &mdash; FREE, beautiful garden walk on a historic bridge over the Rocky Broad River. Easy and scenic.</li>
<li><strong>Walk the town</strong> &mdash; small shops, ice cream, lake views. <em>Dirty Dancing</em> was filmed here &mdash; there&rsquo;s a monument!</li>
<li><strong>Boat tour</strong> (if available) &mdash; Lake Lure Tours offers scenic cruises with mountain views. Check availability: <a href="tel:8286251373">(828) 625-1373</a></li>
</ul>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Tip:</strong> Lake Lure is one of the most scenic lakes in the Southeast &mdash; mountains rising straight out of the water. After yesterday&rsquo;s snow, the peaks around the lake should be dusted white. Perfect photo ops!
</div>

<h3>Full Day Timeline</h3>
<ul>
<li><strong>8:45 AM</strong> &mdash; Depart cabin (~1 hr 10 min drive to Chimney Rock)</li>
<li><strong>10:00&ndash;10:30 AM</strong> &mdash; Arrive at Chimney Rock, park, tickets</li>
<li><strong>10:30 AM</strong> &mdash; Elevator to the summit</li>
<li><strong>10:45 AM</strong> &mdash; Hike Skyline&ndash;Cliff Trail to Exclamation Point (0.4 mi, ~30 min with photos)</li>
<li><strong>11:15 AM</strong> &mdash; Head back down to Chimney Rock Village</li>
<li><strong>11:45 AM</strong> &mdash; Lunch at <strong>RiverWatch Bar &amp; Grill</strong> (379 Main St &mdash; river deck, burgers &amp; tacos)</li>
<li><strong>12:30 PM</strong> &mdash; Browse Chimney Rock Village shops</li>
<li><strong>12:45 PM</strong> &mdash; Drive to Lake Lure (~7 min)</li>
<li><strong>1:00&ndash;3:00 PM</strong> &mdash; Lake Lure &mdash; beach, Flowering Bridge, shops, or boat tour</li>
<li><strong>3:00 PM</strong> &mdash; Depart Lake Lure for Hendersonville (~40 min)</li>
<li><strong>3:45 PM</strong> &mdash; Arrive Hendersonville &mdash; walk Main Street, shops, let Ethan stretch his legs</li>
<li><strong>5:00&ndash;5:30 PM</strong> &mdash; <strong><a href="https://brookstavern.com/" target="_blank" rel="noopener noreferrer">Brooks Tavern</a></strong> (142 3rd Ave W) &mdash; smash burgers, hand-cut fries, craft beer. Kid-friendly. No reservations, arrive early to avoid a wait. Open until 8 PM.</li>
<li><strong>6:30&ndash;7:00 PM</strong> &mdash; Head to cabin (~30 min via I-26 W)</li>
<li><strong>7:00&ndash;7:30 PM</strong> &mdash; Back at the cabin</li>
</ul>

<h3>Dinner &mdash; Brooks Tavern, Hendersonville (5:00&ndash;6:30 PM)</h3>

<p><strong><a href="https://brookstavern.com/" target="_blank" rel="noopener noreferrer">Brooks Tavern</a></strong> &mdash; 142 3rd Ave W, Hendersonville, NC 28792 &mdash; <a href="tel:8285959994">(828) 595-9994</a></p>
<ul>
<li>Known for the <strong>best smash burgers in town</strong> &mdash; 100% Certified Angus Beef, hand-cut fries, 20 oz craft beer pours</li>
<li>Kid-friendly &mdash; casual pub atmosphere, one block off Main Street</li>
<li>Open until 8 PM (Tue) &mdash; <strong>no reservations</strong>, arrive by 5:00 to beat the rush</li>
<li>St. Patrick&rsquo;s Day bonus: ask about any holiday specials!</li>
</ul>

<p><strong>While you wait / after dinner:</strong> Walk a block to <strong>Main Street Hendersonville</strong> &mdash; shops, ice cream, and a nice evening stroll. You were here on Day 4 so you know the lay of the land.</p>

<p><strong>&#127808; St. Patrick&rsquo;s Day note:</strong> It&rsquo;s St. Paddy&rsquo;s! Hendersonville may have some festive energy on Main Street. Brooks Tavern will likely have specials. Enjoy!</p>

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
    print("Done! Day 7 updated: Chimney Rock + Lake Lure + Brooks Tavern.")
    print("(Waterfalls moved to Day 8)")
    print("")
    print("Schedule:")
    print("  8:45 AM   - Depart cabin")
    print("  10:00 AM  - Arrive Chimney Rock -> elevator + Exclamation Point")
    print("  11:45 AM  - Lunch at RiverWatch Bar & Grill")
    print("  12:45 PM  - Drive to Lake Lure (7 min)")
    print("  1:00 PM   - Lake Lure (beach, Flowering Bridge, shops)")
    print("  3:00 PM   - Drive to Hendersonville (~40 min)")
    print("  3:45 PM   - Walk Main Street Hendersonville")
    print("  5:00 PM   - Dinner at Brooks Tavern (St. Patrick's Day!)")
    print("  6:30 PM   - Head to cabin (~30 min)")
    print("  7:00 PM   - Back at cabin")
    print("")
    print("Next: Run fix_day8_add_lookinglass.py to add Looking Glass Falls to Day 8")
    print("")
    print("Preview: python -m http.server 8000")
    print("Then open http://localhost:8000 in your browser")

if __name__ == "__main__":
    main()

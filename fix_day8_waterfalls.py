#!/usr/bin/env python3
"""
Fix: Update Day 8 with full waterfall trail + BRP scenic drive + downtown Brevard.

Route: Cabin -> Pisgah Falls (US-276) -> BRP scenic drive -> DuPont -> Brevard -> Cabin
Waterfalls: Looking Glass, Moore Cove, Sliding Rock, Hooker, Triple, High, Bridal Veil
Plus: BRP scenic drive (MP 411.8-417), O.P. Taylor's toy store, downtown Brevard

Run from the trip-plan repo root: python fix_day8_waterfalls.py
"""
import os

HTML_FILE = "index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

NEW_DAY8 = """<h2 id="day-8">Day 8 &mdash; Wednesday, March 18th: Pisgah Waterfall Trail + BRP + DuPont + Brevard</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#127786;&#65039; Up to 7 waterfalls &bull; Blue Ridge Parkway scenic drive &bull; O.P. Taylor&rsquo;s Toy Store &bull; Downtown Brevard</p>

<p><strong>&#128205; Route &amp; Distances:</strong> <a href="https://www.google.com/maps/dir/35.612841,-82.665031/Looking+Glass+Falls,+Pisgah+Forest,+NC/Moore+Cove+Falls+Trail,+NC/Sliding+Rock,+Pisgah+Forest,+NC/35.3480,-82.6980/Hooker+Falls,+DuPont+State+Recreational+Forest,+NC/O.P.+Taylor's,+16+S+Broad+St,+Brevard,+NC/35.612841,-82.665031" target="_blank" rel="noopener noreferrer">Day 8 Google Map</a> (includes BRP scenic section + O.P. Taylor&rsquo;s)</p>

<table>
<thead><tr><th>#</th><th>Segment</th><th>Miles</th><th>Drive Time</th><th>Route</th></tr></thead>
<tbody>
<tr><td>1</td><td>Candler rental &rarr; <a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></td><td>~40 mi</td><td>~45 min</td><td>I-26 E &rarr; NC-280 E &rarr; US-276 N into Pisgah NF</td></tr>
<tr><td>2</td><td>Looking Glass Falls &rarr; Moore Cove Falls &rarr; <a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></td><td>~4 mi</td><td>~10 min</td><td>Continue north on US-276 &mdash; all sequential, no backtracking</td></tr>
<tr><td>3</td><td>Sliding Rock &rarr; <strong>Blue Ridge Parkway</strong> (MP 411.8&ndash;417)</td><td>~12 mi</td><td>~20 min</td><td>US-276 N to BRP junction at MP 411.8, drive south to MP 417</td></tr>
<tr><td>4</td><td>BRP (MP 417) &rarr; <a href="https://www.dupontstaterecreationalforest.com/" target="_blank" rel="noopener noreferrer">DuPont State Forest</a> (Hooker Falls lot)</td><td>~25 mi</td><td>~35 min</td><td>Return BRP to US-276 S &rarr; US-64 E &rarr; Staton Rd to Hooker Falls parking</td></tr>
<tr><td>5</td><td>DuPont &rarr; <a href="https://www.optaylors.com/" target="_blank" rel="noopener noreferrer">O.P. Taylor&rsquo;s</a> / Downtown Brevard</td><td>~10 mi</td><td>~15 min</td><td>Staton Rd &rarr; US-64 W &rarr; S Broad St</td></tr>
<tr><td>6</td><td>Brevard &rarr; Candler rental</td><td>~40 mi</td><td>~45 min</td><td>US-276 N &rarr; NC-280 W &rarr; I-26 W</td></tr>
<tr><td></td><td><strong>Day 8 Total</strong></td><td><strong>~131 mi</strong></td><td><strong>~2 hr 50 min driving</strong></td><td><em>Waterfalls are sequential on US-276 &mdash; BRP + DuPont + Brevard all on the loop!</em></td></tr>
</tbody>
</table>

<div class="alert" style="background:#e8f5e9;border:2px solid #4caf50;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong>&#9989; BRP STATUS (confirmed):</strong> The NPS completed the landslide repair at MP 401.5 (Ferrin Knob Tunnel), restoring <strong>38 continuous miles from MP 382 to MP 420</strong>. Our scenic section (MP 411.8&ndash;417) is fully within this open corridor. You <strong>cannot continue south past MP 420</strong> (still closed from Helene damage).
</div>

<div class="alert" style="background:#fef3cd;border:2px solid #ffc107;border-radius:10px;padding:12px 16px;margin:10px 0;font-size:0.9em;">
<strong>&#9888;&#65039; Morning-of check:</strong> The BRP can close temporarily for snow or ice. After Monday&rsquo;s storms, check conditions before driving up: <a href="https://www.nps.gov/blri/planyourvisit/roadclosures.htm" target="_blank" rel="noopener noreferrer">NPS Road Status</a> | <a href="https://www.blueridgeparkway.org/road-conditions/" target="_blank" rel="noopener noreferrer">BRP Conditions</a>
</div>

<h3>Part 1 &mdash; Pisgah National Forest Waterfalls (US-276)</h3>

<p>All three waterfalls are <strong>sequential along US-276 heading north</strong> through Pisgah National Forest &mdash; zero backtracking. After Monday&rsquo;s storms, water flow will be roaring!</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Distance</th><th>Difficulty</th><th>Time Needed</th><th>Highlight</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></strong></td><td>Roadside (steps only)</td><td>Easy</td><td>15&ndash;20 min</td><td>60-ft waterfall right off US-276. Walk down ~60 steps to the base. Start here always. FREE.</td></tr>
<tr><td>2</td><td><strong><a href="https://www.alltrails.com/trail/us/north-carolina/moore-cove-falls-trail" target="_blank" rel="noopener noreferrer">Moore Cove Falls</a></strong></td><td>1.2 mi RT</td><td>Easy</td><td>30&ndash;45 min</td><td>Walk <strong>BEHIND</strong> a 50-ft waterfall through lush forest! Kid favorite &mdash; magical experience.</td></tr>
<tr><td>3</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></strong></td><td>Roadside</td><td>Easy</td><td>10&ndash;15 min</td><td>Natural 60-ft rock waterslide, 11,000 gal/min. Too cold to slide in March but amazing to watch.</td></tr>
</tbody>
</table>

<h3>Part 2 &mdash; Blue Ridge Parkway Scenic Drive</h3>

<p>After Sliding Rock, US-276 continues north and <strong>intersects the Blue Ridge Parkway at Milepost 411.8</strong>. Turn south for a gorgeous mountain ridge drive with stunning views.</p>

<ul>
<li><strong>Scenic Drive: MP 411.8 south to MP 417</strong> (~5 mi) &mdash; Drive along the ridge at 35&ndash;45 mph with mountain panoramas on both sides. Allow 15&ndash;20 min with a pullover or two for photos. Snow-dusted peaks after Monday&rsquo;s storm!</li>
<li><strong>Looking Glass Rock Overlook (MP 417)</strong> &mdash; Iconic view of the massive granite dome. One of the most photographed spots on the BRP. Quick stop.</li>
<li><strong>Skinny Dip Falls (BRP MP 417) &mdash; Optional Bonus Waterfall</strong> &mdash; Cascading falls with wading pools in deep forest. 1 mi round trip, moderate. 30&ndash;45 min if energy allows. Trailhead at the Looking Glass Rock Overlook parking area.</li>
</ul>

<p><em>BRP speed limit is 45 mph max; expect 30&ndash;35 mph on curves. After MP 417, return north on BRP to US-276 and head south toward DuPont.</em></p>

<h3>Part 3 &mdash; DuPont State Forest Waterfalls</h3>

<p>DuPont has three major waterfalls on the Little River, all accessible from the <strong>Hooker Falls parking area</strong>. Moderate hiking on well-maintained trails.</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Distance</th><th>Difficulty</th><th>Time Needed</th><th>Highlight</th></tr></thead>
<tbody>
<tr><td>4</td><td><strong><a href="https://www.dupontstaterecreationalforest.com/waterfalls/hooker-falls" target="_blank" rel="noopener noreferrer">Hooker Falls</a></strong></td><td>0.5 mi RT</td><td>Easy</td><td>15 min</td><td>Wide, powerful 12-ft curtain waterfall. Shortest walk from the parking lot. Great warm-up.</td></tr>
<tr><td>5</td><td><strong>Triple Falls</strong></td><td>1.4 mi from Hooker</td><td>Moderate</td><td>45 min</td><td>Three cascading drops, 120 ft total. Featured in <em>The Hunger Games</em> &amp; <em>The Last of the Mohicans</em>. THE must-see.</td></tr>
<tr><td>6</td><td><strong>High Falls</strong></td><td>0.3 mi past Triple</td><td>Moderate</td><td>20 min</td><td>150-ft dramatic plunge over a cliff &mdash; tallest in DuPont. Viewing platform with railing.</td></tr>
<tr><td>7</td><td><strong>Bridal Veil Falls</strong> &#9200;</td><td>0.6 mi past High</td><td>Moderate</td><td>30 min</td><td>120-ft wispy falls. <strong>Only if time &amp; energy.</strong> Beautiful but not essential.</td></tr>
</tbody>
</table>

<p><em>The trail from Hooker Falls &rarr; Triple Falls &rarr; High Falls is a <strong>3.2 mi out-and-back</strong> along the Little River. Well-maintained, moderate difficulty. Triple Falls alone is worth the trip.</em></p>

<h3>Part 4 &mdash; Downtown Brevard</h3>

<p>After DuPont, head 15 min to <strong>downtown Brevard</strong> &mdash; a charming mountain town known as the &ldquo;Land of Waterfalls.&rdquo;</p>

<ul>
<li><strong><a href="https://www.optaylors.com/" target="_blank" rel="noopener noreferrer">O.P. Taylor&rsquo;s Toy Store</a></strong> &mdash; 16 S Broad St &mdash; Legendary independent toy store, one of the best in the Southeast! Floor-to-ceiling toys, games, puzzles, stuffed animals. Ethan will go wild. <strong>A Brevard must-stop.</strong></li>
<li><strong>Downtown Main Street &amp; Broad Street</strong> &mdash; Walkable downtown with local shops, galleries, bookstores, cafes, ice cream, and candy stores.</li>
<li><strong>White Squirrels!</strong> &mdash; Brevard is famous for its colony of white squirrels. Keep an eye out around downtown &mdash; they&rsquo;re real and they&rsquo;re everywhere.</li>
<li><strong>Lunch options:</strong> The Square Root (creative sandwiches &amp; salads), Rocky&rsquo;s Grill (burgers &amp; comfort food), Mayberry&rsquo;s (classic diner), or grab pizza and eat by the courthouse lawn.</li>
</ul>

<h3>Full Day Timeline</h3>
<ul>
<li><strong>8:30 AM</strong> &mdash; Depart cabin (~45 min drive to Looking Glass Falls via I-26 E &rarr; NC-280 &rarr; US-276 N)</li>
<li><strong>9:15 AM</strong> &mdash; <strong>Looking Glass Falls</strong> &mdash; roadside stop, stairs to base, photos (15&ndash;20 min)</li>
<li><strong>9:40 AM</strong> &mdash; <strong>Moore Cove Falls</strong> &mdash; 1.2 mi RT hike, walk behind the falls (30&ndash;45 min)</li>
<li><strong>10:30 AM</strong> &mdash; <strong>Sliding Rock</strong> &mdash; quick roadside stop, watch 11,000 gal/min flow (10&ndash;15 min)</li>
<li><strong>10:50 AM</strong> &mdash; <strong>Blue Ridge Parkway scenic drive</strong> &mdash; US-276 N to BRP at MP 411.8, drive south to MP 417. Mountain ridge panoramas, snow-dusted peaks (20&ndash;30 min)</li>
<li><strong>11:15 AM</strong> &mdash; <strong>Looking Glass Rock Overlook</strong> (MP 417) &mdash; iconic granite dome view. Optional: <strong>Skinny Dip Falls</strong> (1 mi RT, 30&ndash;45 min)</li>
<li><strong>11:30 AM</strong> &mdash; Return to US-276, drive south to DuPont (~35 min via US-276 S &rarr; US-64 E)</li>
<li><strong>12:00 PM</strong> &mdash; Arrive at DuPont &mdash; Hooker Falls parking area</li>
<li><strong>12:10 PM</strong> &mdash; <strong>Hooker Falls</strong> &mdash; quick 0.5 mi walk (15 min)</li>
<li><strong>12:30 PM</strong> &mdash; <strong>Triple Falls</strong> &mdash; 1.4 mi hike from Hooker Falls, multiple viewing platforms (45 min)</li>
<li><strong>1:15 PM</strong> &mdash; <strong>High Falls</strong> &mdash; 0.3 mi past Triple Falls, tallest in DuPont (20 min)</li>
<li><strong>1:45 PM</strong> &mdash; Hike back to parking (~1.7 mi, 35&ndash;40 min)</li>
<li><strong>2:30 PM</strong> &mdash; Drive to downtown Brevard (~15 min)</li>
<li><strong>2:45 PM</strong> &mdash; <strong>Lunch in downtown Brevard</strong> &mdash; restaurants, cafes, and the &ldquo;Land of Waterfalls&rdquo; vibe</li>
<li><strong>3:15 PM</strong> &mdash; <strong>O.P. Taylor&rsquo;s Toy Store</strong> (16 S Broad St) &mdash; legendary toy store, Ethan will love this!</li>
<li><strong>3:45 PM</strong> &mdash; Walk downtown &mdash; browse shops, grab ice cream, look for the <strong>white squirrels</strong></li>
<li><strong>4:15 PM</strong> &mdash; Head back to cabin (~45 min via US-276 N &rarr; NC-280 &rarr; I-26 W)</li>
<li><strong>5:00 PM</strong> &mdash; Back at the cabin &mdash; evening to relax</li>
</ul>

<p><strong>Recommended combos based on energy:</strong></p>
<ul>
<li><strong>Easy (tired kid):</strong> Looking Glass Falls (roadside) &rarr; Sliding Rock (roadside) &rarr; BRP scenic drive &rarr; Hooker Falls (0.5 mi) &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; home by 2 PM</li>
<li><strong>Moderate (good energy):</strong> Looking Glass &rarr; Moore Cove &rarr; Sliding Rock &rarr; BRP drive &rarr; Hooker Falls &rarr; Triple Falls &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; home by 4 PM</li>
<li><strong>Full send (everyone fired up):</strong> All Pisgah falls &rarr; BRP + Skinny Dip Falls &rarr; All DuPont falls &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; home by 5 PM</li>
</ul>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Scouting note:</strong> The US-276 corridor through Pisgah National Forest is everyone&rsquo;s backyard playground. Notice how close world-class waterfalls and the Blue Ridge Parkway are to Asheville. DuPont&rsquo;s Triple Falls from <em>The Hunger Games</em> and Brevard&rsquo;s walkable downtown with O.P. Taylor&rsquo;s show exactly the kind of family-friendly lifestyle this area offers.
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
        print("ERROR: Could not find Day 8 section header (<h2 id=\"day-8\">).")
        return

    if day9_start == -1:
        print("ERROR: Could not find Day 9 section header (<h2 id=\"day-9\">).")
        return

    html = html[:day8_start] + NEW_DAY8 + html[day9_start:]

    write_html(html)
    print("Done! Day 8 updated with full waterfall trail + BRP + DuPont + Brevard.")
    print("")
    print("Schedule:")
    print("  8:30 AM   - Depart cabin")
    print("  9:15 AM   - Looking Glass Falls (60-ft, roadside)")
    print("  9:40 AM   - Moore Cove Falls (walk BEHIND a waterfall!)")
    print("  10:30 AM  - Sliding Rock (11,000 gal/min waterslide)")
    print("  10:50 AM  - Blue Ridge Parkway scenic drive (MP 411.8 -> 417)")
    print("  11:15 AM  - Looking Glass Rock Overlook + optional Skinny Dip Falls")
    print("  12:00 PM  - DuPont State Forest (Hooker, Triple, High Falls)")
    print("  2:30 PM   - Drive to downtown Brevard")
    print("  2:45 PM   - Lunch in Brevard")
    print("  3:15 PM   - O.P. Taylor's Toy Store!")
    print("  3:45 PM   - Walk downtown, white squirrels, ice cream")
    print("  4:15 PM   - Head to cabin")
    print("  5:00 PM   - Back at cabin")
    print("")
    print("BRP Status: OPEN (MP 382-420, confirmed after Helene repair)")
    print("Check morning-of: https://www.nps.gov/blri/planyourvisit/roadclosures.htm")
    print("")
    print("Preview: python -m http.server 8000")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Fix: Update Day 8 with full waterfall trail + BRP scenic drive + downtown Brevard.

Route: Cabin -> Pisgah Falls (US-276) -> BRP scenic drive -> DuPont -> Brevard -> Cabin
Waterfalls: Looking Glass, Moore Cove, Sliding Rock, Hooker, Triple, High, Bridal Veil
Plus: BRP scenic drive (MP 411.8-417), O.P. Taylor's toy store, downtown Brevard

Run from the trip-plan repo root: python fix_day8_waterfalls.py
"""
import os

HTML_FILE = "trip-plan/index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

NEW_DAY8 = """<h2 id="day-8">Day 8 &mdash; Wednesday, March 18th: Pisgah Waterfall Trail + BRP + DuPont + Brevard + The Marquee</h2>
<p style="margin:-8px 0 12px 0;font-size:0.95em;color:#666;font-style:italic;font-family:Fraunces,serif;">&#127786;&#65039; Up to 7 waterfalls &bull; Blue Ridge Parkway scenic drive &bull; O.P. Taylor&rsquo;s Toy Store &bull; Downtown Brevard &bull; The Marquee (River Arts District) &bull; Late dinner in Asheville</p>

<p><strong>&#128205; Route &amp; Distances:</strong> <a href="https://www.google.com/maps/dir/35.612841,-82.665031/Looking+Glass+Falls,+Pisgah+Forest,+NC/Moore+Cove+Falls+Trail,+NC/Sliding+Rock,+Pisgah+Forest,+NC/35.3480,-82.6980/Hooker+Falls,+DuPont+State+Recreational+Forest,+NC/O.P.+Taylor's,+16+S+Broad+St,+Brevard,+NC/35.612841,-82.665031" target="_blank" rel="noopener noreferrer">Day 8 Google Map</a> (includes BRP scenic section + O.P. Taylor&rsquo;s)</p>

<table>
<thead><tr><th>#</th><th>Segment</th><th>Miles</th><th>Drive Time</th><th>Route</th></tr></thead>
<tbody>
<tr><td>1</td><td>Candler rental &rarr; <a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></td><td>~40 mi</td><td>~45 min</td><td>I-26 E &rarr; NC-280 E &rarr; US-276 N into Pisgah NF</td></tr>
<tr><td>2</td><td>Looking Glass Falls &rarr; Moore Cove Falls &rarr; <a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></td><td>~4 mi</td><td>~10 min</td><td>Continue north on US-276 &mdash; all sequential, no backtracking</td></tr>
<tr><td>3</td><td>Sliding Rock &rarr; <strong>Blue Ridge Parkway</strong> (MP 411.8&ndash;417)</td><td>~12 mi</td><td>~20 min</td><td>US-276 N to BRP junction at MP 411.8, drive south to MP 417</td></tr>
<tr><td>4</td><td>BRP (MP 417) &rarr; <a href="https://www.dupontstaterecreationalforest.com/" target="_blank" rel="noopener noreferrer">DuPont</a> &mdash; Hooker Falls lot (Staton Rd)</td><td>~25 mi</td><td>~35 min</td><td>Return BRP to US-276 S &rarr; US-64 E &rarr; Staton Rd to Hooker Falls parking</td></tr>
<tr><td>5</td><td>Hooker Falls lot &rarr; High Falls lot (Cascade Lake Rd)</td><td>~2 mi</td><td>~5 min</td><td>Right on Staton Rd &rarr; right on Cascade Lake Rd &mdash; <strong>closer parking for Triple + High Falls</strong></td></tr>
<tr><td>6</td><td>High Falls lot &rarr; <a href="https://www.optaylors.com/" target="_blank" rel="noopener noreferrer">O.P. Taylor&rsquo;s</a> / Downtown Brevard</td><td>~10 mi</td><td>~15 min</td><td>Cascade Lake Rd &rarr; US-64 W &rarr; S Broad St</td></tr>
<tr><td>7</td><td>Brevard &rarr; <a href="https://marqueeasheville.com/" target="_blank" rel="noopener noreferrer">The Marquee</a> (36 Foundry St, Asheville)</td><td>~40 mi</td><td>~40 min</td><td>US-276 N &rarr; NC-280 W &rarr; I-26 W &rarr; Exit 31 (Amboy Rd) to River Arts District</td></tr>
<tr><td>8</td><td>Late dinner in Asheville &rarr; Candler rental</td><td>~10 mi</td><td>~15 min</td><td>Dozens of restaurants within minutes of the River Arts District &rarr; I-40 W to cabin</td></tr>
<tr><td></td><td><strong>Day 8 Total</strong></td><td><strong>~143 mi</strong></td><td><strong>~3 hr 25 min driving</strong></td><td><em>Waterfalls + BRP + toy store + The Marquee + Asheville dinner &mdash; full day!</em></td></tr>
</tbody>
</table>

<div class="alert" style="background:#e8f5e9;border:2px solid #4caf50;border-radius:10px;padding:16px 20px;margin:12px 0;font-size:0.95em;">
<strong>&#9989; BRP STATUS (confirmed):</strong> The NPS completed the landslide repair at MP 401.5 (Ferrin Knob Tunnel), restoring <strong>38 continuous miles from MP 382 to MP 420</strong>. Our scenic section (MP 411.8&ndash;417) is fully within this open corridor. You <strong>cannot continue south past MP 420</strong> (still closed from Helene damage).
</div>

<div class="alert" style="background:#fef3cd;border:2px solid #ffc107;border-radius:10px;padding:12px 16px;margin:10px 0;font-size:0.9em;">
<strong>&#9888;&#65039; Morning-of check:</strong> The BRP can close temporarily for snow or ice. After Monday&rsquo;s storms, check conditions before driving up: <a href="https://www.nps.gov/blri/planyourvisit/roadclosures.htm" target="_blank" rel="noopener noreferrer">NPS Road Status</a> | <a href="https://www.blueridgeparkway.org/road-conditions/" target="_blank" rel="noopener noreferrer">BRP Conditions</a>
</div>

<h3>Part 1 &mdash; Pisgah National Forest Waterfalls (US-276)</h3>

<p>All three waterfalls are <strong>sequential along US-276 heading north</strong> through Pisgah National Forest &mdash; zero backtracking. Each has its own parking right on US-276. After Monday&rsquo;s storms, water flow will be roaring!</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Walk from Car</th><th>Difficulty</th><th>Time Needed</th><th>Parking &amp; Details</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48624" target="_blank" rel="noopener noreferrer">Looking Glass Falls</a></strong></td><td>~60 steps down</td><td>Easy</td><td>15&ndash;20 min</td><td>&#127359;&#65039; <strong>Pull-off lot right on US-276</strong> (right side heading north). Paved. 60-ft waterfall visible from the road! Walk down stone steps to the base. FREE.</td></tr>
<tr><td>2</td><td><strong><a href="https://www.alltrails.com/trail/us/north-carolina/moore-cove-falls-trail" target="_blank" rel="noopener noreferrer">Moore Cove Falls</a></strong></td><td>1.2 mi RT (flat)</td><td>Easy</td><td>30&ndash;45 min</td><td>&#127359;&#65039; <strong>Gravel lot on US-276</strong>, 0.7 mi past Looking Glass Falls on the right. Trail is flat, mostly creekside, well-maintained. Walk <strong>BEHIND</strong> a 50-ft waterfall! Kid favorite.</td></tr>
<tr><td>3</td><td><strong><a href="https://www.fs.usda.gov/recarea/nfsnc/recarea/?recid=48965" target="_blank" rel="noopener noreferrer">Sliding Rock</a></strong></td><td>Steps to platform</td><td>Easy</td><td>10&ndash;15 min</td><td>&#127359;&#65039; <strong>Paved parking lot at Sliding Rock</strong>, 2.5 mi past Moore Cove on US-276. Walk down steps to the observation platform. Natural 60-ft rock waterslide, 11,000 gal/min. Too cold in March but amazing to watch.</td></tr>
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

<h3>Part 3 &mdash; DuPont State Forest Waterfalls (2 parking lots = shorter hikes!)</h3>

<p><strong>Strategy:</strong> DuPont has multiple access points. Instead of one long out-and-back, we use <strong>two parking lots</strong> to cut total hiking nearly in half:</p>
<ol>
<li><strong>Stop A &mdash; Hooker Falls Access</strong> (Staton Rd) &rarr; quick 0.4 mi RT to Hooker Falls</li>
<li>Drive 5 min to <strong>Stop B &mdash; High Falls Access</strong> (Cascade Lake Rd) &rarr; short 1.6 mi RT loop to Triple Falls + High Falls</li>
</ol>
<p><em>Total DuPont hiking: ~2.0 mi (vs. 3.9 mi if you parked only at Hooker Falls).</em></p>

<h4>Stop A &mdash; Hooker Falls Access Parking (Staton Rd)</h4>
<p>&#127359;&#65039; <strong>Hooker Falls parking lot</strong> &mdash; <a href="https://www.google.com/maps/place/35.1938,-82.6175" target="_blank" rel="noopener noreferrer">GPS: 35.1938, -82.6175</a> &mdash; Turn onto Staton Rd from US-64, follow signs. Paved lot with restrooms.</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Walk from Car</th><th>Difficulty</th><th>Time Needed</th><th>Details</th></tr></thead>
<tbody>
<tr><td>4</td><td><strong><a href="https://www.dupontstaterecreationalforest.com/waterfalls/hooker-falls" target="_blank" rel="noopener noreferrer">Hooker Falls</a></strong></td><td>0.4 mi RT</td><td>Easy &mdash; flat, wide gravel path</td><td>15 min</td><td>Wide, powerful 12-ft curtain waterfall. Shortest walk of any DuPont falls. Great warm-up.</td></tr>
</tbody>
</table>

<h4>Stop B &mdash; High Falls Access Parking (Cascade Lake Rd) &mdash; 5 min drive from Stop A</h4>
<p>&#127359;&#65039; <strong>High Falls trailhead parking</strong> &mdash; <a href="https://www.google.com/maps/place/35.1830,-82.6280" target="_blank" rel="noopener noreferrer">GPS: 35.1830, -82.6280</a> &mdash; From Hooker Falls lot, turn right on Staton Rd, right on Cascade Lake Rd, lot is ~1.5 mi on the left. Gravel lot.</p>

<table>
<thead><tr><th>#</th><th>Waterfall</th><th>Walk from Car</th><th>Difficulty</th><th>Time Needed</th><th>Details</th></tr></thead>
<tbody>
<tr><td>5</td><td><strong>Triple Falls</strong></td><td>~0.5 mi one way</td><td>Easy-moderate &mdash; wide trail, gentle grade</td><td>30&ndash;40 min</td><td>Three cascading drops, 120 ft total. Featured in <em>The Hunger Games</em> &amp; <em>The Last of the Mohicans</em>. THE must-see. Multiple viewing platforms.</td></tr>
<tr><td>6</td><td><strong>High Falls</strong></td><td>~0.3 mi past Triple</td><td>Easy-moderate &mdash; continue on same trail</td><td>20 min</td><td>150-ft dramatic plunge over a cliff &mdash; tallest in DuPont. Viewing platform with railing. Just 0.3 mi past Triple Falls.</td></tr>
<tr><td>7</td><td><strong>Bridal Veil Falls</strong> &#9200;</td><td>~0.3 mi past High</td><td>Moderate</td><td>20 min</td><td>120-ft wispy falls. <strong>Only if time &amp; energy.</strong> Beautiful but adds 0.6 mi RT.</td></tr>
</tbody>
</table>

<p><em>From the High Falls Access lot, it&rsquo;s a <strong>~1.6 mi out-and-back</strong> to see both Triple Falls and High Falls. Much easier than hiking from Hooker Falls. Trail is wide, mostly flat, well-maintained.</em></p>

<h3>Part 4 &mdash; Downtown Brevard</h3>

<p>After DuPont, head 15 min to <strong>downtown Brevard</strong> &mdash; a charming mountain town known as the &ldquo;Land of Waterfalls.&rdquo;</p>

<ul>
<li><strong><a href="https://www.optaylors.com/" target="_blank" rel="noopener noreferrer">O.P. Taylor&rsquo;s Toy Store</a></strong> &mdash; 16 S Broad St &mdash; Legendary independent toy store, one of the best in the Southeast! Floor-to-ceiling toys, games, puzzles, stuffed animals. Ethan will go wild. <strong>A Brevard must-stop.</strong></li>
<li><strong>Downtown Main Street &amp; Broad Street</strong> &mdash; Walkable downtown with local shops, galleries, bookstores, cafes, ice cream, and candy stores.</li>
<li><strong>White Squirrels!</strong> &mdash; Brevard is famous for its colony of white squirrels. Keep an eye out around downtown &mdash; they&rsquo;re real and they&rsquo;re everywhere.</li>
<li><strong>Lunch options:</strong> The Square Root (creative sandwiches &amp; salads), Rocky&rsquo;s Grill (burgers &amp; comfort food), Mayberry&rsquo;s (classic diner), or grab pizza and eat by the courthouse lawn.</li>
</ul>

<h3>Part 5 &mdash; The Marquee + Late Dinner in Asheville</h3>

<p>Instead of heading straight to the cabin from Brevard, take the same route north (US-276 &rarr; NC-280 &rarr; I-26) but exit into Asheville&rsquo;s <strong>River Arts District</strong> for The Marquee and dinner.</p>

<ul>
<li><strong><a href="https://marqueeasheville.com/" target="_blank" rel="noopener noreferrer">The Marquee</a></strong> &mdash; 36 Foundry St &mdash; A massive 50,000 sq ft curated indoor marketplace in a converted warehouse. <strong>145+ vendors</strong> selling art, antiques, vintage decor, jewelry, crafts, home goods, clothing, and more. European street market meets Asheville creativity. Bar on-site with drinks and snacks. Dog-friendly. <strong>Open daily 11 AM&ndash;6 PM.</strong></li>
<li><strong>Late dinner in Asheville</strong> &mdash; The River Arts District and downtown Asheville have endless options. A few family-friendly picks:
<ul>
<li><strong>12 Bones Smokehouse</strong> (South Slope) &mdash; Legendary Asheville BBQ, ribs &amp; smoked meats. Casual counter-service.</li>
<li><strong>Biscuit Head</strong> (multiple locations) &mdash; Southern comfort food, massive cat-head biscuits. Open late.</li>
<li><strong>Twisted Laurel</strong> (downtown) &mdash; Wood-fired pizza, craft cocktails. Family-friendly patio.</li>
<li><strong>White Duck Taco Shop</strong> (River Arts District) &mdash; Creative tacos, right near The Marquee. Quick, easy, kid-approved.</li>
</ul></li>
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
<li><strong>12:00 PM</strong> &mdash; Arrive at DuPont &mdash; <strong>Hooker Falls parking lot</strong> (Staton Rd, paved, restrooms)</li>
<li><strong>12:05 PM</strong> &mdash; <strong>Hooker Falls</strong> &mdash; 0.4 mi RT, flat gravel path, quick and easy (15 min)</li>
<li><strong>12:20 PM</strong> &mdash; Drive 5 min to <strong>High Falls Access parking</strong> (Cascade Lake Rd) &mdash; closer lot for Triple + High Falls</li>
<li><strong>12:30 PM</strong> &mdash; <strong>Triple Falls</strong> &mdash; 0.5 mi from this lot, wide easy trail (30&ndash;40 min)</li>
<li><strong>1:10 PM</strong> &mdash; <strong>High Falls</strong> &mdash; 0.3 mi past Triple Falls, tallest in DuPont (20 min)</li>
<li><strong>1:30 PM</strong> &mdash; Hike back to High Falls lot (~0.8 mi, 15&ndash;20 min)</li>
<li><strong>1:50 PM</strong> &mdash; Drive to downtown Brevard (~15 min from High Falls lot)</li>
<li><strong>2:05 PM</strong> &mdash; <strong>Lunch in downtown Brevard</strong> &mdash; restaurants, cafes, and the &ldquo;Land of Waterfalls&rdquo; vibe</li>
<li><strong>2:45 PM</strong> &mdash; <strong>O.P. Taylor&rsquo;s Toy Store</strong> (16 S Broad St) &mdash; legendary toy store, Ethan will love this!</li>
<li><strong>3:15 PM</strong> &mdash; Walk downtown &mdash; browse shops, grab ice cream, look for the <strong>white squirrels</strong></li>
<li><strong>3:45 PM</strong> &mdash; Leave Brevard, head north toward Asheville (~40 min via US-276 N &rarr; NC-280 &rarr; I-26)</li>
<li><strong>4:30 PM</strong> &mdash; Arrive at <strong>The Marquee</strong> (36 Foundry St, River Arts District) &mdash; 50,000 sq ft indoor marketplace, 145+ vendors. Browse art, antiques, vintage finds, crafts. Bar on-site. Closes at 6 PM.</li>
<li><strong>5:15&ndash;6:00 PM</strong> &mdash; Browse The Marquee (30&ndash;45 min)</li>
<li><strong>6:00 PM</strong> &mdash; <strong>Late dinner in Asheville</strong> &mdash; White Duck Taco (right in RAD), 12 Bones Smokehouse, Biscuit Head, Twisted Laurel, or your pick</li>
<li><strong>7:00&ndash;7:15 PM</strong> &mdash; Head to cabin (~15 min from Asheville via I-40 W)</li>
<li><strong>7:30 PM</strong> &mdash; Back at the cabin</li>
</ul>

<p><strong>Recommended combos based on energy:</strong></p>
<ul>
<li><strong>Easy (tired kid):</strong> Looking Glass Falls (steps only) &rarr; Sliding Rock (steps only) &rarr; BRP scenic drive &rarr; Hooker Falls (0.4 mi RT, flat) &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; The Marquee + dinner. <em>Total hiking: under 1 mile.</em></li>
<li><strong>Moderate (good energy):</strong> Looking Glass &rarr; Moore Cove (1.2 mi RT, flat) &rarr; Sliding Rock &rarr; BRP drive &rarr; Hooker Falls (lot A) &rarr; Triple Falls (lot B, 1 mi RT) &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; The Marquee + dinner. <em>Total hiking: ~2.6 mi.</em></li>
<li><strong>Full send (everyone fired up):</strong> All Pisgah falls &rarr; BRP + Skinny Dip Falls &rarr; All DuPont falls from both lots &rarr; Brevard + O.P. Taylor&rsquo;s &rarr; The Marquee + dinner. <em>Total hiking: ~4.2 mi.</em></li>
</ul>

<div class="tip" style="background:#fff8e1;border-left:4px solid #f9a825;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:0.95em;">
<strong>Scouting note:</strong> The US-276 corridor through Pisgah National Forest is everyone&rsquo;s backyard playground. Notice how close world-class waterfalls and the Blue Ridge Parkway are to Asheville. DuPont&rsquo;s Triple Falls from <em>The Hunger Games</em>, Brevard&rsquo;s walkable downtown with O.P. Taylor&rsquo;s, and Asheville&rsquo;s River Arts District (The Marquee, restaurants, creativity everywhere) show exactly the kind of family-friendly lifestyle this area offers.
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
    print("  12:00 PM  - DuPont: Hooker Falls parking (Staton Rd) -> 0.4 mi RT")
    print("  12:20 PM  - Drive 5 min to High Falls parking (Cascade Lake Rd)")
    print("  12:30 PM  - Triple Falls (0.5 mi) + High Falls (0.3 mi more)")
    print("  1:50 PM   - Drive to downtown Brevard")
    print("  2:05 PM   - Lunch in Brevard")
    print("  2:45 PM   - O.P. Taylor's Toy Store!")
    print("  3:15 PM   - Walk downtown, white squirrels, ice cream")
    print("  3:45 PM   - Leave Brevard -> Asheville (~40 min)")
    print("  4:30 PM   - The Marquee (36 Foundry St, River Arts District)")
    print("  6:00 PM   - Late dinner in Asheville")
    print("  7:15 PM   - Head to cabin (~15 min)")
    print("  7:30 PM   - Back at cabin")
    print("")
    print("BRP Status: OPEN (MP 382-420, confirmed after Helene repair)")
    print("Check morning-of: https://www.nps.gov/blri/planyourvisit/roadclosures.htm")
    print("")
    print("Preview: python -m http.server 8000")

if __name__ == "__main__":
    main()

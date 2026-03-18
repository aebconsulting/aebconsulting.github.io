#!/usr/bin/env python3
"""
Fix: Update Day 7 schedule — elevator + Exclamation Point, then waterfalls.
Depart cabin ~8:45 AM, arrive Chimney Rock ~10-10:30 AM.
Run from the trip-plan repo root: python fix_day7_schedule.py
"""
import os

HTML_FILE = "index.html"

def read_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()

def write_html(content):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

OLD_SCHEDULE = """<p><strong>Suggested Morning Schedule:</strong></p>
<ul>
<li><strong>8:30 AM</strong> &mdash; Arrive at park entrance, buy tickets / confirm reservation</li>
<li><strong>9:00 AM</strong> &mdash; Take elevator or stairs to Chimney summit viewpoint</li>
<li><strong>9:30 AM</strong> &mdash; Hike Skyline&ndash;Cliff Trail to Exclamation Point</li>
<li><strong>10:15 AM</strong> &mdash; Hike Hickory Nut Falls Trail to waterfall overlook</li>
<li><strong>11:30 AM</strong> &mdash; Walk Four Seasons Trail back toward parking</li>
<li><strong>12:00 PM</strong> &mdash; Lunch in Chimney Rock Village or Lake Lure</li>
</ul>"""

NEW_SCHEDULE = """<p><strong>Day 7 Schedule:</strong></p>
<ul>
<li><strong>8:45 AM</strong> &mdash; Depart cabin (~1 hr 10 min drive via I-40 E &rarr; I-26 E &rarr; Exit 49A &rarr; US-64 E &rarr; NC-9 S)</li>
<li><strong>10:00&ndash;10:30 AM</strong> &mdash; Arrive at Chimney Rock, park, buy tickets / confirm reservation</li>
<li><strong>10:30 AM</strong> &mdash; Take the elevator to the Chimney summit viewpoint</li>
<li><strong>10:45 AM</strong> &mdash; Hike Skyline&ndash;Cliff Trail to Exclamation Point (0.4 mi, easy &mdash; best panoramic views of Lake Lure &amp; Hickory Nut Gorge)</li>
<li><strong>11:15 AM</strong> &mdash; Head back down, quick look around Chimney Rock Village</li>
<li><strong>11:45 AM</strong> &mdash; Grab lunch in Chimney Rock Village or Lake Lure</li>
<li><strong>12:30 PM</strong> &mdash; Depart for Looking Glass Falls (~1 hr 15 min drive via US-64 W &amp; US-276)</li>
<li><strong>1:45 PM</strong> &mdash; Arrive at Looking Glass Falls &mdash; walk down staircase to base, explore &amp; photos</li>
<li><strong>2:30 PM</strong> &mdash; Optional: Drive to Sliding Rock (7 min) for a quick look</li>
<li><strong>3:00 PM</strong> &mdash; Head to Brevard for snacks or back to the cabin (~50 min)</li>
</ul>"""

OLD_AFTERNOON_SCHEDULE = """<p><strong>Suggested Afternoon Schedule:</strong></p>
<ul>
<li><strong>1:30 PM</strong> &mdash; Depart Chimney Rock / Lake Lure</li>
<li><strong>2:45 PM</strong> &mdash; Arrive at Looking Glass Falls pull-off</li>
<li><strong>2:50 PM</strong> &mdash; Walk down staircase to falls base, explore &amp; take photos</li>
<li><strong>3:30 PM</strong> &mdash; Optional: Drive to Sliding Rock for a quick look</li>
<li><strong>4:00 PM</strong> &mdash; Head to Brevard for snacks or back to the cabin</li>
</ul>"""

# Also update the hike list to focus on elevator + Exclamation Point
OLD_HIKE_LIST = """<ul>
<li><strong><a href="https://www.chimneyrockpark.com/view_trail/outcroppings-trail/" target="_blank" rel="noopener noreferrer">Outcroppings Trail</a></strong> &mdash; 0.25 miles, paved, to a stunning overlook. Easy for little legs.</li>
<li><strong><a href="https://www.chimneyrockpark.com/view_trail/hickory-nut-falls-trail/" target="_blank" rel="noopener noreferrer">Hickory Nut Falls Trail</a></strong> &mdash; 1.4 miles round trip to 400-ft waterfall. Moderate but doable for a motivated kid.</li>
<li>Option: Take the <strong>elevator</strong> to the top instead of hiking (26-story elevator inside the mountain!)</li>
<li><strong>Exclamation Point Trail</strong> &mdash; 1.4 mi round trip. Moderate. Best panoramic views of Lake Lure &amp; Hickory Nut Gorge.</li>
<li><strong>Four Seasons Trail</strong> &mdash; 0.6 mi. Easy nature walk through forest canopy back toward parking.</li>
<li><strong style="color:#15803d;">Chimney Rock reservation (moved from 3/16).</strong> Check with park about using timed-entry ticket on 3/17 &mdash; call <a href="tel:8286259611">(828) 625-9611</a> to confirm.</li>
</ul>"""

NEW_HIKE_LIST = """<ul>
<li><strong>Elevator to the top</strong> &mdash; 26-story elevator inside the mountain takes you straight to the Chimney summit. No hiking needed to reach the top!</li>
<li><strong>Skyline&ndash;Cliff Trail to Exclamation Point</strong> &mdash; 0.4 mi, easy. Short walk from the Chimney to the highest publicly accessible point. Best panoramic views of Lake Lure &amp; Hickory Nut Gorge. <strong>This is the main hike.</strong></li>
<li><em>Optional if time/energy:</em> <strong><a href="https://www.chimneyrockpark.com/view_trail/outcroppings-trail/" target="_blank" rel="noopener noreferrer">Outcroppings Trail</a></strong> &mdash; 0.25 mi, paved overlook. <strong><a href="https://www.chimneyrockpark.com/view_trail/hickory-nut-falls-trail/" target="_blank" rel="noopener noreferrer">Hickory Nut Falls Trail</a></strong> &mdash; 1.4 mi RT to 400-ft waterfall (skip if saving energy for Looking Glass Falls).</li>
<li><strong style="color:#15803d;">Chimney Rock reservation (moved from 3/16).</strong> Check with park about using timed-entry ticket on 3/17 &mdash; call <a href="tel:8286259611">(828) 625-9611</a> to confirm.</li>
</ul>"""

def main():
    if not os.path.exists(HTML_FILE):
        print(f"ERROR: {HTML_FILE} not found. Run from the trip-plan repo root.")
        return

    html = read_html()
    changes = 0

    # Replace morning schedule with full day schedule
    if OLD_SCHEDULE in html:
        html = html.replace(OLD_SCHEDULE, NEW_SCHEDULE)
        changes += 1
        print("  Updated morning schedule -> full day timeline")
    else:
        print("  WARNING: Morning schedule pattern not found")

    # Remove the separate afternoon schedule (now merged into one timeline)
    if OLD_AFTERNOON_SCHEDULE in html:
        html = html.replace(OLD_AFTERNOON_SCHEDULE, "")
        changes += 1
        print("  Removed separate afternoon schedule (merged into main timeline)")
    else:
        print("  WARNING: Afternoon schedule pattern not found")

    # Update hike list to focus on elevator + Exclamation Point
    if OLD_HIKE_LIST in html:
        html = html.replace(OLD_HIKE_LIST, NEW_HIKE_LIST)
        changes += 1
        print("  Updated hike list: elevator + Exclamation Point focus")
    else:
        print("  WARNING: Hike list pattern not found")

    if changes > 0:
        write_html(html)
        print(f"\nDone! {changes} updates applied to {HTML_FILE}")
        print("Next: git add index.html && git commit -m \"Update Day 7 schedule: elevator + Exclamation Point, then Looking Glass Falls\" && git push")
    else:
        print("\nNo changes made — patterns may not have matched.")

if __name__ == "__main__":
    main()

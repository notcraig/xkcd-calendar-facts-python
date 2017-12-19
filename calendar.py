#!/usr/bin/env python
# Dear gods of geekdom this is fugly.
# But it is my first "totally from scratch" python script. I learned all about lists, appending said lists, 
# the random module and other fun things.
#
# Inspired by https://xkcd.com/1930/

from random import choice
Equinox = ["Fall", "Spring", ]
Solstice = ["Summer", "Winter"]
Olympics = ["Summer", "Winter"]
Sunrise = ["Latest", "Earliest"]
Sunset = ["Latest", "Earliest"]
Daylight = ["Saving", "Savings"]
Leap = ["Day", "Year"]
Moon = ["Harvest", "Super", "Blood", ]
recurring_event = ["Easter",
                   "Toyota Truck Month",
                   "Shark Week",
                   ]
drifts = [" drifts out of sync with the Sun",
          " drifts out of sync with the Moon",
          " drifts out of sync with the Zodiac",
          " drifts out of sync with the atomic clock in Colorado", ]
calendar_type = ["Gregorian",
                 "Mayan",
                 "Lunar",
                 "iPhone", ]
manner = [" happens earlier",
          " happens later",
          " happens at the wrong time",
          " might not happen",
          " might happen twice"]

phenomena = ["a decree by the pope in the 1500s", "magnetic field reversal"]
tz_legislation = ["Indiana", "Arizona", "Russia"]


celestial1 = ["precession", "libration", "nutation",
              "libation", "eccentricity", "obliquity"]
celestial2 = ["Moon", "Sun",
              "Earth's axis",
              "equator",
              "prime meridian", "International Date Line", "Mason-Dixon Line"]
arbitrary_decision = ["Benjamin Franklin", "Isaac Newton", "FDR"]
apparent = ["it causes a predictable increase in car accidents.",
            "that's why we have leap seconds.",
            "scientists are really worried.",
            "it's getting worse and no one knows why."]
extreme = ["Bronze Age.", "Ice Age.", "Cretaceous.", "1990s."]
proposal = ["will never happen.", "actually makes things worse.",
            "is stalled in congress.", "might be unconstitutional."]

trivia = ["causes huge headaches for software developers",
          "is taken advantage of by high-speed traders",
          "triggered the 2003 Northeast Blackout",
          "has to be corrected for by GPS satellites", ]


for e in extreme:
    apparent.append("it was even more extreme during the " + e)
for p in proposal:
    apparent.append("there's a proposal to fix it, but it " + p)
for t in tz_legislation:
    phenomena.append("time zone legislation in " + t)
for person in arbitrary_decision:
    phenomena.append("an arbitrary decision by " + person)

for c1 in celestial1:
    for c2 in celestial2:
        c3 = c1 + " of the " + c2
        phenomena.append(c3)

# add calendar types to drifts
for item in calendar_type:
    item = " drifts out of sync with the " + item + " Calendar"
    drifts.append(item)

# add the drifts to manner
for item in drifts:
    manner.append(item)

# all recurring events to single list
for item in Equinox:
    item = "the " + item + " Equinox"
    recurring_event.append(item)

for item in Solstice:
    item = "the " + item + " Solstice"
    recurring_event.append(item)

for item in Olympics:
    item = "the " + item + " Olympics"
    recurring_event.append(item)

for item in Sunrise:
    item = "the " + item + " Sunrise"
    recurring_event.append(item)

for item in Sunset:
    item = "the " + item + " Sunset"
    recurring_event.append(item)

for item in Daylight:
    item = "Daylight " + item + " Time"
    recurring_event.append(item)

for item in Leap:
    item = "Leap " + item
    recurring_event.append(item)

for item in Moon:
    item = "the " + item + " Moon"
    recurring_event.append(item)


#
the_event = choice(recurring_event)
the_manner = choice(manner)
the_phenomena = choice(phenomena)
the_trivia = "While it may seem like trivia, it " + choice(trivia)
calendar_event = "Did you know that " + the_event + \
    the_manner + " because of " + the_phenomena + "?\n" + the_trivia

print(calendar_event)

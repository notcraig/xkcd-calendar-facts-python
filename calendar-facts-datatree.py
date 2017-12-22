#!/usr/bin/env python
# Dear gods of geekdom this is fugly.
# This is an exercise in learning about data trees.

from treelib import Node, Tree
from random import choice


event = Tree()
manner = Tree()
phenomena = Tree()
apparently = Tree()
trivia = Tree()
# Create tree roots

event.create_node("Did you know that", "event")
manner.create_node("Manner", "manner")
phenomena.create_node("because of", "because")
# event branches and leaves

event.create_node("Equinox", "equinox", parent="event")
event.create_node("Fall", "fallequinox", parent="equinox")
event.create_node("Spring", "springequinox", parent="equinox")
event.create_node("Olympics", "olympics", parent="event")
event.create_node("Winter", "winterolympics", parent="olympics")
event.create_node("Summer", "summerolympics", parent="olympics")
event.create_node("Solstice", "solstice", parent="event")
event.create_node("Winter", "wintersolstice", parent="solstice")
event.create_node("Summer", "summersolstice", parent="solstice")
event.create_node("Sunrise", "sunrise", parent="event")
event.create_node("Latest", "latestsunrise", parent="sunrise")
event.create_node("Earliest", "earliestsunrise", parent="sunrise")
event.create_node("Sunset", "sunset", parent="event")
event.create_node("Latest", "latestsunset", parent="sunset")
event.create_node("Earliest", "earliestsunset", parent="sunset")
event.create_node("Daylight", "daylight", parent="event")
event.create_node("Savings", "savings", parent="daylight")
event.create_node("Saving", "saving", parent="daylight")
event.create_node("Leap", "leap", parent="event")
event.create_node("Day", "leapday", parent="leap")
event.create_node("Year", "leapyear", parent="leap")
event.create_node("Easter", "easter", parent="event")
event.create_node("Moon", "moon", parent="event")
event.create_node("Harvest", "harvestmoon", parent="moon")
event.create_node("Super", "supermoon", parent="moon")
event.create_node("Blood", "bloodmoon", parent="moon")
event.create_node("Toyota Truck Month", "toyota", parent="event")
event.create_node("Shark Week", "sharkweek", parent="event")

# Create the unusual manners in which things happen

manner.create_node("happens",
                   "happens", parent="manner")
manner.create_node("every year",
                   "year", parent="happens")
manner.create_node("later",
                   "later", parent="year")
manner.create_node("earlier",
                   "earlier", parent="year")
manner.create_node("the wrong time",
                   "wrongtime", parent="year")
manner.create_node("drifts out of sync with the", "drifts", parent="manner")
manner.create_node("atomic clock in Colorado", "clock", parent="drifts")

manner.create_node("Sun", "sun", parent="drifts")
manner.create_node("Moon", "moon", parent="drifts")
manner.create_node("Zodiac", "zodiac", parent="drifts")
manner.create_node("Calendar", "calendar", parent="drifts")
manner.create_node("Gregorian", "gregorian", parent="calendar")
manner.create_node("Mayan", "mayan", parent="calendar")
manner.create_node("Lunar", "lunar", parent="calendar")

manner.create_node("iPhone", "iphone", parent="calendar")

manner.create_node("might", "might", parent="manner")
manner.create_node("not happen", "not", parent="might")
manner.create_node("happen twice", "twice", parent="might")

# Create the phenomena or political reasons
phenomena.create_node("time zone legislation in", "timezone", parent="because")
phenomena.create_node("Indiana", "indiana", parent="timezone")
phenomena.create_node("Arizona", "arizona", parent="timezone")
phenomena.create_node("Russia", "russia", parent="timezone")
phenomena.create_node("a decree by the pope in the 1500s",
                      "pope", parent="because")

# precession of

phenomena.create_node("the precession of ",
                      "precession", parent="because")
phenomena.create_node("the Sun",
                      "precessionsun", parent="precession")
phenomena.create_node("the Moon",
                      "precessionmoon", parent="precession")
phenomena.create_node("the Earth's Axis",
                      "precessionaxis", parent="precession")
phenomena.create_node("the equator",
                      "precessionequator", parent="precession")
phenomena.create_node("the prime meridian",
                      "precessionprime", parent="precession")
phenomena.create_node("Line", "precessionline", parent="precession")
phenomena.create_node("the International Date",
                      "precessioninternational", parent="precessionline")
phenomena.create_node("the Mason-Dixon",
                      "precessionmasondixon", parent="precessionline")

# libration of

phenomena.create_node("the libration of ",
                      "libration", parent="because")
phenomena.create_node("the Sun",
                      "librationsun", parent="libration")
phenomena.create_node("the Moon",
                      "librationmoon", parent="libration")
phenomena.create_node("the Earth's Axis",
                      "librationaxis", parent="libration")
phenomena.create_node("the equator",
                      "librationequator", parent="libration")
phenomena.create_node("the prime meridian",
                      "librationprime", parent="libration")
phenomena.create_node("Line", "librationline", parent="libration")
phenomena.create_node("the International Date",
                      "librationinternational", parent="librationline")
phenomena.create_node("the Mason-Dixon",
                      "librationmasondixon", parent="librationline")

# nutation of
phenomena.create_node("the nutation of ",
                      "nutation", parent="because")
phenomena.create_node("the Sun",
                      "nutationsun", parent="nutation")
phenomena.create_node("the Moon",
                      "nutationmoon", parent="nutation")
phenomena.create_node("the Earth's Axis",
                      "nutationaxis", parent="nutation")
phenomena.create_node("the equator",
                      "nutationequator", parent="nutation")
phenomena.create_node("the prime meridian",
                      "nutationprime", parent="nutation")
phenomena.create_node("Line", "nutationline", parent="nutation")
phenomena.create_node("the International Date",
                      "nutationinternational", parent="nutationline")
phenomena.create_node("the Mason-Dixon",
                      "nutationmasondixon", parent="nutationline")
# libation of
phenomena.create_node("the libation of ",
                      "libation", parent="because")
phenomena.create_node("the Sun",
                      "libationsun", parent="libation")
phenomena.create_node("the Moon",
                      "libationmoon", parent="libation")
phenomena.create_node("the Earth's Axis",
                      "libationaxis", parent="libation")
phenomena.create_node("the equator",
                      "libationequator", parent="libation")
phenomena.create_node("the prime meridian",
                      "libationprime", parent="libation")
phenomena.create_node("Line", "libationline", parent="libation")
phenomena.create_node("the International Date",
                      "libationinternational", parent="libationline")
phenomena.create_node("the Mason-Dixon",
                      "libationmasondixon", parent="libationline")
# eccentricity of
phenomena.create_node("the excentricity of ",
                      "excentricity", parent="because")
phenomena.create_node("the Sun",
                      "excentricitysun", parent="excentricity")
phenomena.create_node("the Moon",
                      "excentricitymoon", parent="excentricity")
phenomena.create_node("the Earth's Axis",
                      "excentricityaxis", parent="excentricity")
phenomena.create_node("the equator",
                      "excentricityequator", parent="excentricity")
phenomena.create_node("the prime meridian",
                      "excentricityprime", parent="excentricity")
phenomena.create_node("Line", "excentricityline", parent="excentricity")
phenomena.create_node("the International Date",
                      "excentricityinternational", parent="excentricityline")
phenomena.create_node("the Mason-Dixon",
                      "excentricitymasondixon", parent="excentricityline")

# obliquity of
phenomena.create_node("the obliquity of ",
                      "obliquity", parent="because")
phenomena.create_node("the Sun",
                      "obliquitysun", parent="obliquity")
phenomena.create_node("the Moon",
                      "obliquitymoon", parent="obliquity")
phenomena.create_node("the Earth's Axis",
                      "obliquityaxis", parent="obliquity")
phenomena.create_node("the equator",
                      "obliquityequator", parent="obliquity")
phenomena.create_node("the prime meridian",
                      "obliquityprime", parent="obliquity")
phenomena.create_node("Line", "obliquityline", parent="obliquity")
phenomena.create_node("the International Date",
                      "obliquityinternational", parent="obliquityline")
phenomena.create_node("the Mason-Dixon",
                      "obliquitymasondixon", parent="obliquityline")


# magnetic field reversal
phenomena.create_node("magnetic field reversal", "magnetic", parent="because")

# an arbitrary decision by ( Benjamin Franklin | Isaac Newton | FDR )
phenomena.create_node("an arbitrary decision by", "decision", parent="because")
phenomena.create_node("Benjamin Franklin", "ben", parent="decision")
phenomena.create_node("Isaac Newton", "newton", parent="decision")
phenomena.create_node("FDR", "fdr", parent="decision")


# wild card statement
apparently.create_node("Apparently", "apparently")
apparently.create_node(
    "it causes a predictable increase in car accidents.", "accidents", parent="apparently")
apparently.create_node("that's why we have leap seconds.",
                       "leapseconds", parent="apparently")
apparently.create_node("scientists are really worried.",
                       "scientists", parent="apparently")
apparently.create_node("it's getting worse and no one knows why.",
                       "worse", parent="apparently")
apparently.create_node("it was even more extreme during the",
                       "extreme", parent="apparently")
apparently.create_node("Bronze Age.",
                       "bronze", parent="extreme")
apparently.create_node("Ice Age.",
                       "ice", parent="extreme")
apparently.create_node("Cretaceous.",
                       "cretaceous", parent="extreme")
apparently.create_node("1990s",
                       "1990s", parent="extreme")

apparently.create_node("there's a proposal to fix it, but it",
                       "proposal", parent="apparently")
apparently.create_node("will never happen.",
                       "never", parent="proposal")
apparently.create_node("actually makes things worse.",
                       "worseproposal", parent="proposal")
apparently.create_node("is stalled in congress.",
                       "congress", parent="proposal")
apparently.create_node("might be unconstitutional.",
                       "unconstitutional", parent="proposal")

# Create trivia
trivia.create_node("While it may seem like trivia, it", "trivia")
trivia.create_node(
    "causes huge headaches for software developers", "software", parent="trivia")
trivia.create_node(
    "is taken advantage of by high-speed traders", "traders", parent="trivia")
trivia.create_node(
    "triggered the 2003 Northeast Blackout", "blackout", parent="trivia")
trivia.create_node(
    "has to be corrected for by GPS satellites", "gps", parent="trivia")


# print the event.
event.show(line_type="ascii-ex")
manner.show(line_type="ascii-ex")
phenomena.show(line_type="ascii-ex")
apparently.show(line_type="ascii-ex")
trivia.show(line_type="ascii-ex")

# # Assemble the parts
# leafs = []
# for child in apparently.is_branch('apparently'):
#     leafs.append((apparently[child].tag))

# theleaf = choice(leafs)
# print(theleaf)

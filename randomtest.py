#random tester
import libtcodpy as libtcod
import random
i = 0
d100 = 0.0
d20 = 0.0
d10 = 0.0
d8 = 0.0
d6 = 0.0
d4 = 0.0
d3 = 0.0
d2 = 0.0

while (i != 10001):
	d100 += libtcod.random_get_int(0, 1, 100)
	d20 += libtcod.random_get_int(0, 1, 20)
	d10 += libtcod.random_get_int(0, 1, 10)
	d8 += libtcod.random_get_int(0, 1, 8)
	d6 += libtcod.random_get_int(0, 1, 6)
	d4 += libtcod.random_get_int(0, 1, 4)
	d3 += libtcod.random_get_int(0, 1, 3)
	d2 += libtcod.random_get_int(0, 1, 2)
	i += 1
print "d100 average is " + str(d100 / 10000)
print "d20 average is " + str(d20 / 10000)
print "d10 average is " + str(d10 / 10000)
print "d8 average is " + str(d8 / 10000)
print "d6 average is " + str(d6 / 10000)
print "d4 average is " + str(d4 / 10000)
print "d3 average is " + str(d3 / 10000)
print "d2 average is " + str(d2 / 10000)

print str(libtcod.map_new(80, 50))

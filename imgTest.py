from life import *
from os import sys,popen
from sys import stdout

grid = randGrid(100,100)
grid = str2grid("""
.........................
..o......................
...o.....................
.ooo.....................
.........................
.........................
.........................
.........................
.........................
.........................
.........................
.........................
.........................
.........................
.........................
""",'o','.');
grid = str2grid("""
........................................
..........................o.............
........................o.o.............
..............oo......oo............oo..
.............o...o....oo............oo..
..oo........o.....o...oo................
..oo........o...o.oo....o.o.............
............o.....o.......o.............
.............o...o......................
..............oo........................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
""",'o','.')
num_gens = 200

for i in range(num_gens):
	saveGrid2Img(grid,"gen%03d.gif" % i,10,True)
	stdout.write("\rGeneration: %d/%d" % (i+1,num_gens))
	stdout.flush()
	grid = nextGen(grid)
stdout.write("\n")

stdout.write("Converting...\n")
popen("gifsicle --loop --delay=1 gen*.gif > out.gif")

stdout.write("Deleting frame images....\n")
popen("rm gen*.gif")

stdout.write("Opening...");
popen("open -a Firefox out.gif");

stdout.write("Done.")


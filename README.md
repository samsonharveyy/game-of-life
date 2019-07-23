# game-of-life

The objective in this problem is to create a simple simulator of “Conway’s Game of Life”. The general specification is
to present ten iterations of the Game of Life given an initial input grid. To help you visualize the output, follow this link: 
https://bitstorm.org/gameoflife/.

You will be given a text file with the following format:
N 

x1, y1

x2, y2

...

xN, yN

The first line of the file is an integer N. It is guaranteed to be greater than zero. N represents the number of succeeding
lines in the file.
Each of the next N lines have two integers. Both integres are guaranteed to be greater than zero. The values in each
line represents the x and y coordinates, respectively, which you will set to one as the initial state of the Game of Life
board. A sample file is presented below:
5

9,10

10,9

10,10

10,11

11,10


Note that the grid will be 0-indexed, so we can have input coordinates (20,20) as part of the input, but not
(21,21).

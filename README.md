# Nifty Fifty resolver

## The puzzle 

This project is a python implementation for
solving the Nifty Fifty puzzle.

It consists in fitting 4 wooden pieces looking
like charts in a restricted area. There is only 
one solution.

![image of the nifty fifty puzzle](nifty.jpg)

## Modeling the puzzle 

Each chart can be represented as a sequence of 
segments of discrete length, articulated with 
each other on right angles.

The restricted area is represented as a 2 dimensinal 
plan with discrete coordinates.

The following sketch illustrates the model.
A square irepresents a (x,y) unit

![graphical representation of the model](model.jpg)

## Model design

The charts are represented as a series of their points 
in a 2 dimensional array variable.

Each chart variable is named after its color:

- red
- yellow
- brown
- stripped

The available space is represented as a 2 dimensional 
array stored in the [grid.txt text file](grid.txt), as 
follows:

```
.......############
........###########
........###########
...........########
...........########
..............#####
...............####
...............####
...............####
##..............###
#####...........###
#####..............
#####..............
######.............
#######............
#######............
#########..........
#########..........
##########.........


# = unavailable space
. = available space
```

## Implementation 

[The algorithm](nifty.py) consists in bruteforcing all the possible
combinations until the 4 charts fit in the area.

### Chart arrangement

Each chart can be arranged in 4 different ways :

- initial
- flipped horizontally
- flipped vertically
- flipped both horizontally and vertically

There are 256 (4^4) possible arrangements.

### Positionning order 

Each try implies a given order, in other words which chart is postionned 1st, 2nd,  3rd and 4th.

There are 24 (4!) possible orderings.

### Combinations

A combination is a set of charts with specific arrangements and order.

All permutations of combinations need to be tested. 

There are 6144 (24x256) possible combinations.

### Resolution

- For each valid position of the 1st chart
  - For each valid position of the 2nd chart (given a selected position of the 1st chart)
    - For each valid position of the 3nd chart (given the selected positions of the previous charts)
      - If a valid position exists for the 4th chart (given the selected positions of the previous charts) , then the puzzle is solved !


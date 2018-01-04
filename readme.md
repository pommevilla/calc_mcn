# Calc_MCN

Python code to calculate the meridional coloring number of a knot diagram as outlined in [Wirtinger systems of generators of knot groups][wirtpaper].

## Description

*In progress*

The *meridional coloring number* of a knot diagram is the minimal number of generators required to generate the Wirtinger presentation of that knot diagram.  The problem of finding these generators can be reduced to assigning unique colors to a subset of the strands of the diagram and attempting to color the rest of the diagram according to a certain rule.

More information about the Gauss code of a knot diagram can be found [here][gaussinfo].

Full details of the algorithm are in *Section 4: Appendix: Computing $$\omega(D)$$* of the paper [Wirtinger systems of generators of knot groups][wirtpaper].


## Usage

Let `gauss_code` be a sequence of signed integers representing a knot diagram.  Open a command prompt in the same directory as `calc_mcn.py` and run `calc_mcn` from the command line by entering:

```
>python calc_mcn.py gauss_code
```

The output will be the knot dictionary corresponding to `gauss_code`, the seed strands that lead to a successful coloring, and the meridional coloring number of the knot diagram described by `gauss_code`.  See examples below.

## Examples

### Example 1

A Gauss code corresponding to a knot diagram of the [figure eight knot][fig8] is 1, -4, 3, -1, 2, -3, 4, -2.  Calling `calc_mcn` on this Gauss code will output the following:

```
>python calc_mcn.py 1 -4 3 -1 2 -3 4 -2

Knot dictionary:

    STRAND     SUBSEQUENCE                   CROSSINGS OVER
       A       (-1, 2, -3)                   ('C', 'D')
       B       (-4, 3, -1)                   ('D', 'A')
       C       (-2, 1, -4)                   ('A', 'B')
       D       (-3, 4, -2)                   ('B', 'C')

Seed strand set: ('A', 'B')
Meridional coloring number: 2
```

### Example 2

A Gauss code corresponding to a knot diagram of [K11n170][sample_knot] is 1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7.  Calling `calc_mcn` on this Gauss code will output the following:

```
>python calc_mcn.py 1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7

Knot dictionary:

    STRAND     SUBSEQUENCE                   CROSSINGS OVER
       A       (-5, 10, 8, -11)              ('G', 'I') ('C', 'J')
       B       (-11, 7, 1, -6)               ('J', 'K') ('I', 'D')
       C       (-8, -3)
       D       (-9, 3, -1)                   ('H', 'C')
       E       (-2, 6, -4)                   ('F', 'B')
       F       (-6, 2, -9)                   ('E', 'G')
       G       (-10, 5, -2)                  ('A', 'H')
       H       (-3, 9, -5)                   ('D', 'F')
       I       (-1, 4, -10)                  ('K', 'E')
       J       (-7, 11, -8)                  ('B', 'A')
       K       (-4, -7)

Seed strand set: ('A', 'B', 'D')
Meridional coloring number: 3
```

Note that the Gauss codes for Examples 1 and 2 are in different formats.  `calc_mcn` can handle Gauss code inputs with or without commas.

## Warnings

`calc_mcn` does NOT check for incorrect Gauss codes and will likely crash or return nonsensical answers.  "Incorrect" here means Gauss codes where there is some integer `x` without a corresponding `-x`.

## Details

*In progress*

## To Do

*In progress*

I am currently working on a dynamic programming solution for calculating the meridional coloring number of a knot diagram.  

## Contact

Send questions, comments, and feedback to pvillanueva13 at gmail dot com.

[wirtpaper]: https://arxiv.org/abs/1705.03108
[gaussinfo]: http://katlas.org/wiki/Gauss_Codes
[fig8]: http://katlas.org/wiki/4_1
[sample_knot]: http://katlas.org/wiki/K11n170


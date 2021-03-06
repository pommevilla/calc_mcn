# Calc_Wirt

Python code to calculate the Wirtinger number of a knot diagram.

## Description

Given a knot diagram, assign some *k* colors to a subset of its strands.  Then, at every crossing, if the over-strand and *only one* of the under-strands is colored, color the other under-strand the same color as the first over-strand.  

<p align = "center">
	<img src="https://github.com/pommevilla/calc_wirt/blob/master/excolmov.jpg" alt="Example of a coloring move.">
<p>


If you can repeat this process to color the whole knot diagram, then we say that the diagram is *k*-meridionally colorable.  For example, in the diagram of the figure eight knot below, we begin with two colored strands and can continue to color the rest of strands according to the coloring rule presented above.  Therefore, this diagram of the figure eight knot is 2-meridionally colorable.

<p align = "center">
	<img src="https://github.com/pommevilla/calc_wirt/blob/master/fig8col.jpg" alt="Sequence of coloring moves on the figure eight knot.">
<p>


We define the **Wirtinger number** of a knot diagram to be the smallest integer *k* such that the diagram is *k*-meridionally colorable.  For example, the Wirtinger number of the figure eight knot above is 2.  

This program automates the process of finding the Wirtinger number of a knot diagram.  Instead of keeping track of colors, we keep track of whether or not a strand has been colored with a set.  Then, a new strand can only be colored if the over-strand and under-strand that they are incident to at a crossing are already in this colored set.  A *knot dictionary*, derived from the diagram's Gauss code, is used to keep track of which strands are incident to each other. 

Let `gc` be the Gauss code of a knot diagram `D`.  The outline of the program is:

	1. Derive knot dictionary k_d from gc. 
	2. Pick 2 of the strands of D (represented by the keys of k_d) and attempt to 'color' the knot.
	3. If the knot was 'colored', return 2.  If not, repeat with all combinations of 2 strands.  If a successful coloring is found, return 2.
	4. If not, repeat this process with all combinations of 3 strands.  Return 3 if a successful coloring is found.  
	5. etc., etc...

Full details of the algorithm are in *Section 4: Appendix* of "[Wirtinger systems of generators of knot groups][wirtpaper]," the paper that I wrote in collaboration with Ryan Blair, Alexandra Kjuchukova, and Roman Velazquez.

## Usage

Download `calc_wirt.py` to a local directory (or just copy/paste the script from here).  


```
>python calc_wirt.py gauss_code
```

Here, `gauss_code` is a sequence of signed integers representing a knot diagram.  The output will be a line with the Wirtinger number of the knot diagram.

There are optional arguments for quiet and verbose modes:

```
>python calc_wirt.py -h
usage: calc_wirt.py [-h] [-v] [-q]

Calculate Wirtinger number of a knot diagram from its Gauss code

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  output knot dictionary
  -q, --quiet    only print Wirtinger number
```

In verbose mode, the output will also include the knot dictionary corresponding to the knot diagram as well as the seed strands that led to the first successful coloring. In quiet mode, the output will only be the integer representing the Wirtinger number of the knot diagram without any other text.  See examples below.

Compiled on Python 3.

## Examples

### Example 1

A Gauss code corresponding to a knot diagram of the [figure eight knot][fig8] is `1, -4, 3, -1, 2, -3, 4, -2`.  Calling `calc_wirt` on this Gauss code will output the following:

```
>python calc_wirt.py 1 -4 3 -1 2 -3 4 -2
Wirtinger number: 2
```

Calling `calc_wirt` with the `-v` (or `--verbose`) flag outputs the corresponding knot dictionary with the set of seed strands that lead to a complete coloring of the knot:

```
>python calc_wirt.py -v 1 -4 3 -1 2 -3 4 -2

Knot dictionary:

    STRAND     SUBSEQUENCE                   CROSSINGS OVER
       A       (-1, 2, -3)                   ('C', 'D')
       B       (-4, 3, -1)                   ('D', 'A')
       C       (-2, 1, -4)                   ('A', 'B')
       D       (-3, 4, -2)                   ('B', 'C')

Seed strand set: ('A', 'B')
Wirtinger number: 2
```

### Example 2

A Gauss code corresponding to a knot diagram of [K11n170][sample_knot] is `1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7`.  Calling `calc_wirt` on this Gauss code will output the following:

```
>python calc_wirt.py 1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7
Wirtinger number: 3
```

Note that the Gauss codes for Examples 1 and 2 are in different formats.  `calc_wirt` can handle Gauss code inputs with or without commas.

With the `--verbose` flag:

```
>python calc_wirt.py --verbose 1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7 

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
Wirtinger number: 3
```

Calling `calc_wirt` with the `-q` (or `--quiet`) flag will output only the Wirtinger number:

```
>python calc_wirt.py 1, -6, 2, -9, 3, -1, 4, -10, 5, -2, 6, -4, -7, 11, -8, -3, 9, -5, 10, 8, -11, 7 -q
3
```


## Warnings

`calc_wirt` does NOT check for incorrect Gauss codes and will likely crash or return nonsensical answers.  "Incorrect" here means Gauss codes where there is some integer *x* without a corresponding *-x*.

`calc_wirt' works for knots with up to 26 crossings, though I have modified this program to work on knots of larger size.  I am happy to share this version if requested.

## Details

More information about the Gauss code of a knot diagram can be found [here][gaussinfo].

The motivation for this program comes from the problem of finding generating sets of the Wirtinger presentation of the fundamental group of a knot exterior.  The coloring described in the first paragraph is an abstraction of a Wirtinger relation derived from the crossing of a knot diagram.  Thus, when we find a set of *k* strands that colors an entire knot diagram, we have actually found a set of strands whose meridians generate the entire knot group, as can be seen by iterating the Wirtinger relations in the diagram.  

In [our paper][wirtpaper], we prove that the minimum Wirtinger number over all knot diagrams of a knot *K* is equal to the bridge number of *K*. Having done so, we established a combinatoric-based approach for finding the bridge number of a knot and have added bridge number information for knots with 12, 13, 14, 15, and 16 crossings. Spreadsheets containing this information are available on Alexandra Kjuchukova's website [here][bridgelink].  

## To Do

- [ ] Implement dynamic programming solution 
- [x] Complete Description
- [x] Complete Details
- [x] Implement verbose and quiet options
- [x] ~~Post~~ Link Wirtinger numbers for 13-, 14-, 15-, 16-crossing knots.
- [ ] *(long term)* Publish `knot_utils` package

## Contact

Send questions, comments, and feedback to pvillanueva13 at gmail dot com.

[fig8col]: https://github.com/pommevilla/calc_wirt/blob/master/fig8col.jpg
[wirtpaper]: https://arxiv.org/abs/1705.03108
[gaussinfo]: http://katlas.org/wiki/Gauss_Codes
[fig8]: http://katlas.org/wiki/4_1
[sample_knot]: http://katlas.org/wiki/K11n170
[bridgelink]: https://sites.google.com/a/wisc.edu/alexandra-a-kjuchukova/bridge-numbers

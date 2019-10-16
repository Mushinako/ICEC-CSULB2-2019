# 8180 - Star Arrangements

The recent vote in Puerto Rico favoring United States statehood has made flag makers very excited. An updated flag with 51 stars rather than the urrent 50 would cause a huge jump in U. S. flag sales. The current pattern for 50 stars is five rows of 6 stars (30), interlaced with four offset rows of 5 stars (20).

This pattern has the property that adjacent rows differ by no more than one star. We represent this star arrangement compactly by the number of stars in the first two rows: `6,5`.

A 51-star flag that preserves the relationship can have three rows of 9 stars, interlaced with three rows of 8 stars (27 + 24 = 51), or `9,8`. If Guam were to also become a state, a 52-star flag could have 13 rows of 4 stars, or `13,13` (because there are 13 stars in each of the first 2 rows).

A star arrangement is visually appealing if it satisfies the following conditions:

* There are at least 2 rows of stars.
* All odd numbered rows have the same number of stars.
* All even numbered rows have the same number of stars.
* The difference in the number of stars between any two adjacent rows is either always 0, or always 1.
* The first row cannot have fewer stars than the second, nor can it have only 1 star.

Your team is to write a program that will, given the number of stars to place on a flag (**S**), find all possible visually appealing star arrangements.

## Input

Input to your program is a list of values of **S**, one number per line starting in the first column, where 3 ≤ **S** ≤ 10^6

## Output

For each line of input, your program is to print a line with the value of **S** immediately followed by a colon, then for each visually appealing star arrangement, print a line with a space followed by the compact star arrangement. Each compact star arrangement is to be printed in the form '`x,y`', with exactly one comma between `x` and `y` and no other characters.

The list of compact representations is to be printed in increasing order of the number of stars in the first row. If there are multiple compact representations with the same number of stars in the first row, print them in increasing order of the number of stars in the second row. The cases 1-by-**S** and **S**-by-1 are considered trivial, so do not print those arrangements.

## Sample

### Sample Input

```txt
3
50
51
52
```

### Sample Output

```txt
3:
 2,1
50:
 2,1
 2,2
 3,2
 5,4
 5,5
 6,5
 10,10
 13,12
 17,16
 25,25
51:
 2,1
 3,3
 9,8
 17,17
 26,25
52:
 2,2
 4,4
 7,6
 13,13
 26,26
```

# 8178 - Latin Squares

A Latin Square is an **n** × **n** array filled with **n** different symbols, with each symbol occurring exactly once in each row and once in each column. The name “Latin Square” was inspired by the work of Leonhard Euler, who used Latin characters in his papers on the topic.

A Latin Square is said to be in reduced form if both its first (top) row and first (leftmost) column are in their natural order.

Your team is to write a program that will read a series of square **n** × **n** arrays, where **n** is in the range 2 through 36 inclusive. For each array your program is to determine if it is a Latin Square, and if so, if it is in reduced form.

## Input

Input to your program will be a series of square arrays. The first line for each array is the value of **n**, starting in the first column. The next **n** lines each contain **n** characters in base **n**, using the characters `0` through `9` and upper-case `A` (10) through `Z` (35). The last line of the last array is followed by end-of-file.

## Output

If the array is not a Latin Square, print a line ontaining only the string `No`. If it is a Latin Square, but not in reduced form, print a line containing only the string `Not Reduced`. If it is a Latin Square in reduced form, print a line containing only the string `Reduced`.

No leading or trailing whitespace is to appear on an output line.

## Sample

### Sample Input

```txt
3
012
120
201
4
3210
0123
2301
1032
11
0123458372A
A9287346283
0285475A834
84738299A02
1947584037A
65848430002
038955873A8
947530200A8
93484721084
95539A92828
04553883568
```

### Sample Output

```txt
Reduced
Not Reduced
No
```

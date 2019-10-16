# 8181 Halfway

A friend of yours has written a program that compares every pair of ... something. With **n** items, it works like this: First, it prints a 1, and it compares item 1 to items 2, 3, 4, ..., **n**. It then prints 2, and compares item 2 to items 3, 4, 5, ..., **n**. It continues like that until every pair has been compared exactly once. If it compares item number *x* to item number *y*, it will not later compare item number *y* to item number *x*. It will not compare any item to itself.

Your friend wants to know when his program is halfway done. Assuming that all comparisons take the same amount of time, what will the last number printed be when the program is exactly halfway done? For an odd number of comparisons, this is when it’s doing the middle comparison. For an even number, it’s the first of the two middle comparisons. Note that since the earlier items have more comparisons than the later items, the answer is not simply **n/2**.

## Input

Input to your program will be a series of lines terminated by end-of-file. Each line will consist of a single integer **n**, (2 ≤ **n** ≤ 10^9), which is the number of items. The integer will have no sign and no leading or trailing spaces.

## Output

For each input value, your program is to print a line containing an integer with no sign or leading or trailing spaces that is the last number printed by your friend’s program before it does the halfway comparison.

## Sample

### Sample Input

```txt
2
500
1919
1000000000
72
7
```

### Sample Output

```txt
1
147
562
292893219
21
2
```

# 8179 - Congruent Numbers

A *congruent number* is an integer that is the area of some right triangle where the length of each side of the triangle is a rational number.

A rational number is a fraction, **p/q**, where **p**, the numerator, and **q**, the denominator, are integers. Note that if **q** = 1, then **p** = 1 is an integer; therefore, an integer is a rational number.

The *"congruent number problem"* is: given an integer **n**, is it a congruent number? Mathematicians have been working on this since the Middle Ages, so far without success. There is a test that relies on the unproven *Birch and Swinnerton-Dyer conjecture*. If you can prove that conjecture you win a one million dollar prize from the Clay Mathematics Institute. (Your team can work on the proof after the contest.)

The task here is much easier: given a and b, the nonhypotenuse sides of a right triangle, determine if the area of that triangle is a congruent number. That is, determine if the lengths of all three sides of the triangle are rational numbers and the area n is an integer.

Where **c**^22 = **a**^2 + **b**^2, **a**, **b**, **c**, are rational numbers and **n** is an integer.

## Input

Input to your program will be a series of lines terminated by end-of-file. Each line will consist of two positive rational numbers of the form **p** or **p/q** where **p** and **q** are integers with no embedded signs or spaces and the two rational numbers are separated by whitespace. The maximum number of digits in a numerator (**p**) or denominator (**q**) is 100.

## Output

For each input pair, your program is to print a line with **n**, the integer area of the triangle, if **n** is a congruent number or the word 'no' if not. No leading or trailing whitespace is to be printed on an output line. There are to be no signs or leading zeroes in front of an integer.

## Sample

### Sample Input

```txt
3 4
3/2 20/3
3/5 4/5
1 10
335946000/2950969 233126551/167973000
20 21
12 35
65979511071975972/2305628412171265 16139398885198855/251830194931206
```

### Sample Output

```txt
6
5
no
no
79
210
210
917
```

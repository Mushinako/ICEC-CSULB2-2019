# 10562 - Undraw the Trees

Professor Homer has been reported missing. We suspect that his recent research works might have had something to with this. But we really don’t know much about what he was working on! The detectives tried to hack into his computer, but after hours of failed efforts they realized that the professor had been lot more intelligent than them. If only they could realize that the professor must have been absent minded they could get the clue rightaway. We at the crime lab were not at all surprised when the professor’s works were found in a 3.5" floppy disk left inside the drive.

The disk contained only one text file in which the professor had drawn many trees with ASCII characters. Before we can proceed to the next level of investigation we would like to match the trees drawn with the ones that we have in our database. Now you are the computer geek, we leave this trivial task for you. Convert professor’s trees to our trees.

## Input

The first line of the input file (which you can assume comes from standard input) contains the number of trees, **T** (1 ≤ **T** ≤ 20) drawn in the file. Then you would have **T** trees, each ending with a single hash (`#`) mark at the beginning of the line. All the trees drawn here are drawn vertically in top down fashion. The labels of each of node can be any printable character except for the symbols `-`, `|`, ` ` (space) and `#`. Every node that has children has a `|` symbol drawn just below itself. And in the next line there would be a series of `-` marks at least as long as to cover all the immediate children. The sample input section will hopefully clarify your doubts if there is any. No tree drawn here requires more than 200 lines, and none of them has more than 200 characters in one line.

## Output

Our trees are drawn with parenthesis and the node labels. Every subtree starts with an opening parenthesis and ends with a closing parenthesis; inside the parenthesis the node labels are listed. The sub trees are always listed from left to right. In our database each tree is written as a single string in one line, and they do not contain any character except for the node labels and the parenthesis pair. The node labels can be repeated if the original tree had such repetitions.

## Sample

### Sample Input

```txt
2
A
|
--------
B C D
| |
----- -
E F G
#
e
|
----
f g
#
```

### Sample Output

```txt
(A(B()C(E()F())D(G())))
(e(f()g()))
```

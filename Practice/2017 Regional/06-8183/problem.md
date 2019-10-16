# 8183 - Haiku

A haiku is a three-line poem in which the first and third lines contain five syllables each, and the second line contains seven syllables.

An example of a haiku is:

> Blue Ridge mountain road.
> Leaves, glowing in autumn sun,
> fall in Virginia.

Write a program to examine a line of English text and and attempt to render it as a haiku.

This will require counting the syllables in the words of the text, which should be done according to the following rules:

1. A word consists of a maximal string of alphabetic characters (upper and/or lower-case), followed by zero or more non-blank, non-alphabetic characters.
    1. Upper/lower case distinctions are ignored for the purpose of counting syllables, but must be retained in the final output.
    2. Non-alphabetic characters are ignored for the purpose of counting syllables, but must be retained in the final output.
2. The characters “A”, “E”, “I”, “O”, “U”, and “Y” are vowels. All other alphabetic characters are consonants, with these exceptions:
    1. The character sequence “QU” is considered to be a single consonant.
    2. The letter “Y” is considered to be a consonant if it is immediately followed by one of the other vowels.
3. Every word has at least one syllable. For example, “Fly”,“I”, and “Ssshhh!” are words of one syllable.
4. Each (maximal) string of one or more consonants with at least one vowel to either side indicates a division into separate syllables. For example, “strong” has one syllable, “stronger” has two, and “bookkeeper” has three. “player” has two syllables (because the “y”, being followed by an “e”, is considered a consonant). There are two exceptions to this rule:
    1. An “E” appearing as the last alphabetic character in a word is silent and should be ignored unless the next-to-last alphabetic character is an “L” and the character immediately before that is another consonant. For example, “ale” and “pale” have one syllable. “able” has two.
    2. An “ES” sequence at the end of the alphabetic sequence in a word does not add a syllable unless preceded by two or more consonants. For example, “ales” and “pales” have one syllable. “witches” and “verses” have two.

## Input

Input to your program will consist of a series of lines of text consisting of a sequence of one or more words (as defined above) separated by single spaces. The total line length will not exceed 200 characters.

## Output

If the words in a given input line can be divided into a haiku, then print the haiku as three lines of output.

* Each line should be left-justified.
* A single space should separate each pair of words within a line.
* Each word should appear exactly as it does in the input, preserving case and any terminal nonalphabetic characters.
* Do not split a word across multiple lines.

If the words in the input cannot be divided into a haiku, print the line of input with no changes.

## Sample

### Sample Input

```txt
Blue Ridge mountain road. Leaves, glowing in autumn sun, fall in Virginia.
Who would know if we had too few syllables?
International ontest- motivation high Programmers have fun!.
```

### Sample Output

```txt
Blue Ridge mountain road.
Leaves, glowing in autumn sun,
fall in Virginia.
Who would know if we had too few syllables?
International
ontest- motivation high
Programmers have fun!.
```

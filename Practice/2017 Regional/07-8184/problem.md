# 8184 - Law 11

The *Laws of the Game* describe the rules to soccer (internationally known as “football”). Of the seventeen enumerated laws, Offside as described by Law 11 is perhaps the most contentious. Law 11 takes barely more than a single page to describe. In short, offside consists of two conditions: the offside position, and a state of play that turns the offside position into an offense. To consistently enforce offside position at youth soccer matches (and generally ratchet down the poor sportsmanship of parents who onsider themselves smarter than the referees, but too selfish to serve as referees themselves), your team has been ocntacted to implement a program for offside position determination.

The offside position may be stated as

1. *any part of the head, body, or feet (but not hands or arms) is in the opponents’ side of the field (excluding the halfway line)*, AND
2. *any part of the head, body, or feet (but not hands or arms) is closer to the opponents’ goal line than BOTH the ball and the second-to-last opponent.*

Your program is to treat all lines as one-dimensional, with the ball and players treated as points. Condition 1 is satisfied anytime the point representing a player is in the opponent’s half of the field. (A player at mid-field (x = 0) is not in the opponent’s half of the field.) Your program will unburden the referees from having to track 22 players spread across the playingfield. This frees the referees to make the judgment calls that humans are better at.

## Input

Your program must take time-series data for the *x, y* position of the ball and the *x, y* positions of 22 players (11 on each team). Input to your program starts with a line describing the length, **L**, and width, **W**, of the soccer pitch, measured in meters. **L** and **W** are separated by a comma. The remaining input is a series of three-line groups. Within each group, the first line will contain the timestamp ('`mm:ss`', minutes and seconds into the half), followed by the *x* and *y* coordinates of the ball. These fields are separated by commas. The second line contains 22 comma-separated values, 11 *x, y* pairs representing the coordinates of players numbered 1 through 11 on team "Left", defending the goal on the left side of the field. The third line contains 22 comma-separated values as well; these are the *x, y* coordinates of players numbered 1 through 11 on team "Right", defending the goal on the right side of the field.

In some example, team "Left" defends the goal at `x = −L/2`. Team "Right" defends the goal at `x = L/2`. The center of the field is at oordinate `(0, 0)`. Players stepping out of bounds are still considered in play; specifically, players beyond the goal lines (`|x| > L/2`) are considered to be at the respective goal line for offside position determination.

## Output

Only for time points (lines) that have players in offside position(s), print a line of output.

Begin the line with the '`mm:ss`' timestamp of the data. If there are any players in offside positions for team Left, print a single space, followed by 'Left'. For each player on team Left that is in an offside position, print a single space followed by the number of that player, 1 through 11, in ascending order by player number.

Similarly, if there are any players in offside positions for team Right, print a single space, followed by 'Right'. For each player on team Right that is in an offside position, print a single space followed by the number of that player, 1 through 11, in ascending order by player number.

## Sample

### Sample Input

```txt
90,50
00:00,0,25
-45,25,0,25,-10,20,-10,21,-10,22,-10,23,-10,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,10,29
00:01,-5,25
-45,25,15,25,-10,20,-10,21,-10,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,20,29
00:02,10,25
-45,25,20,25,-10,20,-10,21,-10,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,15,29
00:03,15,25
-45,25,20,25,-10,20,-10,21,0,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,15,25
00:04,0,25
-45,25,15,26,-10,20,-10,21,10,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,15,25
00:05,-5,24
-45,25,20,26,-10,20,-10,21,20,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,15,25
00:06,10,25
-45,25,15,26,-10,20,-10,21,-10,22,-10,23,-5,24,-10,25,-10,26,-10,27,-10,28
45,25,10,20,10,21,10,22,10,23,10,24,10,25,10,26,10,27,10,28,15,25
```

### Sample Output

```txt
00:02 Left 2
00:03 Left 2
00:05 Left 2 5
```

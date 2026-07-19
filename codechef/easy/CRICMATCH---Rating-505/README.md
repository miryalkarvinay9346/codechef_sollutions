# CRICMATCH - Rating 505

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cricket Match

There is a cricket match in Chefland. Chef's team requires $N$ runs to win in $M$ overs.

Given that $1$ over consists of $6$ balls and a player can score a maximum of $6$ runs in a ball, find whether Chef's team can win.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $M$ — the number of runs required to win the game and the remaining number of overs.
### Output Format

For each test case, output on a new line, `YES`, if Chef's team can win the game. Otherwise, output `NO`.

You can print each character in uppercase or lowercase. For example `NO`, `no`, `No`, and `nO` are all considered identical.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq M \leq 100$
### Sample 1:
Input
Output

```
4
500 20
100 2
30 1
216 6
```

```
YES
NO
YES
YES
```

### Explanation:

 **Test case $1$:**  Chef's team requires $500$ runs to win. If they hit $6$ runs on every ball for $13$ overs, they will score $6\cdot 6\cdot 13 = 468$ runs.
In the $14^{th}$ over they can hit $6$ runs in the first five balls and $2$ runs in the sixth ball to get a total of $468 + 6\cdot 5 + 2 = 500$ runs.
Thus, Chef's team can win the game.

 **Test case $2$:**  Since $100$ is greater than the maximum runs that can be scored $2$ overs, it is not possible for Chef's team to win the game.

 **Test case $3$:**  Since $30$ is less than the maximum runs that can be scored in $1$ over, it is possible for Chef's team to win the game.

 **Test case $4$:**  Since $216$ is equal to the maximum runs that can be scored in $6$ overs, it is possible for Chef's team to win the game.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-19T08:40:30.354Z  

```py
# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    print("YES" if m*6*6>=n else "NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/CRICMATCH)
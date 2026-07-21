# SHOPCHANGE - Rating 526

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Shopping Change

Chef went shopping and bought items worth $X$ rupees ($1 \le X \le 100$). Unfortunately, Chef only has a single $100$ rupees note.

Since Chef is weak at maths, can you help Chef in calculating what money he should get back after paying $100$ rupees for those items?

### Input Format
- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line containing an integer $X$, the total price of items Chef purchased.
### Output Format

For each test case, output in a single line the money Chef has to receive back.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
### Sample 1:
Input
Output

```
3
1
25
100

```

```
99
75
0

```

### Explanation:

 **Test case-1:**  Since chef paid $100$ rupees for items worth $1$ rupee. He should get back $99$ rupees.

 **Test case-2:**  Since chef paid $100$ rupees for items worth $25$ rupees. He should get back $75$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T16:23:59.682Z  

```py
# cook your dish here
for _ in range(int(input())):
    x=int(input())
    print(100-x)
```

---

[View on CodeChef](https://www.codechef.com/problems/SHOPCHANGE)
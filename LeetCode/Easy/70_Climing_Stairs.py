"""
70. CLIMBING STAIRS
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many
distinct ways can you climb to the top?
"""

"""
first solution:
(14ms/62.22%)(13.2MB/51.93%)
memoization/tabulation
1. initialize memoization table of len(n+1)
2. initialize 0 and 1 to 1
3. add memo[i-1] and memo[i-2] to form memo[i]
/ represents number of ways that the number can be formed
4. return memo[i] / which is number n
"""


def climbStairs(n):
    count = 0
    memo = [0 for i in range(n // 1 + 1)]
    memo[0] = memo[1] = 1
    for i in range(2, len(memo)):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[i]


"""
second solution:
(12ms/77.62%)(13.30MB/51.93%)
memoization without table
1. initialize pointers, prev(minus 1) and prev2(minus 2)
2. set prev to 1, iterate from 1 to n+1
3. move value of prev to prev and set prev to prev + prev2
"""


def climbStairs_2(n):
    prev = 1
    prev2 = 0
    for i in range(1, n + 1):
        cur = prev + prev2
        prev2 = prev
        prev = cur
    return prev


if __name__ == "__main__":
    n = 4
    print(climbStairs(n))
    n2 = 10
    print(climbStairs(n))

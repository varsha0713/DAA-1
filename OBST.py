def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            freq_sum = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                cost = dp[i][r - 1] + dp[r + 1][j] + freq_sum
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

keys = [10, 12, 20]
freq = [34, 8, 50]
result = optimal_bst(keys, freq)
print("Optimal BST Cost:", result)
//OUTPUT:
Optimal BST Cost: 142
//

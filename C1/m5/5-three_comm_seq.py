def LCS(m, n, o, A, B, C):
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[m][n][o]


if __name__ == "__main__":
    m = int(input())
    A = list(map(int, input().split()))
    n = int(input())
    B = list(map(int, input().split()))
    o = int(input())
    C = list(map(int, input().split()))
    print(LCS(m, n, o, A, B, C))

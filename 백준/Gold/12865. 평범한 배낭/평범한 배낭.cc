#include <iostream>
#include <algorithm>

int main() {
    int N, K;
    int w[101];
    int v[100001];
    int dp[101][100001];

    std::cin >> N >> K;

    for (int n = 1; n <= N; n++) {
        std::cin >> w[n] >> v[n];
    }

    for (int n = 1; n <= N; n++) {
        for (int k = 1; k <= K; k++) {
            if (k - w[n] < 0) {
                dp[n][k] = dp[n-1][k];
            } else {
                dp[n][k] = std::max(
                    dp[n-1][k - w[n]] + v[n],
                    dp[n-1][k]
                );
            }
        }
    }

    std::cout << dp[N][K];
    
    return 0;
}
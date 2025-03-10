#include <iostream>
using namespace std;

void step_up(int n, int x[], int dp[]) {  // dp 배열을 전달
    dp[0] = 0;
    dp[1] = x[1];
    dp[2] = x[2] + dp[1];

    if (n > 2) {
        for (int i = 3; i <= n; i++) {
            dp[i] = x[i] + max(x[i-1] + dp[i-3], dp[i-2]);
        }
    }
}

int main() {
    int n;
    int x[301] = {};
    int dp[301] = {};

    x[0] = 0;
    
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        cin >> x[i];
    }

    step_up(n, x, dp);
    cout << dp[n] << endl;

    return 0;
}

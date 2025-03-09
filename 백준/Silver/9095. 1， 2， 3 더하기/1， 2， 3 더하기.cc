#include <iostream>
using namespace std;

void plus_123(int n, int dp[]) {  // dp를 배열로 전달
    if (n < 4) return;

    for (int i = 4; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
}

int main() {
    int test;
    int max_n = 0;
    int n[20] = {};
    int dp[20] = {};  // dp 배열 초기화
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    
    cin >> test;

    for (int i = 1; i <= test; i++) {
        cin >> n[i];
        if (max_n < n[i]) { max_n = n[i]; }  // 세미콜론 추가
    }

    plus_123(max_n, dp);  // dp를 배열로 전달하여 업데이트

    for (int i = 1; i <= test; i++) {
        cout << dp[n[i]] << endl;  // 줄바꿈 추가
    }

    return 0;
}

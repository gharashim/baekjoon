#include <iostream>
using namespace std;

void tile_2n(int n, int dp[]) {  // dp 배열을 전달
    if (n < 3) return;

    for (int i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;  // ✅ 값이 커지는 것을 방지
    }
}

int main() {
    int n;
    int dp[1001] = {};  // ✅ 배열 크기를 최적화 (1 ≤ n ≤ 1000)

    dp[1] = 1;
    dp[2] = 2;

    cin >> n;

    tile_2n(n, dp);  // dp 배열 업데이트
    cout << dp[n] << endl;  // ✅ 이미 나머지를 적용했으므로 추가 % 필요 없음

    return 0;
}

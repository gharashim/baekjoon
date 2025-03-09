#include <iostream>
#include <algorithm>  // min 함수를 사용하기 위해 필요
using namespace std;

int make_one(int n) {
    int dp[1000000] = {0}; // 배열 초기화
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;

    if (n < 4) {
        return dp[n]; // ✅ 세미콜론 추가
    }

    for (int iter = 4; iter <= n; iter++) { // ✅ while → for로 변경
        dp[iter] = dp[iter - 1] + 1; // 기본 연산 (1 빼기)

        if (iter % 2 == 0) {
            dp[iter] = min(dp[iter], dp[iter / 2] + 1); // ✅ 정수 나누기 사용
        }
        if (iter % 3 == 0) {
            dp[iter] = min(dp[iter], dp[iter / 3] + 1); // ✅ 정수 나누기 사용
        }
    }

    return dp[n];
}

int main() {
    int n;
    cin >> n;
    cout << make_one(n) << endl;
    return 0;
}

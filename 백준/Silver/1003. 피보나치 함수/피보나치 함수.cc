#include <iostream>
using namespace std;

void find_0_1(int n, int dp_0[], int dp_1[]) {  // dp를 배열로 전달
    if (n < 2) return;
    for (int i = 2; i <= n; i++) {
        dp_0[i] = dp_0[i - 1] + dp_0[i - 2];
        dp_1[i] = dp_1[i - 1] + dp_1[i - 2];
    }
}

int main() {
    int test;
    int max_n = 0;
    int n[1000] = {};
    int dp_0[1000] = {};  // dp 배열 초기화
    int dp_1[1000] = {};  // dp 배열 초기화
    
    dp_0[0] = 1;
    dp_0[1] = 0;

    dp_1[0] = 0;
    dp_1[1] = 1;
    
    cin >> test;

    for (int i = 1; i <= test; i++) {
        cin >> n[i];
        if (max_n < n[i]) { max_n = n[i]; }  // 세미콜론 추가
    }

    find_0_1(max_n, dp_0, dp_1);  // dp를 배열로 전달하여 업데이트

    for (int i = 1; i <= test; i++) {
        cout << dp_0[n[i]] << " " << dp_1[n[i]] << endl;
    }

    return 0;
}

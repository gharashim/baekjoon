#include <iostream>
using namespace std;

int get_sum(int N) {
    int sum = N;
    while (N > 0) {
        sum += N % 10;
        N /= 10;
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N;
    cin >> N;

    int ans = 0;

    for (int i = 1; i < N; i++) {
        if (get_sum(i) == N) {
            ans = i;
            break;
        }
    }

    cout << ans << '\n';
    return 0;
}

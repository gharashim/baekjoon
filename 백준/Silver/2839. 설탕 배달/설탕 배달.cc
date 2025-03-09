#include <iostream>
using namespace std;

int min_sugar_bags(int n) {
    int bags = 0;
    
    while (n >= 0) {
        if (n % 5 == 0) { // 5kg 봉지로 나누어떨어지는 경우
            bags += n / 5;
            return bags;
        }
        n -= 3; // 3kg 봉지를 하나 사용
        bags++;
    }
    
    return -1; // 정확한 무게를 맞출 수 없는 경우
}

int main() {
    int n;
    cin >> n;
    cout << min_sugar_bags(n) << endl;
    return 0;
}

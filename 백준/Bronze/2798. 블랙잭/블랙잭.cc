# include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int N; int M;
    int cards[101];
    int temp;
    int answer;
    
    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        cin >> cards[i];
    }

    answer = -1;

    for (int i = 1; i <= N - 2; i++) {
        for (int j = i + 1; j <= N - 1; j++) {
            for (int k = j + 1; k <= N; k ++) {
                temp = cards[i] + cards[j] + cards[k];
                if (temp > M) {continue;}
                if (answer < temp) {answer = temp;}
            }
        }
    }
    cout << answer << endl;
    return 0;
}
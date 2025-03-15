// 1. 입출력
// 2. 연산자 식별
// 3. 각 연산 수행하는 함수
// 4. 연산을 조합하여 최대 / 최소 계산

#include<iostream>
#include<vector>
using namespace std;

int N;
vector<int> numbers;
vector<int> cal_array;
vector<int> cals_input(4);

int result_min = 1e9, result_max = -1e9;

void input_test() {
    cout << N << "\n";

    for (int num : numbers) {cout << num;}
    cout << "\n";
    
    for (int cal : cals_input) {cout << cal;}
    cout << "\n---------------\n";
}

void calculation(vector<int> numbers, vector<int> &array) {
    int score = numbers[0];
    for (int i=1; i<N; i++) {
        if (array[i-1] == 0) score += numbers[i];
        if (array[i-1] == 1) score -= numbers[i];
        if (array[i-1] == 2) score *= numbers[i];
        if (array[i-1] == 3) score /= numbers[i];
    }

    if (result_min >= score) result_min = score;
    if (result_max <= score) result_max = score;
}

void DFS(int depth, vector<int> &array, vector<int> &cals) {
    if (depth == N - 1) {
        // for (int i : array) {
        //     cout << i << " ";
        // } cout << "\n";
        calculation(numbers, array);
        
        return;
    }
    
    for(int i=0; i<4; i++) {
        if (cals[i] == 0) continue;
        array.push_back(i);
        cals[i] -= 1;
        DFS(depth + 1, array, cals);
        array.pop_back();
        cals[i] += 1;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    numbers.resize(N);
    // cal_array.resize(N-1);
    
    for (int i=0; i<N; i++) {
        cin >> numbers[i];
    }
    
    for (int i=0; i<4; i++) {
        cin >> cals_input[i];
    }
    
    // input_test();
    DFS(0, cal_array, cals_input);

    cout << result_max << "\n";
    cout << result_min << "\n";
}
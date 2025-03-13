#include<iostream>
#include<vector>
using namespace std;

void DFS(int node, vector<int> &picked, int N, int M) {
    if (picked.size() == M) {
        for (int p : picked) {
            cout << p << " ";
        }
        cout << "\n";
        return;
    }

    for (int i=1; i<=N; i++) {
        picked.push_back(i);
        DFS(i, picked, N, M);
        picked.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N; int M;

    cin >> N >> M;

    vector<int> picked;

    DFS(1, picked, N, M);
}
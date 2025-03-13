#include<iostream>
#include<vector>
using namespace std;

void DFS(int node, int N, vector<bool> &visited, vector<int> &picked, int M) {
    if (picked.size() == M) {
        for (int p : picked) cout << p << " ";
        cout << "\n";
        return;
    }
    
    for (int i = node; i <= N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            picked.push_back(i);
            DFS(i + 1, N, visited, picked, M);
            visited[i] = false;
            picked.pop_back();
        }
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N; int M;

    cin >> N >> M;

    vector<int> picked;
    vector<bool> visited(N+1, false);

    DFS(1, N, visited, picked, M);
}
#include<iostream>
#include<vector>
using namespace std;

void DFS(int node, int N, vector<bool> &visited, vector<int> &pocket, int M) {
    if (pocket.size() == M) {
        for (int p : pocket) {cout << p << " ";}
        cout << "\n";
        return;
    }

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            pocket.push_back(i);
            DFS(i + 1, N, visited, pocket, M);
            visited[i] = false;
            pocket.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N; int M;
    vector<int> pocket;
    vector<bool> visited(N+1, false);

    cin >> N >> M;
    
    DFS(1, N, visited, pocket, M);    
}
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> graph;
bool visited[9];
vector<int> pocket;

void DFS(int node) {
    if (pocket.size() == 7) {
        int total = 0;
        for (int a : pocket) total += a;
        if (total == 100) {
            sort(pocket.begin(), pocket.end());
            for (int j : pocket) {
                cout << j <<endl;
            }
            exit(0);
        }
        return;
    }
    
    for (int n = node; n < 9; n++) {
        if (!visited[n]) {
            visited[n] = true;
            pocket.push_back(graph[n]);
            DFS(n + 1);
            pocket.pop_back();
            visited[n] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int x; 

    for (int i=0; i<9; i++) {
        cin >> x;
        graph.push_back(x);
    }

    DFS(0);
}
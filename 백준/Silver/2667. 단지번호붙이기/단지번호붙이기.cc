#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void DFS(int x, int y, vector<vector<int>> &graph, vector<vector<bool>> &visited, int &cnt, int N) {
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, -1, 0, 1};

    visited[x][y] = true;
    cnt += 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (!visited[nx][ny] && graph[nx][ny] == 1) {
                DFS(nx, ny, graph, visited, cnt, N);
            }
        }
    }
}

int main() {
    int N;
    cin >> N;

    vector<vector<int>> graph(N, vector<int>(N));
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    vector<int> result;

    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < N; j++) {
            graph[i][j] = row[j] - '0';
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j] && graph[i][j] == 1) {
                int cnt = 0;
                DFS(i, j, graph, visited, cnt, N);
                result.push_back(cnt);
            }
        }
    }

    sort(result.begin(), result.end());

    cout << result.size() << '\n';
    for (int num : result) {
        cout << num << '\n';
    }

    return 0;
}

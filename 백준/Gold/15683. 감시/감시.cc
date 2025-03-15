#include<iostream>
#include<vector>
using namespace std;

int N; int M;
vector<vector<int>> office;
vector<pair<int, int>> cctvs;
int result = 1e9;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void watch(int x, int y, vector<vector<int>> &map, int dir) {
    while(1) {
        x += dx[dir];
        y += dy[dir];

        if (x < 0 || x >= N || y < 0 || y >= M) return;
        if (map[x][y] == 6) return;
        if (map[x][y] == 0) map[x][y] = -1;
    }
}

void count_unwatch(vector<vector<int>> map) {
    int cnt = 0;
    
    for (vector<int> line: map) {
        for (int i: line) {
            if (i == 0) cnt += 1;
        }
    }

    if (cnt < result) result = cnt;
}

void DFS(int depth, vector<vector<int>> map) {
    count_unwatch(map);
    // for (int i=0; i<N; i++) {
    //     for (int j=0; j<M; j++) {
    //         cout <<  map[i][j] << " ";
    //         } cout << "\n";
    // } cout << "\n";
    // cout << result << "\n" << "\n";
    
    if (depth == cctvs.size()) return;

    int x, y;

    x = cctvs[depth].first;
    y = cctvs[depth].second;

    for (int dir=0; dir<4; dir++) {
        vector<vector<int>> tmp = map;
        
        if (tmp[x][y] == 1) {
            watch(x, y, tmp, dir);
        }

        if (tmp[x][y] == 2) {
            watch(x, y, tmp, dir);
            watch(x, y, tmp, (dir + 2) % 4);
        }
        
        if (tmp[x][y] == 3) {
            watch(x, y, tmp, dir);
            watch(x, y, tmp, (dir + 1) % 4);
        }
        
        if (tmp[x][y] == 4) {
            watch(x, y, tmp, dir);
            watch(x, y, tmp, (dir + 1) % 4);
            watch(x, y, tmp, (dir + 2) % 4);
        }
        
        if (tmp[x][y] == 5) {
            watch(x, y, tmp, 0);
            watch(x, y, tmp, 1);
            watch(x, y, tmp, 2);
            watch(x, y, tmp, 3);
            DFS(depth + 1, tmp);
            break;
        }
        DFS(depth + 1, tmp);
    }
    
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    office.resize(N, vector<int>(M));

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >>  office[i][j];
            if (office[i][j] >= 1 && office[i][j] <= 5) {
                cctvs.push_back({i,j});
            }
        }
    }

    DFS(0, office);
    cout << result;

}
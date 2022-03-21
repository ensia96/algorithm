import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 9**9
n, m = L()
n += 1
E, N = [[]for _ in ' '*n], [1]*n
for _ in ' '*m:
    a, b, c = L()
    E[a] += (b, c),
    E[b] += (a, c),
for e in E:
    e.sort()
s, e = L()


def F():
    D, Q = [M]*n, [(0, s)]
    D[s] = 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i, j in E[y]:
            if D[i] > D[y]+j and N[i]:
                D[i] = D[y]+j
                h.heappush(Q, (D[i], i))
    return D[e]


def D(x, y):
    if x == e or y > A:
        return y == A
    for i, j in E[x]:
        if N[i]:
            N[i] = 0
            if D(i, y+j):
                return 1
            N[i] = 1


A = F()
D(s, 0)
N[e] = 1
print(A+F())

# (시간 초과 해결 방법이 안 떠올라서, 아래 블로그 참조 + 코드 다듬어서 제출...)
# https://ongveloper.tistory.com/236
# #include<iostream>
# #include<queue>
# #include<vector>
# #include<climits>
#
# using namespace std;
#
# const int INF = 0x3f3f3f3f;
# vector<vector<pair<int, int>>> graph;
# vector<int> distS, distE;
# vector<int> used;
#
# void dijkstra(vector<int> &dist, int S) {
#     priority_queue<pair<int, int>> pq;
#     dist[S] = 0;
#     pq.emplace(0, S);
#     while(!pq.empty()) {
#         auto [d, cur] = pq.top(); pq.pop();
#         if(dist[cur] != -d) continue;
#         for(auto [nxt, cost] : graph[cur]) {
#             if(used[nxt]) continue;
#             if(dist[nxt] > dist[cur] + cost) {
#                 dist[nxt] = dist[cur] + cost;
#                 pq.emplace(-dist[nxt], nxt);
#             }
#         }
#     }
# }
#
# void eraseEdge(int S, int E) {
#     int pre = S;
#     while(S != E) {
#         int mn = INT_MAX;
#         for(auto [nxt, cost] : graph[S]) {
#             if(nxt == pre) continue;
#             if(distS[S] + cost + distE[nxt] == distS[E]) mn = min(mn, nxt);
#         }
#         pre = S;
#         S = mn;
#         if(S != E) used[S] = 1;
#     }
# }
#
# int main() {
#     ios::sync_with_stdio(false);
#     cin.tie(0);
#
#     int N, M; cin >> N >> M;
#     graph.resize(N);
#     used.resize(N);
#
#     distS.resize(N, INF);
#     distE.resize(N, INF);
#
#     for(int i = 0; i < M; i++) {
#         int a, b, c; cin >> a >> b >> c;
#         graph[--a].emplace_back(--b, c);
#         graph[b].emplace_back(a, c);
#     }
#     int S, E; cin >> S >> E;
#     --S; --E;
#
#     dijkstra(distS, S); dijkstra(distE, E);
#     int ans = distS[E];
#     eraseEdge(S, E);
#     distE = vector<int>(N, INF);
#     dijkstra(distE, E);
#     ans += distE[S];
#     cout << ans;
#
#     return 0;
# }

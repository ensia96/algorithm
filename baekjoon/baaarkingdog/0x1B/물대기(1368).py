# 설명을 듣고도 전혀 감이 안 와서, 인터넷에서 풀이 찾아봄..
# https://lastknight00.tistory.com/123

# #include <algorithm>
# #include <cstdio>
# #include <vector>

# using namespace std;
# typedef pair<int, pair<int, int>> P;
# int n, t, m, i, j, s, g[301];
# vector<P> v;
# int f(int a) { return a == g[a] ? a : g[a] = f(g[a]); }
# void u(int a, int b) { g[f(a)] = f(b); }

# int main()
# {
# scanf("%d", &n);
# for (i = 1; i <= n; i++)
# scanf("%d", &t), v.push_back({ t, { i, 0 } }), g[i] = i;
# for (i = 1; i <= n; i++) {
# for (j = 1; j <= n; j++) {
# scanf("%d", &t);
# if (i < j)
# v.push_back({ t, { i, j } });
# }
# }
# sort(v.begin(), v.end());
# for (P p : v) {
# i = p.second.first;
# j = p.second.second;
# if (f(i) != f(j))
# s += p.first, u(i, j);
# }
# printf("%d", s);
# }

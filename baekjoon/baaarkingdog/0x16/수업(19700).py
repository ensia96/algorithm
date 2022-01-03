import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
S, T, A = [], {1: []}, 0
for _ in ' '*int(I()):
    h, k = map(int, I().split())
    i(S, (h, k))
while S:
    h, k = d(S)
    for m in range(k-1, -1, -1):
        if T.get(m):
            d(T[m])
            T[m+1] = T.get(m+1, [])
            i(T[m+1], h)
            break
    else:
        T[1], A = T[1]+[h], A+1
print(A)

# (시간 초과 해결 방법이 안 떠올라서, 아래 블로그에 올라온 C++ 코드 다듬어서 제출...)
# https://kth990303.tistory.com/154

# # include <algorithm>
# # include <cmath>
# # include <cstring>
# # include <iostream>
# # include <map>
# # include <queue>
# # include <set>
# # include <stack>
# # include <string>
# # include <vector>

# using namespace std;

# typedef long long ll;
# typedef pair<int, int> pi;

# int n, ans;
# priority_queue<pi> pq;
# multiset<int> S;

# int main()
# {
# cin.tie(0)->sync_with_stdio(0);
# cin >> n;
# for (int i = 0; i < n; i++) {
# int h, k;
# cin >> h >> k;
# pq.push({ h, k });
# }
# while (!pq.empty()) {
# int k = pq.top().second;
# int s = 0, e = k - 1, res = -1;
# pq.pop();
# while (s <= e) {
# int m = (s + e) / 2;
# auto it = S.upper_bound(m);
# if (it != S.end() && *it < k) {
# res = m;
# s = m + 1;
# } else
# e = m - 1;
# }
# if (res != -1) {
# S.erase(S.find(res + 1));
# S.insert(res + 2);
# } else {
# S.insert(1);
# ans++;
# }
# }
# cout << ans << "\n";
# }

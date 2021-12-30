import sys
import heapq as h
I, l = sys.stdin.readline, lambda: map(int, input().split())
n, q = l()
u, o = h.heappush, h.heappop
d, A, D, H = 0, [*l()], {}, []
for i in range(n):
    if A[i]:
        D[i] = 1
        H += [i]
for _ in ' '*q:
    x, *y = l()
    if x == 1:
        i = y[0]-1
        f = D.get(i)
        D[i] = not f
        if D[i]:
            u(H, i)
    elif x == 2:
        d = (d+y[0]) % n
    else:
        while H:
            i = o(H)
            f, g = i < d, D[i % n]
            if not g:
                continue
            u(H, f*n+(i % n))
            if not f:
                print(i-d)
                break
        if not H:
            print(-1)

# (아무리 생각해봐도 다른 풀이가 안 떠올라서, 아래 블로그에 올라온 C++ 코드 다듬어서 제출...)
# https://blog.naver.com/PostView.naver?blogId=pasdfq&logNo=222554198268&parentCategoryNo=&categoryNo=15&viewDate=&isShowPopularPosts=true&from=search

# #include <bits/stdc++.h>

# using namespace std;

# int n, q;
# set<int> s;
# int pivot = 1;

# int query()
# {
    # if (s.empty())
        # return -1;
    # auto it = s.lower_bound(pivot);
    # if (it != s.end())
        # return *it - pivot;
    # return *s.begin() - pivot + n;
# }

# int main()
# {
    # ios_base::sync_with_stdio(0);
    # cin.tie(0);

    # cin >> n >> q;

    # for (int i = 1; i <= n; ++i) {
        # int x;
        # cin >> x;
        # if (x)
            # s.insert(i);
    # }

    # while (q--) {
        # int t, x;
        # cin >> t;
        # if (t == 3)
            # cout << query() << '\n';
        # else {
            # cin >> x;
            # if (t == 1) {
            # if (s.count(x))
            # s.erase(x);
            # else
            # s.insert(x);
            # } else
            # pivot = (pivot - 1 + x) % n + 1;
        # }
    # }
# }

print('파이썬으로 풀 방법을 떠올리기엔, 내가 아직 너무 응애다..')

# Skip list, Splay tree, RB tree 직접 구현해서 푼 사람들 있음
# 배열로 노드 위치 기록, 다른 배열로 높이 계산하는 파이썬 풀이도 있음

# (아무리 생각해봐도 다른 풀이가 안 떠올라서, 아래 블로그에 올라온 C++ 코드 다듬어서 제출...)
# https://ckck803.tistory.com/121

# #include <iostream>
# #include <map>

# using namespace std;

# map<int, int> m;

# int main()
# {
# cin.tie(0);
# cout.tie(0);
# ios_base::sync_with_stdio(false);

# int n;
# cin >> n;
# long long a = 0;

# for (int i = 0; i < n; i++) {
# int v, d = 0;
# cin >> v;

# auto iter = m.lower_bound(v);

# if (iter != m.end())
# d = max(d, iter->second);

# if (iter != m.begin()) {
# iter--;
# d = max(d, iter->second);
# }
# m[v] = 1 + d;
# a += 1 + (long long)d;
# }
# cout << a << '\n';
# }

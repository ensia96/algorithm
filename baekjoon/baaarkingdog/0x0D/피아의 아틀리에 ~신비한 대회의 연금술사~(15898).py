import sys
import itertools as t
i, g = sys.stdin.readline, range
n, m = int(i()), [[[0, 0] for _ in g(5)] for _ in g(5)]
a, c = lambda: [i().split() for _ in g(4)], t.permutations(g(n), 3)
l = [[[[int(a[i][j]), {'R': 7, 'G': 3, 'B': 5, 'Y': 2, 'W': 0}[b[i][j]]] for i in range(4)]
      for j in range(4)] for a, b in [[a(), a()]for _ in g(n)]]


def r(m): return [[m[3-j][i] for j in g(4)] for i in g(4)]
def p(m): return sum(m[i][j][0] * m[i][j][1] for i in g(5) for j in g(5))
def d(m): return [[[a, b] for a, b in l] for l in m]


def s(a, b, c, m):
    i, j, k, e = l[a], l[b], l[c], 0
    for x in g(4):
        for aa, bb in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            u = f(i, d(m), aa, bb)
            for y in g(4):
                for cc, dd in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    v = f(j, d(u), cc, dd)
                    for z in g(4):
                        for ee, ff in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                            e = max(e, p(f(k, d(v), ee, ff)))
                        k = r(k)
                j = r(j)
        i = r(i)
    return e


def f(i, m, x, y):
    for a in g(4):
        for b in g(4):
            u, v = i[a][b]
            h, k = m[a+x][b+y]
            w = h+u
            m[a+x][b+y] = ([[w, 9][w > 9], 0][w < 0], [v, k][not v])
    return m


print(max(s(*i, m)for i in c))

# (시간 초과 때문에 아래 블로그에 올라온 C++ 코드 다듬어서 제출...)
# https://geniusjo-story.tistory.com/399

# #include <iostream>
# #include <algorithm>
# #include <vector>
# #include <utility>
# using namespace std;

# int n;
# pair<int, char> board[5][5];
# pair<int, char> material[10][4][4];
# int result = -987654321;

# void setup() {
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++) {
# board[i][j].first = 0;
# board[i][j].second = 'W';
# }
# }

# int cal() {
# int r = 0;
# int b = 0;
# int g = 0;
# int y = 0;
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++) {
# if (board[i][j].second == 'R')
# r += board[i][j].first;
# else if (board[i][j].second == 'B')
# b += board[i][j].first;
# else if (board[i][j].second == 'G')
# g += board[i][j].first;
# else if (board[i][j].second == 'Y')
# y += board[i][j].first;
# }
# return (7 * r) + (5 * b) + (3 * g) + (2 * y);
# }

# void fill(pair<int, int> position, int number) {
# for (int i = position.first; i < position.first + 4; i++)
# for (int j = position.second; j < position.second + 4; j++) {
# pair<int, char> current_location = board[i][j];

# current_location.first += material[number][i - position.first][j - position.second].first;

# if (current_location.first < 0)
# current_location.first = 0;
# else if (current_location.first > 9)
# current_location.first = 9;

# if (material[number][i - position.first][j - position.second].second != 'W')
# current_location.second = material[number][i - position.first][j - position.second].second;

# board[i][j] = current_location;
# }
# }

# void rotate(int number) {
# pair<int, char> dummy[4][4];

# for (int i = 0; i < 4; i++)
# for (int j = 0; j < 4; j++) {
# dummy[i][j] = material[number][3 - j][i];
# }

# for (int i = 0; i < 4; i++)
# for (int j = 0; j < 4; j++) {
# material[number][i][j] = dummy[i][j];
# }
# }

# void subs(vector<int> select, int index) {
# if (index == 3) {
# result = max(result, cal());
# return;
# }

# pair<int, char> copied[5][5];

# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++)
# copied[i][j] = board[i][j];

# for (int t = 0; t < 4; t++) {
# fill(make_pair(0, 0), select[index]);
# subs(select, index + 1);
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++)
# board[i][j] = copied[i][j];

# fill(make_pair(0, 1), select[index]);
# subs(select, index + 1);
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++)
# board[i][j] = copied[i][j];

# fill(make_pair(1, 0), select[index]);
# subs(select, index + 1);
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++)
# board[i][j] = copied[i][j];

# fill(make_pair(1, 1), select[index]);
# subs(select, index + 1);
# for (int i = 0; i < 5; i++)
# for (int j = 0; j < 5; j++)
# board[i][j] = copied[i][j];

# rotate(select[index]);
# }
# }

# void solve() {
# vector<int> perm;

# for (int i = 0; i < n; i++)
# perm.push_back(0);

# perm[0] = 1;
# perm[1] = 1;
# perm[2] = 1;

# sort(perm.begin(), perm.end());

# do {
# vector<int> select;
# for (int i = 0; i < perm.size(); i++) {
# if (perm[i] == 1)
# select.push_back(i);
# }
# sort(select.begin(), select.end());
# do {
# subs(select, 0);
# } while (next_permutation(select.begin(), select.end()));
# } while (next_permutation(perm.begin(), perm.end()));
# }

# int main() {
# cin.tie(NULL);
# ios_base::sync_with_stdio(false);

# setup();
# cin >> n;

# for (int i = 0; i < n; i++) {
# for (int j = 0; j < 4; j++)
# for (int k = 0; k < 4; k++) {
# int input;
# cin >> input;

# material[i][j][k].first = input;
# }

# for (int j = 0; j < 4; j++)
# for (int k = 0; k < 4; k++) {
# char input;
# cin >> input;

# material[i][j][k].second = input;
# }
# }

# solve();
# cout << result;

# return 0;
# }

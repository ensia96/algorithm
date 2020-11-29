#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> arr; // C++ 에선 벡터 라이브러리를 사용

int main(void) {
	cin >> n;
	// 반복 작업을 위해 벡터 객체에 원소 삽입
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}
	// 벡터 객체의 요소들을 정렬
	sort(arr.begin(), arr.end());

	// 총 그룹의 수
	int result = 0;
	// 현재 그룹에 포함된 모험가의 수
	int cnt = 0;
	// 공포도를 낮은 것부터 하나씩 확인하며
	for (int i = 0; i < n; i++) {
		// 현재 그룹에 해당 모험가를 포함시키기
		cnt += 1
		// 모험가의 수가 현재의 공포도 이상이라면,
		if (cnt >= arr[i]) {
			// 그룹을 결성 (총 그룹의 수 증가시키기)
			result += 1;
			// 현재 그룹에 포함된 모험가의 수 초기화
			cnt = 0;
		}
	}
	// 총 그룹의 수 출력
	cout << result << '\n'
}
def merge_sort(l):
    if len(l) == 1:
        return l
    t = len(l)
    m = t//2
    a, b, c = merge_sort(l[:m]), merge_sort(l[m:]), []
    i = j = 0
    for _ in range(t):
        if j == t-m:
            c += [a[i]]
            i += 1
        elif i == m:
            c += [b[j]]
            j += 1
        elif a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c


print(merge_sort([3, 4, 1, 2, 3, 45, 1, 2, 3, 45, 7, 9, 6, 1]))
print(sorted([3, 4, 1, 2, 3, 45, 1, 2, 3, 45, 7, 9, 6, 1]))

# 다른 사람의 풀이를 보다가 인상 깊어서 가져온 코드
# 출처 : https://www.acmicpc.net/source/29188108


def merge_sort(arr):
    def sort(start, end):
        if end - start < 2:
            return arr
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        return merge(start, mid, end)

    def merge(start, mid, end):
        temp = []
        a = start
        b = mid
        while a < mid and b < end:
            if arr[a] < arr[b]:
                temp.append(arr[a])
                a += 1
            else:
                temp.append(arr[b])
                b += 1
        while a < mid:
            temp.append(arr[a])
            a += 1
        while b < end:
            temp.append(arr[b])
            b += 1
        for i in range(start, end):
            arr[i] = temp[i - start]
    return sort(0, len(arr))

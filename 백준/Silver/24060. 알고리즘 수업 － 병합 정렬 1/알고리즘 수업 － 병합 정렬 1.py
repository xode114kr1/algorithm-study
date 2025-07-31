def merge_sort(arr, start, end):
    global cnt, result
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    global cnt, result
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1

    # 여기서 진짜 저장이 이루어지므로, 이때 cnt 증가
    for t in range(len(temp)):
        arr[start + t] = temp[t]
        cnt += 1
        if cnt == k:
            result = temp[t]

# 입력 처리
n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
result = -1

merge_sort(arr, 0, n - 1)
print(result)

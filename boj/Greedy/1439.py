'''
입력  => 정답, 숫자가 바뀌는 횟수
0, 1 => 0, 0
01, 10 => 1, 1
010, 101 => 1, 2
0101, 1010 => 2, 3
01010, 10101 => 2, 4


정답 = (숫자가 바뀌는 횟수 + 1) / 2


'''
S = input()

cnt = 0

for i in range(0, len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1

print((cnt+1)//2)

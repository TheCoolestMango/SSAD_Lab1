s = input().upper()
for i in reversed(s):
    print(ord(i) - ord('A') + 1, end=' ')

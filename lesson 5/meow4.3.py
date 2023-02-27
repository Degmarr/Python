n = int(input())
s = 0
for i in range(0, n):
    if i%3 == 0:
        s = s + 3
        print(s)
    i = i + 1    
print(s)    
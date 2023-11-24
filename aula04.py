N = int(input())
LA, LB = map(int, input().split())
SA, SB = map(int, input().split())

if LA <= N <= LB and SA <= N <= SB:
    print("possivel")
else:
    print("impossivel")
h, w = map(int, input().split())
ground = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    left_max = max(ground[:i])
    right_max = max(ground[i+1:])
    
    compare = min(left_max, right_max)
    
    if ground[i] < compare:
        ans += compare - ground[i]
        
print(ans)

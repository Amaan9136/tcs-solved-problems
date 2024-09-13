def zero_count(L, K):
    if K == 0: 
        return L
    if K == L: 
        return 0
    
    zeros = L - K
    gaps = K + 1
    min_zeros_per_gap = zeros // gaps
    extra_zeros = zeros % gaps
    if extra_zeros > 0:
        return min_zeros_per_gap + 1
    else:
        return min_zeros_per_gap

# Input
L, K = map(int, input().split())

# Output
print(zero_count(L, K))

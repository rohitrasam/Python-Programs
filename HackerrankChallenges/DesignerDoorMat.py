n, m = map(int, input().split())
pattern = []
for i in range(n // 2):
    pattern.append(('.|.'*(2*i + 1)).center(m, '-'))
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
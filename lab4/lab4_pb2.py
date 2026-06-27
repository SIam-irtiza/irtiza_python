from collections import Counter
d = {'A': 10, 'B': 20, 'C': 10, 'D': 30, 'E': 20, 'F': 10}
result = Counter(d.values())
print(result)
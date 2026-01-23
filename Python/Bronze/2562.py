num = [int(input()) for _ in range(9)]

max_val = num[0]
max_idx = 0

for i in range(len(num)):
	if num[i] > max_val:
		max_val = num[i]
		max_idx = i

print(max_val)
print(max_idx + 1)
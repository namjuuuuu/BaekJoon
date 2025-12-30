H, M = map(int, input().split())

if M < 45:
	H -= 1
	M += 60
	if H < 0:
		H = 23
	M -= 45 //이 줄 역시 첫 번째 if문 구조 안에 있음. -> 두 번째 if문을 수행하지 않더라도 이 줄은 수행해야 함.
else:
	M -= 45

print(H, M)
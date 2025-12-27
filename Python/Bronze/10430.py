A, B, C = map(int, input().split())

print(f"{(A + B) % C}\n"
f"{((A % C) + (B % C)) % C}\n"
f"{(A B) % C}\n"
f"{((A % C) (B % C)) % C}")
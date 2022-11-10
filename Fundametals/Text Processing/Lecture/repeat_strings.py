text = input().split()
final_result = []

for word in text:
    final_result.append(word * len(word))

print(*final_result, sep="")
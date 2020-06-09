numbers = []
for i in range(1000_000, 10_000_000):
    word = str(i)
    if not '0' in word:
        numbers.append(i)
    if not '7' in word:
        numbers.append(i)
    if not '8' in word:
        numbers.append(i)
    if not '9' in word:
        numbers.append(i)

print(numbers[21358])
        
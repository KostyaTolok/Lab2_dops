data = input()

count = {}
words = data.replace(',', '').replace('.', '').replace(':', '').lower().split(" ")
for w in words:
    if w in count.keys():
        count[w] += 1
    else:
        count[w] = 1
print(count)
sentences = data[:-1].split('.')
count_in_sent = []

for sent in sentences:
    count_in_sent.append(len(sent.split()))

print(count_in_sent)

n = len(count_in_sent)
print(f"Среднее: {sum(count_in_sent) / n}")

med = (count_in_sent[n // 2] + count_in_sent[-n // 2]) / 2
print(f"Медианное: {med}")

n = int(input("Введите n"))
k = int(input("Введите k"))

ngrams = zip(*[words[:i] for i in range(n)])
ngrams = [" ".join(ngram) for ngram in ngrams]

print(ngrams)
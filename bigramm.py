text = "I love natural language processing. I love programming."
tokens = text.split()
bigram_counts = {}

for i in range(len(tokens) - 1):
    bigram = (tokens[i], tokens[i + 1])
    if bigram not in bigram_counts:
        bigram_counts[bigram] = 0
    bigram_counts[bigram] += 1

print("Bigram Combinations and Frequencies:")
for bigram, count in bigram_counts.items():
    print(f"{bigram}: {count}")

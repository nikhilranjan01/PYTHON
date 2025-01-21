text = "I love natural language processing. I love programming."
tokens = text.split()
bigram_counts = {}

for i in range(len(tokens) - 1):
    bigram = (tokens[i], tokens[i + 1])
    if bigram not in bigram_counts:
        bigram_counts[bigram] = 0
    bigram_counts[bigram] += 1

bigram_probs = {}
total_bigrams = sum(bigram_counts.values())
for bigram, count in bigram_counts.items():
    bigram_probs[bigram] = count / total_bigrams

print("Bigram Probabilities:")
for bigram, prob in bigram_probs.items():
    print(f"P({bigram[1]} | {bigram[0]}) = {prob:.3f}")

words_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    words_to_count[word] = words_to_count.get(word, 0) + 1

words = list(words_to_count.keys())
words.sort()
max_len = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, max_len, words_to_count[word]))
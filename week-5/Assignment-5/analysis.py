import string

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = 0
word_frequency = {}

for line in lines:
    line = line.lower()
    for symbol in string.punctuation:
        line = line.replace(symbol, "")

    words = line.split()
    total_words += len(words)

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

with open("analysis.txt", "w", encoding="utf-8") as result:
    result.write("Text File Analysis\n")
    result.write("Total lines: " + str(total_lines) + "\n")
    result.write("Total words: " + str(total_words) + "\n")
    result.write("\nWord frequency:\n")

    for word in word_frequency:
        result.write(word + ": " + str(word_frequency[word]) + "\n")

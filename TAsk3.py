import matplotlib.pyplot as plt

vowels = "aeiouAEIOU"

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

freq = {v: 0 for v in "aeiou"}

for ch in text:
    if ch.lower() in freq:
        freq[ch.lower()] += 1

letters = list(freq.keys())
values = list(freq.values())

plt.figure(figsize=(7, 5))
plt.bar(letters, values)
plt.title("Гістограма частоти появи голосних літер")
plt.xlabel("Літера")
plt.ylabel("Кількість повторів")

plt.savefig("histogram.png", dpi=200)
plt.close()

print("Гістограму збережено у файлі histogram.png")

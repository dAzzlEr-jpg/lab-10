with open("aaaaaa.txt", "w", encoding="utf-8") as f:
    for i in range(1, 9 + 1):
        f.write("a" * i + "\n")

print("Файл 'aaaaaa.txt' був успішно кріейтед!")

lst = ["1.txt.txt", "2.txt.txt", "3.txt.txt"]
result = []
for file in lst:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()  # получаем все строки из файла
        file_data = [line.strip() for line in lines]  # удаляем символы переноса строки
        result.append((file, len(file_data), file_data))
sorted_result = sorted(result, key=lambda x: x[1])
with open("4.txt.txt", "w", encoding="utf-8") as f:
    i = ""
    for item in sorted_result:
        i += "\n"
        i += str(item[0])
        i += "\n"
        i += str(item[1])
        i += "\n"
        for line in item[2]:
            i += line
            i += "\n"
    f.write(i)








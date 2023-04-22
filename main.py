import json
keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}

with open('file1.txt', encoding='utf-8') as text:
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)

    for name in lines:
        cook_book[name] = []
        num = next(lines)

        for _ in range(int(num)):
            sostav_line = next(lines)
            ingrid = sostav_line.split(' | ')
            ingredients = {'ingredient_name': ingrid[0], 'quantity': int(ingrid[1]), 'measure': ingrid[2]}
            cook_book[name].append(ingredients)
            continue

        continue
print(json.dumps(cook_book, indent=2, ensure_ascii=False))


def list_of_stores_with_ingredients(dishes, person_count, cook_book):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                          'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result


person_count = 3
dishes = ['Омлет', 'Фахитос', 'Сельдь под шубой', 'Запеченный картофель']

print(json.dumps(cook_book, indent=2, ensure_ascii=False))
print()
print(list_of_stores_with_ingredients(dishes, person_count, cook_book))


#Task_3

file_for_writing = []
sum_line = {}
with open('1.txt', 'rt', encoding='utf-8') as f_1:
    sum_line_1 = {}
    file_1_oneline = []
    counting_1 = 0
    for line in f_1.readlines():
        file_1_oneline.append(line)
        counting_1 += 1
    sum_line[counting_1] = file_1_oneline

with open('2.txt', 'rt', encoding='utf-8') as f_2:
    sum_line_2 = {}
    file_2_oneline = []
    counting_2 = 0
    for line in f_2.readlines():
        file_2_oneline.append(line)
        counting_2 += 1
    sum_line[counting_2] = file_2_oneline

with open('3.txt', 'rt', encoding='utf-8') as f_3:
    sum_line_3 = {}
    file_3_oneline = []
    counting_3 = 0
    for line in f_3.readlines():
        file_3_oneline.append(line)
        counting_3 += 1
    sum_line[counting_3] = file_3_oneline

sorted_keys = sorted(sum_line.keys())
sorted_sum_line = {}
for i in sorted_keys:
    sorted_sum_line[i] = sum_line[i]

for line in sorted_sum_line.values():
    file_for_writing += line
print(file_for_writing)

with open('file_finish.txt', 'x') as f:
    f.writelines(file_for_writing)

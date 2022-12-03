with open('input/input01.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
elf_calories = {}
elf_number = 1
calories_sum = 0
for line in lines:
    if line == '':
        elf_number += 1
        calories_sum = 0
    else:
        if not elf_number in elf_calories:
            elf_calories[elf_number] = 0
        elf_calories[elf_number] = elf_calories[elf_number] + int(line)

elf_with_most_calories = max(elf_calories, key=elf_calories.get)
most_calories = elf_calories[elf_with_most_calories]

print('Answer 1: ', most_calories)


# part two
sorted_elf_calories = dict(sorted(elf_calories.items(), key=lambda item: item[1], reverse=True))
top_three_calories = list(sorted_elf_calories.values())[:3]
sum_top_three_calories = sum(top_three_calories)

print('Answer 2: ', sum_top_three_calories)

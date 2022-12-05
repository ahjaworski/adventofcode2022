with open('input/input04.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
count_first = 0
count_second = 0
for line in lines:
    first = line.split(',')[0]
    first_start = int(first.split('-')[0])
    first_end = int(first.split('-')[1])
    second = line.split(',')[1]
    second_start = int(second.split('-')[0])
    second_end = int(second.split('-')[1])

    if (first_start <= second_start and first_end >= second_end) or (
            first_start >= second_start and first_end <= second_end):
        count_first += 1

    if (second_start <= first_start <= second_end) or (second_start <= first_end <= second_end) or (
            first_start <= second_start <= first_end) or (first_start <= second_end <= first_end):
        count_second += 1

print('Answer 1: ', count_first)

print('Answer 2: ', count_second)

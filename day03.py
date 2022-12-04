with open('input/input03.txt') as f:
    lines = [i.strip() for i in f.readlines()]


# part one

def find_shared_item(line):
    first, second = line[:len(line) // 2], line[len(line) // 2:]
    for item in first:
        if item in second:
            return item


def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96


sum_priorities = 0
for game_line in lines:
    shared_item = find_shared_item(game_line)
    priority = get_priority(shared_item)
    sum_priorities += priority

print('Answer 1: ', sum_priorities)


def find_shared_item_three_elves(line1, line2, line3):
    for item in line1:
        if item in line2 and item in line3:
            return item

sum_priorities_three = 0
i = 0
while i < len(lines):
    shared_item = find_shared_item_three_elves(lines[i], lines[i+1], lines[i+2])
    priority = get_priority(shared_item)
    sum_priorities_three += priority
    i += 3

print('Answer 2: ', sum_priorities_three)

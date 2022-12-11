def priority(s: str) -> int:
    return ord(s) - ord('A') + 27 if s.isupper() else ord(s) - ord('a') + 1

# Part 1
# print(sum(priority(priority_item) for line in open('input.txt').read().strip().splitlines() for priority_item in set(line[:int(len(line)/2)]).intersection(set(line[int(len(line)/2):]))))

# Part 2
elves = open('input.txt').read().strip().splitlines()
print(sum(priority(common_item) for batch_idx in range(len(elves) // 3) for common_item in set(elves[batch_idx * 3]).intersection(set(elves[batch_idx * 3 + 1])).intersection(set(elves[batch_idx * 3 + 2]))))

# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(list(f"priority for {char} is {priority(char)}" for char in chars))

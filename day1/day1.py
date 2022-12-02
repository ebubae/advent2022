print("part 1:", max(sum(map(int, elf.split("\n"))) for elf in open("input.txt").read().strip().split("\n\n")))
print("part 2:", sum(sorted((sum(map(int, elf.split("\n"))) for elf in open("input.txt").read().strip().split("\n\n")), reverse=True)[:3]))

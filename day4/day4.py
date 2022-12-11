# ngl this was a stack overflow cop
def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

def range_overlap(range1: range, range2: range):
    return range1.start in range2 or range1[-1] in range2 or range2.start in range1 or range2[-1] in range1

def make_range(range_str: str) -> range:
    start, end = range_str.split("-")
    return range(int(start), int(end) + 1)

# print(sum(range_subset(range1, range2) or range_subset(range2, range1) for range1, range2 in ((make_range(r1), make_range(r2))for r1, r2 in (line.split(",") for line in open('input.txt').read().strip().splitlines()))))
print(sum(range_overlap(range1, range2) for range1, range2 in ((make_range(r1), make_range(r2))for r1, r2 in (line.split(",") for line in open('input.txt').read().strip().splitlines()))))

use std::fs;

fn main() {
    let full_string = fs::read_to_string("input.txt").unwrap();
    let result = full_string
        .trim()
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|elf_item| elf_item.parse::<i32>().unwrap())
                .sum()
        })
        // .flatten()
        .max()
        .unwrap_or(0);
    println!("part 1: {:?}", result);
    let result2 = full_string.trim();
    println!("part 2: {:?}", result2);
}

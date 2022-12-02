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
        .max()
        .unwrap_or(0);
    println!("part 1: {:?}", result);
    let mut tops = full_string
        .trim()
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|elf_item| elf_item.parse::<i32>().unwrap())
                .sum()
        })
        .collect::<Vec<i32>>();
    tops.sort();
    tops.reverse();
    if let Some(slice) = tops.get(0..3) {
        println!("part 2: {:?}", slice.iter().sum::<i32>());
    }
}

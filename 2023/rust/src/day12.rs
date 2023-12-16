use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u64 = 0;
    let mut str_arr: Vec<&str> = input_lines[0].split_whitespace().collect(); 
    println!("{:?}",str_arr);

}

fn solve_part2(input_lines: &Vec<String>){

}
pub fn solve() {
    let input = read_input("input/input_day12.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    solve_part1(&input_lines);
    solve_part2(&input_lines);
}

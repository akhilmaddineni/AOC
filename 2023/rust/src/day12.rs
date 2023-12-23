use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u64 = 0;
    for input_line in input_lines{
        let mut str_arr: Vec<&str> = input_line.split_whitespace().collect(); 
        println!("{:?}",str_arr);
        let mut char_array: Vec<_> = str_arr[0].chars().collect(); 
        let mut seq: Vec<u16> = Vec::new();
        let mut temp_str: Vec<_> = str_arr[1].split(",").collect();
        for ele in temp_str {
            seq.push(ele.parse::<u16>().unwrap());
        }
        println!("{:?}",char_array);
        println!("{:?}",seq);
        ans += solve(&char_array,&seq,0,0);
    }
    

}

fn solve_part2(input_lines: &Vec<String>){

}
pub fn solve() {
    let input = read_input("input/input_day12.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    solve_part1(&input_lines);
    solve_part2(&input_lines);
}

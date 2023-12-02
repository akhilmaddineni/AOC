use std::fs;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn caluculate_calibration(calibration_str: &str) -> u8 {
    let mut left: u8 = 0 ; 
    let mut right: u8 = 0 ; 
    for (_i, c) in calibration_str.chars().enumerate() {
        if c.is_ascii_digit() {
            if left == 0 {
                left = (c as u32 - '0' as u32 ) as u8 ; //TODO : how to properly write this 
            }
            right = (c as u32 - '0' as u32 ) as u8 ; 
        }
    }
    //return
    left*10+right
}

fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u64 = 0;
    for item in input_lines
    {
        let ans_line: u8 = caluculate_calibration(&item);
        ans = ans+ans_line as u64;
    }
    println!("answer part1 : {}",ans);
}

fn solve_part2(input_lines: Vec<String>) {
    let mut ans: u64 = 0;

    //two ways : hack the replace string with weird strings to account for overlap 
    //TODO: find and track the indexes of all substrings and replace first and last 
    for mut item in input_lines
    {
        item = item.replace("zero", "zer0o"); 
        item = item.replace("one", "o1ne");
        item = item.replace("two", "tw2o");
        item = item.replace("three", "t3hree");
        item = item.replace("four", "f4our");
        item = item.replace("five","f5ive");
        item = item.replace("six","s6ix");
        item = item.replace("seven","s7even");
        item = item.replace("eight","ei8ght");
        item = item.replace("nine","ni9ne");
        let ans_line: u8;
        ans_line = caluculate_calibration(&item);
        ans = ans+ans_line as u64;
    }
    println!("answer part2 : {}",ans);
}


pub fn solve() {
    let input = read_input("input/input_day1.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    solve_part1(&input_lines);
    solve_part2(input_lines);
}

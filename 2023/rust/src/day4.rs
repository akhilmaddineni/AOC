use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u64 = 0; 
    for line in input_lines {
        let divide_line: Vec<&str> = line.split(":").collect();
        let game_info: Vec<&str> = divide_line[1].split("|").collect();
        let winning_num: Vec<&str> = game_info[0].trim().split_whitespace().collect();
        let current_num: Vec<&str> = game_info[1].trim().split_whitespace().collect();
        let mut num_matches: u64 = 0 ; 
        for each_num in winning_num {
            if current_num.contains(&each_num) {
                num_matches +=1;
            }
        }
        if num_matches >0 {
            ans += u64::pow(2,(num_matches-1).try_into().unwrap());
        }
    }
    println!("part1 ans {}",ans);
}

fn solve_part2(input_lines: &Vec<String>) {
    let mut ans: u64 = 0; 
    let num_cards: usize = input_lines.len();
    let mut freq_hash = vec![1; num_cards];
    for line_num in 0..num_cards {
        let divide_line: Vec<&str> = input_lines[line_num].split(":").collect();
        let game_info: Vec<&str> = divide_line[1].split("|").collect();
        let winning_num: Vec<&str> = game_info[0].trim().split_whitespace().collect();
        let current_num: Vec<&str> = game_info[1].trim().split_whitespace().collect();
        let mut num_matches: usize = 0 ; 
        for num_idx in 0..winning_num.len() {
            if current_num.contains(&winning_num[num_idx]) {
                num_matches += 1; 
            }
        }
        if num_matches > 0
        {
            for idx in (line_num+1)..(line_num+num_matches+1)
            {
                if idx >= num_cards {
                    break;
                }
                else {
                    freq_hash[idx] += 1;
                    freq_hash[idx] += freq_hash[line_num]-1;
                }
            }
        }

    }
    for idx in 0..num_cards {
        ans += freq_hash[idx];
    }
    println!("part2 ans {}",ans);
}


pub fn solve() {
    let input = read_input("input/input_day4.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);

    solve_part1(&input_lines);
    solve_part2(&input_lines);
}

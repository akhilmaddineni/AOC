use std::fs;
use regex::Regex;
use std::collections::HashMap;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a.abs()
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: i64, b: i64) -> i64 {
    (a / gcd(a, b)) * b
}

fn solve_part1(desert_map: &HashMap<&str,(&str,&str)>, instructions: &str) {
    let mut cur_point: &str = "AAA" ; 
    let inst_len = instructions.len(); 
    let mut ans = 0; 
    while cur_point != "ZZZ" {
        let idx : usize = ans as usize %inst_len;
        if instructions.chars().nth(idx) == Some('L') {
            cur_point = desert_map[cur_point].0;
        }
        else {
            cur_point = desert_map[cur_point].1;
        }
        ans +=1;
    }
    println!("Part1 ans : {}",ans);
}

fn solve_part2(desert_map: &HashMap<&str,(&str,&str)>, instructions: &str) {
    //start at **A and shoudl end at **Z
    let mut cur_point: Vec<&str> = Vec::new() ; 
    for each_key in desert_map.keys(){
        if each_key.chars().last() == Some('A') {
            cur_point.push(each_key);
        }
    }
    let inst_len = instructions.len(); 
    let mut ans = 1;  
    for cur_point_idx in 0..cur_point.len() {
        let mut steps = 0; 
        while cur_point[cur_point_idx].chars().last() != Some('Z'){
            let idx : usize = steps as usize %inst_len;
            if instructions.chars().nth(idx) == Some('L') {
                cur_point[cur_point_idx] = desert_map[cur_point[cur_point_idx]].0;
            }
            else {
                cur_point[cur_point_idx] = desert_map[cur_point[cur_point_idx]].1;
            }
            steps +=1;
        }
        ans = lcm(ans,steps);
    }
    println!("Part2 ans : {}",ans);
}




pub fn solve() {
    let input = read_input("input/input_day8.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    let instructions:  String = input_lines[0].clone(); 
    //create map 
    let mut desert_map: HashMap<&str,(&str,&str)> = HashMap::new();
    for each_line in &input_lines {
        let re = Regex::new(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)").unwrap();
        if let Some(map_index) = re.captures(&each_line) {
            // Inserting into HashMap
            desert_map.insert(
                map_index.get(1).map_or("", |m| m.as_str()),
                (
                    map_index.get(2).map_or("", |m| m.as_str()),
                    map_index.get(3).map_or("", |m| m.as_str())
                )
            );
        } else {
            println!("No match found");
        }
    }
    println!("{:?}",desert_map);
    solve_part1(&desert_map,&instructions);
    solve_part2(&desert_map,&instructions);
}

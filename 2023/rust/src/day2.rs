use std::collections::HashMap;

use std::fs;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}


fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u16 = 0;
    let num_cubes_map = HashMap::from([
        ("red",12),
        ("green",13),
        ("blue",14)
    ]);
    //Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in input_lines {
        let divide_line: Vec<&str> = line.split(":").collect();
        let game_num = divide_line[0].replace("Game ","").trim().parse::<u16>().unwrap();
        let game_info: Vec<&str> = divide_line[1].split(";").collect();
        let mut flag: bool = true;
        for each_game in game_info {
            let cube_info: Vec<&str> = each_game.split(",").collect();
            for mut cube in cube_info {
                cube = cube.trim();
                let cube_data: Vec<&str> = cube.split(" ").collect();
                let num_cubes: u16 = cube_data[0].parse::<u16>().unwrap();
                //println!("{}",num_cubes);
                if num_cubes > *num_cubes_map.get(&cube_data[1]).unwrap() 
                {
                    flag = false;
                }
                if !flag {
                    break;
                }
            }
            if !flag {
                break;
            }
        }
        if flag {
            ans = ans+game_num;
        }
    }
    println!("part1 result : {}",ans);
}

fn solve_part2(input_lines: Vec<String>) {
    let mut ans: u64 = 0;
    
    //Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in input_lines {
        let mut num_cubes_map = HashMap::from([
            ("red",0),
            ("green",0),
            ("blue",0)
        ]);
        let divide_line: Vec<&str> = line.split(":").collect();
        let game_info: Vec<&str> = divide_line[1].split(";").collect();
        for each_game in game_info {
            let cube_info: Vec<&str> = each_game.split(",").collect();
            for mut cube in cube_info {
                cube = cube.trim();
                let cube_data: Vec<&str> = cube.split(" ").collect();
                let num_cubes: u16 = cube_data[0].parse::<u16>().unwrap();
                //println!("{}",num_cubes);
                if num_cubes > *num_cubes_map.get(&cube_data[1]).unwrap() 
                {
                    num_cubes_map.insert(&cube_data[1],num_cubes);
                }
            }
        }
        let mut ans_row: u64 = 1;
        for value in num_cubes_map.values() {
            ans_row *= *value as u64 ;
        }
        ans += ans_row;
    }
    println!("part2 result : {}",ans);
}


pub fn solve() {
    let input = read_input("input/input_day2.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    solve_part1(&input_lines);
    solve_part2(input_lines);
}

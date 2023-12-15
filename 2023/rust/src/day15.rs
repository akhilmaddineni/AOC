use std::fs;
use std::collections::HashMap;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(input_lines: &Vec<String>) {
    let mut ans: u64 = 0;
    let mut str_arr: Vec<&str> = input_lines[0].split(",").collect(); 
    println!("input {:?}",str_arr);
    for each_str in &str_arr {
        let mut ans_hash: u32 = 0;
        for (_i,each_char) in each_str.chars().enumerate() {
            ans_hash += each_char as u32 ; 
            ans_hash *= 17;
            ans_hash %= 256 ;
        }
        ans += ans_hash as u64;
    }
    println!("part1 ans {}",ans);
}

fn solve_part2(input_lines: &Vec<String>) {
    let mut ans: u32 = 0;
    let mut str_arr: Vec<&str> = input_lines[0].split(",").collect(); 
    //println!("input {:?}",str_arr);
    let mut focal_len_hash: HashMap<u32,Vec<(&str,u8)>> = HashMap::new();
    for each_str in &str_arr {
        let mut ans_hash: u32 = 0;
        let mut focal_len = 0;
        let str_len = each_str.len();
        for (i,each_char) in each_str.chars().enumerate() {
            if i<str_len-1 && each_char != '-' && each_char != '='{
                ans_hash += each_char as u32 ; 
                ans_hash *= 17;
                ans_hash %= 256 ;
            }
            if each_char.is_digit(10){
                //println!("digit : {}",each_char);
                if let Some(digit) = each_char.to_digit(10) {
                    focal_len = digit;
                }
                else {
                    println!("not numeric");
                }
            }
        }

        if let Some(values) = focal_len_hash.get_mut(&ans_hash) {
            if focal_len != 0 {
                //check if entry is already present 
                let mut present: bool = false ; 
                for i in 0..values.len() {
                    if values[i].0 == &each_str[0..str_len - 2]{
                        values[i] = (&each_str[0..str_len-2],focal_len.try_into().unwrap()); 
                        present = true;
                        break;
                    }
                }
                if !present {
                    values.push((&each_str[0..str_len-2],focal_len.try_into().unwrap()));
                }
                
            }
            else {

                for i in 0..values.len() {
                    if values[i].0 == &each_str[0..str_len - 1] {
                        values.remove(i);
                        break;
                    }
                }

                //println!("values : {:?}",values);
            }
            
        } else {
            // Key does not exist, so insert a new key-value pair
            if focal_len != 0 {
                focal_len_hash.insert(ans_hash, vec![(&each_str[0..str_len-2],focal_len.try_into().unwrap())]);
            }
            
        }
       // println!("focal len hash : {:?}",focal_len_hash);

    }

    for (key,each_box) in focal_len_hash {
        for i in 0..each_box.len() {
            ans += (key+1)*(i as u32+1)*(each_box[i].1 as u32);
        }
    }
    println!("answer part2 : {}",ans);

}


pub fn solve() {
    let input = read_input("input/input_day15.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    solve_part1(&input_lines);
    solve_part2(&input_lines);
}

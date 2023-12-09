use std::fs;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part(sensor_val_arr: &Vec<Vec<i64>>) {
    let mut ans_part1: i64 = 0; 
    let mut ans_part2: i64 = 0; 
    //find next value of each ele 
    for sensor_history in sensor_val_arr {
        let mut sensor_diff_arr: Vec<Vec<i64>> = Vec::new(); 
        let mut flag: bool = false ; 
        let mut predicted_val: i64 = 0;
        let mut predicted_prev_val: i64 = 0;
        sensor_diff_arr.push(sensor_history.clone());

        while !flag {
            let mut next_diff_arr: Vec<i64> = Vec::new(); 
            let last_arr = sensor_diff_arr.last().unwrap().clone() ; 
            for i in 0..last_arr.len()-1 {
                next_diff_arr.push((last_arr[i+1]-last_arr[i]));
            }
            sensor_diff_arr.push(next_diff_arr.clone());
            if next_diff_arr.iter().all(|&x| x == 0) {
                flag = true;
            }
        }
        println!("{:?}",sensor_diff_arr);
        for each_ele in &sensor_diff_arr {
            predicted_val += each_ele.last().unwrap(); 
        }
        for each_ele in sensor_diff_arr.iter().rev() {
            predicted_prev_val = each_ele[0]-predicted_prev_val;
        }
        println!("predicted val {}",predicted_val);
        println!("predicted prev val {}",predicted_prev_val);
        ans_part1 += predicted_val;
        ans_part2 += predicted_prev_val;
    }
    println!("part1 ans {}" , ans_part1);
    println!("part2 ans {}" , ans_part2);
}




pub fn solve() {
    let input = read_input("input/input_day9.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    //assuming strictly increasing diff

    let mut sensor_val_arr: Vec<Vec<i64>> = Vec::new() ; 
    for each_line in &input_lines {
        let mut temp_line: Vec<i64> = Vec::new(); 
        let temp_line_str: Vec<&str> = each_line.trim().split_whitespace().collect(); 
        for each_num in temp_line_str {
            temp_line.push(each_num.parse::<i64>().unwrap());
        }
        sensor_val_arr.push(temp_line);
    }
    println!("{:?}",sensor_val_arr);

    solve_part(&sensor_val_arr);
}

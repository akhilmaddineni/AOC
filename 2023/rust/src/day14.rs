use std::fs;
use std::collections::HashMap;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(matrix_input: &Vec<Vec<char>>) {
    let mut ans: u32 = 0;
    let mut matrix = matrix_input.clone();
    let mut change = true;
    while change {
        change = false;
        for i in 0..matrix.len()-1{
            for j in 0..matrix[0].len(){
                if matrix[i][j] == 'O' && matrix[i+1][j] == '.' {
                    matrix[i][j] = '.';
                    matrix[i+1][j] = 'O' ;
                    change = true;
                }
            }
        }
    }
    
    //println!("updated matrix {:?}",matrix);
    for i in 0..matrix.len(){
        let mut num_zero: u32 = 0;
        for j in 0..matrix[0].len(){
            if matrix[i][j] == 'O' {
                num_zero+=1;
            }
        }
        ans += (i as u32 +1)*num_zero; 
    }


    println!("part 1 ans : {}",ans);
}

fn tilt_north(matrix: &mut Vec<Vec<char>>){
    let mut change = true;
    while change {
        change = false;
        for i in 0..matrix.len()-1{
            for j in 0..matrix[0].len(){
                if matrix[i][j] == 'O' && matrix[i+1][j] == '.' {
                    matrix[i][j] = '.';
                    matrix[i+1][j] = 'O' ;
                    change = true;
                }
            }
        }
    }
}

fn tilt_south(matrix: &mut Vec<Vec<char>>){
    let mut change = true;
    while change {
        change = false;
        for i in (1..matrix.len()).rev(){
            for j in 0..matrix[0].len(){
                if matrix[i][j] == 'O' && matrix[i-1][j] == '.' {
                    matrix[i][j] = '.';
                    matrix[i-1][j] = 'O' ;
                    change = true;
                }
            }
        }
    }
}

fn tilt_west(matrix: &mut Vec<Vec<char>>){
    let mut change = true;
    while change {
        change = false;
        for i in 0..matrix.len(){
            for j in 1..matrix[0].len(){
                if matrix[i][j] == 'O' && matrix[i][j-1] == '.' {
                    matrix[i][j] = '.';
                    matrix[i][j-1] = 'O' ;
                    change = true;
                }
            }
        }
    }
}

fn tilt_east(matrix: &mut Vec<Vec<char>>){
    let mut change = true;
    while change {
        change = false;
        for i in 0..matrix.len(){
            for j in 0..matrix[0].len()-1{
                if matrix[i][j] == 'O' && matrix[i][j+1] == '.' {
                    matrix[i][j] = '.';
                    matrix[i][j+1] = 'O' ;
                    change = true;
                }
            }
        }
    }
}


fn solve_part2(matrix_input: &Vec<Vec<char>>) {
    let mut ans: u32 = 0;
    let mut matrix = matrix_input.clone();
    let mut find_cycle = false ;
    let mut cycle_len = 0; 
    let mut seen_hash: HashMap<Vec<Vec<char>>,u32> = HashMap::new();
    seen_hash.insert(matrix.clone(),cycle_len);
    while true {
        //println!("{}",cycle_len);
        tilt_north(&mut matrix);
        tilt_west(&mut matrix);
        tilt_south(&mut matrix);
        tilt_east(&mut matrix);
        cycle_len += 1;
        if seen_hash.contains_key(&matrix){
            find_cycle= true;
            break;
        }
        else {
            seen_hash.insert(matrix.clone(),cycle_len);
        }
    }
    println!("cycle_len : {}",cycle_len);
    println!("repeated at : {}",seen_hash.get(&matrix).unwrap());

    // println!("{:?}",matrix);

    // remaining cycles 
    let mut remaining = (1000000000-seen_hash.get(&matrix).unwrap())%(cycle_len-seen_hash.get(&matrix).unwrap()); 
    println!("remaining cycles : {}",remaining);
    while remaining > 0 {
        tilt_north(&mut matrix);
        tilt_west(&mut matrix);
        tilt_south(&mut matrix);
        tilt_east(&mut matrix);
        remaining -= 1;
    }

    for i in 0..matrix.len(){
        let mut num_zero: u32 = 0;
        for j in 0..matrix[0].len(){
            if matrix[i][j] == 'O' {
                num_zero+=1;
            }
        }
        ans += (i as u32 +1)*num_zero; 
    }
    println!("part2 ans : {}",ans);
}

pub fn solve() {
    let input = read_input("input/input_day14.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    let mut matrix: Vec<Vec<char>> = Vec::new(); 

    for i in 0..input_lines.len() {
        //append to start for easy processing
        matrix.insert(0,input_lines[i].chars().collect::<Vec<_>>().clone());
    }
    println!("{:?}",matrix);

    solve_part1(&matrix); 
    solve_part2(&matrix);
}

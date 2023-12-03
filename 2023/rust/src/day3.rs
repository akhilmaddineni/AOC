use std::fs;
use std::collections::HashMap;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(number_map: &Vec<Vec<char>>) {
    //println!("{:?}",number_map);
    let row_limit = number_map.len() ;
    let col_limit = number_map[0].len(); 
    let mut ans: u64 = 0 ; 
    for row in 0..row_limit 
    {
        let mut valid = false;
        let mut num: u32 = 0;
        for col in 0..col_limit
        {
            if '0' <= number_map[row][col] && number_map[row][col] <= '9' {
                num = num*10 + number_map[row][col] as u32 - '0' as u32 ; 

                //check for validity 
                //-1,+1 -1,0 -1,-1 0,1 0,0 0,-1 1,1 1,0 1,-1 
                // Check up
                if !valid {
                if row > 0 && number_map[row - 1][col] != '.' && !number_map[row-1][col].is_ascii_digit(){
                    //println!("symblol found up {} {}",row,col);
                    valid = true;
                }

                // Check down
                if row < row_limit - 1 && number_map[row + 1][col] != '.'&& !number_map[row+1][col].is_ascii_digit() {
                    //println!("symblol found down {} {}",row,col);
                    valid = true;
                }

                // Check left
                if col > 0 && number_map[row][col - 1] != '.' && !number_map[row][col - 1].is_ascii_digit(){
                    //println!("symblol found left {} {}",row,col);
                    valid = true;
                }

                // Check right
                if col < col_limit - 1 && number_map[row][col + 1] != '.' && !number_map[row][col + 1].is_ascii_digit(){
                    //println!("symblol found right {} {}",row,col);
                    valid = true;
                }

                // Check top-left diagonal
                if row > 0 && col > 0 && number_map[row - 1][col - 1] != '.'&& !number_map[row-1][col - 1].is_ascii_digit() {
                    //println!("symblol found top left {} {}",row,col);
                    valid = true;
                }

                // Check top-right diagonal
                if row > 0 && col < col_limit - 1 && number_map[row - 1][col + 1] != '.'&& !number_map[row-1][col + 1].is_ascii_digit() {
                    //println!("symblol found top right {} {}",row,col);
                    valid = true;
                }

                // Check bottom-left diagonal
                if row < row_limit - 1 && col > 0 && number_map[row + 1][col - 1] != '.'&& !number_map[row+1][col - 1].is_ascii_digit() {
                    //println!("symblol found bot left {} {}",row,col);
                    valid = true;
                }

                // Check bottom-right diagonal
                if row < row_limit - 1 && col < col_limit - 1 && number_map[row + 1][col + 1] != '.' && !number_map[row+1][col + 1].is_ascii_digit() {
                    //println!("symblol found bot right {} {}",row,col);
                    valid = true;
                } 
            }/*if !valid */

            }/*if 48 <= number_map[row][col] as u16  <=57  */
            else {
                if valid 
                {
                    ans = ans + num as u64 ; 
                    //println!("valid number inner : {}",num);
                }
                valid = false;
                num = 0; 
            }
        }
        if valid
        {
            ans = ans + num as u64 ; 
            //println!("valid number : {}",num);
        }
    }
    println!("Part1 answer : {}",ans);


}

fn solve_part2(number_map: &Vec<Vec<char>>) {
    //println!("{:?}",number_map);
    let row_limit = number_map.len() ;
    let col_limit = number_map[0].len(); 
    let mut ans: u64 = 0 ; 
    let mut gear_point_hash: HashMap<(u16, u16), Vec<u32>> = HashMap::new(); 
    for row in 0..row_limit 
    {
        let mut number_processing = false; 
        let mut valid = false;
        let mut num: u32 = 0;
        let mut gear_point: (u16,u16) = (0,0);
        for col in 0..col_limit
        {
            if '0' <= number_map[row][col] && number_map[row][col] <= '9' {
                number_processing = true; 
                num = num*10 + number_map[row][col] as u32 - '0' as u32 ; 

                //check for validity 
                //-1,+1 -1,0 -1,-1 0,1 0,0 0,-1 1,1 1,0 1,-1 
                // Check up
                if !valid {
                if row > 0 && number_map[row - 1][col] == '*'{
                    //println!("symblol found up {} {}",row,col);
                    gear_point = ((row-1).try_into().unwrap(),col.try_into().unwrap());
                    valid = true;
                }

                // Check down
                if row < row_limit - 1 && number_map[row + 1][col] == '*' {
                    //println!("symblol found down {} {}",row,col);
                    gear_point = ((row+1).try_into().unwrap(),col.try_into().unwrap());
                    valid = true;
                }

                // Check left
                if col > 0 && number_map[row][col - 1] == '*'{
                    //println!("symblol found left {} {}",row,col);
                    gear_point = ((row).try_into().unwrap(),(col-1).try_into().unwrap());
                    valid = true;
                }

                // Check right
                if col < col_limit - 1 && number_map[row][col + 1] == '*' {
                    //println!("symblol found right {} {}",row,col);
                    gear_point = (row.try_into().unwrap(),(col+1).try_into().unwrap());
                    valid = true;
                }

                // Check top-left diagonal
                if row > 0 && col > 0 && number_map[row - 1][col - 1] == '*' {
                    //println!("symblol found top left {} {}",row,col);
                    gear_point = ((row-1).try_into().unwrap(),(col-1).try_into().unwrap());
                    valid = true;
                }

                // Check top-right diagonal
                if row > 0 && col < col_limit - 1 && number_map[row - 1][col + 1] == '*' {
                    //println!("symblol found top right {} {}",row,col);
                    gear_point = ((row-1).try_into().unwrap(),(col+1).try_into().unwrap());
                    valid = true;
                }

                // Check bottom-left diagonal
                if row < row_limit - 1 && col > 0 && number_map[row + 1][col - 1] == '*'{
                    //println!("symblol found bot left {} {}",row,col);
                    gear_point = ((row+1).try_into().unwrap(),(col-1).try_into().unwrap());
                    valid = true;
                }

                // Check bottom-right diagonal
                if row < row_limit - 1 && col < col_limit - 1 && number_map[row + 1][col + 1] == '*' {
                    //println!("symblol found bot right {} {}",row,col);
                    gear_point = ((row+1).try_into().unwrap(),(col+1).try_into().unwrap());
                    valid = true;
                } 
            }/*if !valid */

            }/*if 48 <= number_map[row][col] as u16  <=57  */
            else {
                if valid 
                {
                    if let Some(values) = gear_point_hash.get_mut(&gear_point) {
                        values.push(num);
                    } else {
                        // Key does not exist, so insert a new key-value pair
                        gear_point_hash.insert(gear_point, vec![num]);
                    }
                }
                number_processing = false;
                valid = false;
                num = 0; 
            }
        }
        if valid
        {
            if let Some(values) = gear_point_hash.get_mut(&gear_point) {
                values.push(num);
            } else {
                // Key does not exist, so insert a new key-value pair
                gear_point_hash.insert(gear_point, vec![num]);
            }
        }
    }
    println!("gear point hash : {:?}",gear_point_hash);
    for (each_key,each_val) in gear_point_hash {
        if each_val.len() > 1 {
            let mut ans_key = 1 ; 
            for each_num in each_val {
                ans_key *= each_num ;
            }
            ans += ans_key as u64 ;
        }
    }
    println!("Part2 answer : {}",ans);

}


pub fn solve() {
    let input = read_input("input/input_day3.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    println!("num lines : {} , size of line {}",input_lines.len(),input_lines[0].len());
    //declare 2d array
    let mut number_map = vec![vec![' '; input_lines[0].len()]; input_lines.len()];
    //fill number map 
    for row in 0..number_map.len() {
        number_map[row] = input_lines[row].chars().collect();
    }
    solve_part1(&number_map);
    solve_part2(&number_map);
}

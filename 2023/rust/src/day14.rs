use std::fs;

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
}

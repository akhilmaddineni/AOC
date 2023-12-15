use std::fs;
use std::collections::{HashMap, VecDeque};
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(matrix_vector: &Vec<Vec<Vec<char>>> ) {
    let mut ans: u32 = 0 ; 
    //check each matrix 
    for matrix in matrix_vector {
        println!("processing matrix : {:?}",matrix);
        let num_rows = matrix.len(); 
        let num_cols = matrix[0].len();
        //if odd number of rows or cols we may need to ignore one column at end to ignore for reflection 
        let mut found_reflection: bool = false ; 
        let mut row_idx_reflection = 0; 
        let mut col_idx_reflection = 0; 
        for col_idx in 1..matrix[0].len() {
            (found_reflection,col_idx_reflection) = check_col_reflection(&matrix,col_idx);
            if found_reflection {
                println!("found col reflection at test {}",col_idx_reflection);
                break;
            }
        }
        if found_reflection {
            ans += col_idx_reflection as u32;
            continue;
        }
        for row_idx in 1..matrix.len() {
            (found_reflection,row_idx_reflection) = check_row_reflection(&matrix,row_idx);
            if found_reflection {
                println!("found row reflection at test {}",row_idx_reflection);
                break;
            }
        }
        if found_reflection {
            ans += (row_idx_reflection as u32)*100;
            continue;
        }
        println!("no reflection!");
        std::process::exit(1);
    }
    println!("part 1 ans : {}",ans);
}

pub fn check_col_reflection(matrix: &Vec<Vec<char>>,col_start: usize)->(bool,usize) {
    //find start end and mid is col_start
    let mut start: usize = 0;
    let mut end: usize = matrix[0].len(); 
    //println!("inital col start : {} , start {} end {}",col_start,start,end);
    if col_start < end-col_start {
        end = 2*col_start ; 
    }
    else {
        start = 2*col_start-end;
    }
    //println!("col start : {} , start {} end {}",col_start,start,end);
    for i in 0..matrix.len() {
        for j in start..col_start{
            //println!("process row : {:?} idx : {}",matrix[i],i);
            if matrix[i][j] != matrix[i][end - j - 1+start] {
                //println!("idx {}{} {}   ref{} {}",i,j,matrix[i][j],end - j - 1+start, matrix[i][end - j - 1+start]);
                return (false,0)
            }
        }
    }
    return (true,col_start)
}

pub fn check_row_reflection(matrix: &Vec<Vec<char>>,row_start: usize)->(bool,usize) {
    //println!("checking row");
    let mut start: usize = 0;
    let mut end: usize = matrix.len(); 
    //println!("inital row start : {} , start {} end {}",row_start,start,end);
    if row_start < end-row_start {
        end = 2*row_start ; 
    }
    else {
        start = 2*row_start-end;
    }
    //println!("row start : {} , start {} end {}",row_start,start,end);
    for j in 0..matrix[0].len() {
        for i in start..row_start{
            //println!("process row : {:?} idx : {}",matrix[i],i);
            if matrix[i][j] != matrix[end-i-1+start][j] {
                //println!("idx {}{} {}   ref{} {}",i,j,matrix[i][j],end-i-1+start, matrix[end-i-1+start][j]) ;
                return (false,0)
            }
        }
    }
    return (true,row_start)
}


pub fn solve() {
    let input = read_input("input/input_day13.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    let mut matrix_vector: Vec<Vec<Vec<char>>> = Vec::new(); 
    let mut i = 0;
    let mut temp_matrix: Vec<Vec<char>> = Vec::new();
    while i < input_lines.len() {
        if input_lines[i].len() == 0 {
            matrix_vector.push(temp_matrix.clone()); 
            temp_matrix.clear(); 
        }
        else {
            temp_matrix.push(input_lines[i].chars().collect::<Vec<_>>().clone());
        }
        i+=1;
    }
    if temp_matrix.len() > 0 {
        matrix_vector.push(temp_matrix.clone());
        temp_matrix.clear();
    }

    //println!("input matrix: {:?}",matrix_vector );
    solve_part1(&matrix_vector);
}

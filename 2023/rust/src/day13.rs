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

        //check row wise reflection 
        // if (num_rows%2 == 0) {
        //     let mid = 
        // }
        //check col reflection 
        // if num_rows%2 == 0 {
        //     (found_reflection,row_idx_reflection) = check_row_reflection(&matrix,0); 
        // }
        // else {
            // for i in 0..
            // (found_reflection,row_idx_reflection) = check_row_reflection(&matrix,0) ; 
            // if !found_reflection {
            //     (found_reflection,row_idx_reflection) = check_row_reflection(&matrix,1); 
            // }
        // }
        println!("for matrix : {:?} found reflection : {}",matrix,found_reflection);
        if found_reflection {
            ans += (row_idx_reflection as u32)*100;
            continue;
        }

        if (num_cols%2 == 0) {
            (found_reflection,col_idx_reflection) = check_col_reflection(&matrix,0);
        }
        else {
            println!("checking ß");
            (found_reflection,col_idx_reflection) = check_col_reflection(&matrix,0) ; 
            if !found_reflection {
                (found_reflection,col_idx_reflection) = check_col_reflection(&matrix,1); 
            }
        }
        println!("for matrix : {:?} found reflection : {}",matrix,found_reflection);
        if found_reflection {
            ans += col_idx_reflection as u32;
        }
        println!("no reflection found"); 
        std::process::exit(1);
    }
    println!("part 1 ans : {}",ans);
}

pub fn check_col_reflection(matrix: &Vec<Vec<char>>,col_start: usize)->(bool,usize) {
    println!("checking col : ");
    let mut len_cols: usize = 0;
    if col_start == 0 && matrix[0].len()%2 == 1 {
        len_cols = matrix[0].len()-1;
    }
    else {
        len_cols = matrix[0].len();
    }
    let mid_col: usize = (len_cols/2);
    for i in 0..matrix.len() {
        for j in col_start..col_start+mid_col{
            if matrix[i][j] != matrix[i][len_cols - j - 1+col_start] {
                println!("idx {}{} {}   ref{} {}",i,j,matrix[i][j],len_cols - j - 1, matrix[i][len_cols - j - 1]);
                return (false,0)
            }
        }
    }
    return (true,mid_col+col_start)
}

pub fn check_row_reflection(matrix: &Vec<Vec<char>>,row_start: usize)->(bool,usize) {
    println!("checking row");
    let mut len_rows: usize = 0;
    if row_start == 0 && matrix.len()%2 == 1 {
        len_rows = matrix.len()-1;
    }
    else {
        len_rows = matrix.len();
    }
    println!("num_rows : {}",len_rows);
    let mid_row: usize = len_rows/2;
    for j in 0..matrix[0].len() {
        for i in row_start..row_start+mid_row{
            //println!("process row : {:?} idx : {}",matrix[i],i);
            if matrix[i][j] != matrix[len_rows-i-1+row_start][j] {
                println!("idx {}{} {}   ref{} {}",i,j,matrix[i][j],len_rows-i-1+row_start, matrix[len_rows-i-1+row_start][j]) ;
                return (false,0)
            }
        }
    }
    return (true,mid_row+row_start)
}


pub fn solve() {
    let input = read_input("input/input_day13.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    // solve_part1(&input_lines);
    // solve_part2(&input_lines);
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

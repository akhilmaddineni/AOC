use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(matrix: &Vec<Vec<char>>) {
    //find rows and cols with no galaxy's 
    let mut row_idx: Vec<usize> = Vec::new(); 
    let mut col_idx: Vec<usize> = Vec::new(); 
    let mut galaxy_idxs: Vec<(usize,usize)> = Vec::new();
    let mut ans: i64 = 0;
    for i in 0..matrix.len() {
        let mut flag: bool = true ; 
        for j in 0..matrix[0].len() {
            if matrix[i][j] == '#' {
                flag = false;
                galaxy_idxs.push((i,j));
            }
        }
        if flag {
            row_idx.push(i.try_into().unwrap());
        }
    }
    for j in 0..matrix[0].len() {
        let mut flag: bool = true;
        for i in 0..matrix.len() {
            if matrix[i][j] == '#' {
                flag = false;
                break;
            }
        }
        if flag {
            col_idx.push(j.try_into().unwrap());
        }
    }
    println!("empty rows {:?} empty cols {:?} galaxy idx {:?}",row_idx,col_idx,galaxy_idxs);
    //calculate glaxy idxs after counting empty row / cols as double as big 
    for idx in (0..row_idx.len()).rev() {
        //count from reverse to make stored indexes valid
        for i in 0..galaxy_idxs.len() {
            if row_idx[idx] < galaxy_idxs[i].0 {
                galaxy_idxs[i].0 += 999999; //for part 1 replace with 1
            }
        }
    }
    for idx in (0..col_idx.len()).rev() {
        for i in 0..galaxy_idxs.len() {
            if col_idx[idx] < galaxy_idxs[i].1 {
                galaxy_idxs[i].1 += 999999; //for part 1 replace with 1
            }
        } 
    }
    println!("updated galaxy idx {:?}",galaxy_idxs);

    //calculate distances 
    for i in 0..galaxy_idxs.len()-1 {
        for j in i+1..galaxy_idxs.len() {
            ans += i32::abs(galaxy_idxs[j].0 as i32-galaxy_idxs[i].0 as i32) as i64 + i32::abs(galaxy_idxs[j].1 as i32-galaxy_idxs[i].1 as i32) as i64 ;
        }
    }
    println!("part 2 ans : {}",ans);
}

pub fn solve() {
    let input = read_input("input/input_day11.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    // solve_part1(&input_lines);
    // solve_part2(&input_lines);
    let mut matrix: Vec<Vec<char>> = Vec::new(); 

    for i in 0..input_lines.len() {
        matrix.push(input_lines[i].chars().collect::<Vec<_>>().clone());
    }
    println!("{:?}",matrix);

    solve_part1(&matrix); 
}

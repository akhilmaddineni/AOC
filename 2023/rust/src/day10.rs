use std::fs;
use std::collections::{HashMap, VecDeque};
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

#[derive(Clone, Copy, Hash, Eq, PartialEq, Debug)]
struct Point {
    x: isize,
    y: isize,
}

/*

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

*/

// fn is_valid_connection(c1: char, c2: char, dir: &str) -> bool {
//     //println!("checking {} {} {}",c1,c2,dir);
//     if c1 == 'S' || c2 == 'S' {
//         return c2 != '.' && c1 != '.';
//     }

//     match dir {
//         "north" => matches!((c1, c2), ('|', '|') | ('|', '7') | ('|', 'F') | ('L', '7') | ('L', 'F') | ('L', '|') | ('J', '7') | ('J', 'F') | ('J', '|') ),
//         "south" => matches!((c1, c2), ('|', '|') | ('|', 'J') | ('|', 'L') | ('7', 'J') | ('7', 'L') | ('7','|') | ('F', 'J') | ('F', 'L') | ('F','|')),
//         "east" => matches!((c1, c2), ('-', '-') | ('-', 'J') | ('-', '7') | ('L', '-') | ('L', 'J') | ('L', '7') | ('F', '-') | ('F', 'J') | ('F', '7') ),
//         "west" => matches!((c1, c2), ('-', '-') | ('-', 'F') | ('-', 'L')  | ('J', 'L') | ('J', 'F') | ('J', '-') | ('7', 'L') | ('7', 'F') | ('7', '-')),
//         _ => false,
//     }
// }

fn valid_directions(letter: char) -> Vec<(isize,isize)> {
    if letter == 'S' {
        return vec![(-1,0),(0,1),(1,0),(0,-1)]
    }
    else if letter == 'F' {
        return vec![(0,1),(1,0)]
    }
    else if letter == '7' {
        return vec![(1,0),(0,-1)]
    }
    else if letter == 'J' {
        return vec![(-1,0),(0,-1)]
    }
    else if letter == 'L' {
        return vec![(-1,0),(0,1)]
    }
    else if letter == '-' {
        return vec![(0,1),(0,-1)]
    }
    else if letter == '|' {
        return vec![(-1,0),(1,0)]
    }
    Vec::new()
}

fn valid_move(point: (isize,isize), letter: char)->bool {
    if letter == 'S' {
        return true;
    }
    else if letter == '.'{
        return false;
    }
    else if letter == '|' && (point == (-1,0) || point == (1,0)) {
        return true;
    }
    else if letter == '-' && (point == (0,-1) || point == (0,1)) {
        return true;
    }
    else if letter == 'L' && (point == (1,0) || point == (0,-1)) {
        return true;
    }
    else if letter == 'J' && (point == (1,0) || point == (0,1)) {
        return true;
    }
    else if letter == '7' && (point == (-1,0) || point == (0,1)) {
        return true;
    }
    else if letter == 'F' && (point == (0,-1) || point == (-1,0)) {
        return true;
    }
    false
}

fn farthest_distance(matrix: Vec<Vec<char>>) -> isize {
    let rows = matrix.len() as isize;
    let cols = matrix[0].len() as isize;
    let mut max_distance: isize = 0;
    let mut start_point: Point = Point{x:0,y:0}; 
    let mut start_flag: bool = false;
    for i in 0..rows {
        for j in 0..cols {
            if matrix[i as usize][j as usize] == 'S' {
                start_point = Point{x:i,y:j};
                start_flag = true;
                break;
            }
        }
        if start_flag {
            break;
        }
    }

    if !start_flag {
        println!("Start not found, exiting");
        return 0
    }

    //find the farthest distance from S 
    let mut queue: VecDeque<(Point,isize)> = VecDeque::new(); 
    let mut visited = HashMap::new(); 
    queue.push_back((start_point,0));
    visited.insert(start_point,0);
    let mut last_point: Point = start_point;

    //let directions = [("north",-1,0),("south",1,0),("east",0,1),("west",0,-1)] ; 
    while let Some((point, dist)) = queue.pop_front() {
        println!("processing : {:?} {} dist {}",point,matrix[point.x as usize][point.y as usize],dist);

        for &(dx, dy) in &valid_directions(matrix[point.x as usize][point.y as usize]) {
            let new_x = point.x + dx;
            let new_y = point.y + dy;
            if new_x >= 0 && new_x < rows && new_y >= 0 && new_y < cols {
                let new_point = Point { x: new_x, y: new_y };
                if !visited.contains_key(&new_point) && valid_move((dx, dy),matrix[new_x as usize][new_y as usize]) {
                    visited.insert(new_point,dist+1); // Mark as visited when enqueued
                    //println!("valid path");
                    queue.push_back((new_point, dist + 1));
                    last_point = new_point;
                }
            }
        }
    }
    max_distance = *visited.get(&last_point).unwrap();
    max_distance
}

pub fn solve() {
    let input = read_input("input/input_day10.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    // solve_part1(&input_lines);
    // solve_part2(&input_lines);
    let mut matrix: Vec<Vec<char>> = Vec::new(); 

    for i in 0..input_lines.len() {
        matrix.push(input_lines[i].chars().collect::<Vec<_>>().clone());
    }

    println!("Farthest distance: {}", farthest_distance(matrix));
}

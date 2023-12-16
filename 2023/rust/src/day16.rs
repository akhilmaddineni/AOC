use std::fs;
use std::collections::VecDeque;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

#[derive(Debug, Clone, Copy)]
struct Point {
    x: usize,
    y: usize,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Point {
    fn move_in_direction(&mut self, direction: Direction) {
        match direction {
            Direction::Up => self.x -= 1,
            Direction::Down => self.x += 1,
            Direction::Left => self.y -= 1,
            Direction::Right => self.y += 1,
        }
    }
    fn is_valid_move(&mut self,direction: Direction,x_lim: usize,y_lim: usize) -> bool{
        match direction {
            Direction::Up => self.x > 0,
            Direction::Down => self.x < x_lim-1,
            Direction::Left => self.y > 0,
            Direction::Right => self.y < y_lim-1,
        }
    }
}

fn get_num_active(matrix: &Vec<Vec<char>>,matrix_store: &Vec<Vec<(bool,Vec<Direction>)>>,start_point: Point, direction: Direction) -> u64 {
    let mut ans: u64 = 0;
    let mut matrix_seen = matrix_store.clone(); 
    let mut beam_queue: VecDeque<(Point,Direction)> = VecDeque::new();

    let row_len = matrix.len(); 
    let col_len = matrix[0].len();

    //finding inital direction 
    matrix_seen[start_point.x][start_point.y].0 = true;
    if (matrix[start_point.x][start_point.y] == '.' || matrix[start_point.x][start_point.y]== '-' ) && direction == Direction::Right {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Right);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Right));
    }
    else if matrix[start_point.x][start_point.y] == '\\' && direction == Direction::Right {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Down);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Down));
    }
    else if matrix[start_point.x][start_point.y] == '/' && direction == Direction::Right {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Up);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Up));
    }
    else if matrix[start_point.x][start_point.y] == '|' && direction == Direction::Right {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Up);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Up));
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Down);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Down));
    }
    else if (matrix[start_point.x][start_point.y] == '.' || matrix[start_point.x][start_point.y]== '-' ) && direction == Direction::Left {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Left);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Left));
    }
    else if matrix[start_point.x][start_point.y] == '|'&& direction == Direction::Left {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Up);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Up));
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Down);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Down));
    }
    else if matrix[start_point.x][start_point.y] == '/'&& direction == Direction::Left {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Down);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Down));
    }
    else if matrix[start_point.x][start_point.y] == '\\'&& direction == Direction::Left {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Up);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y}, Direction::Up));
    }
    else if (matrix[start_point.x][start_point.y] == '.' || matrix[start_point.x][start_point.y]== '|' ) && direction == Direction::Up {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Up);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Up));
    }
    else if matrix[start_point.x][start_point.y] == '/' && direction == Direction::Up {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Right);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Right));
    }
    else if matrix[start_point.x][start_point.y] == '\\' && direction == Direction::Up {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Left);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Left));
    }
    else if matrix[start_point.x][start_point.y] == '-' && direction == Direction::Up {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Left);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Left));
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Right);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Right));
    }
    else if (matrix[start_point.x][start_point.y] == '.' || matrix[start_point.x][start_point.y]== '|' ) && direction == Direction::Down {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Down);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Down));
    }
    else if matrix[start_point.x][start_point.y] == '/' && direction == Direction::Down {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Left);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Left));
    }
    else if matrix[start_point.x][start_point.y] == '\\' && direction == Direction::Down {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Right);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Right));
    }
    else if matrix[start_point.x][start_point.y] == '-' && direction == Direction::Down {
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Left);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Left));
        matrix_seen[start_point.x][start_point.y].1.push(Direction::Right);
        beam_queue.push_back((Point {x:start_point.x,y:start_point.y},Direction::Right));
    }

    //process queue until empty 
    while beam_queue.len() > 0 {
        let mut cur_point: Point ; 
        let mut cur_direction: Direction;
        (cur_point,cur_direction)=beam_queue.pop_back().unwrap();
        //println!("{:?}{:?}",cur_point,cur_direction);
        if cur_point.is_valid_move(cur_direction,row_len,col_len){
            cur_point.move_in_direction(cur_direction); 
            if cur_point.x >=0 && cur_point.x<row_len && cur_point.y>=0 && cur_point.y<col_len {
                if matrix[cur_point.x][cur_point.y] == '.' {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&cur_direction) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(cur_direction); 
                        beam_queue.push_back((cur_point,cur_direction)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '-' && (cur_direction == Direction::Right || cur_direction == Direction::Left) {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&cur_direction) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(cur_direction); 
                        beam_queue.push_back((cur_point,cur_direction)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '|' && (cur_direction == Direction::Up || cur_direction == Direction::Down) {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&cur_direction) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(cur_direction); 
                        beam_queue.push_back((cur_point,cur_direction)); 
                    }
                    
                }
                else if matrix[cur_point.x][cur_point.y] == '-' && (cur_direction == Direction::Up || cur_direction == Direction::Down) {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Left) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Left);
                        beam_queue.push_back((cur_point.clone(),Direction::Left)); 
                    }
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Right) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Right);
                        beam_queue.push_back((cur_point.clone(),Direction::Right)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '|' && (cur_direction == Direction::Right || cur_direction == Direction::Left) {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Up) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Up);
                        beam_queue.push_back((cur_point.clone(),Direction::Up)); 
                    }
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Down) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Down);
                        beam_queue.push_back((cur_point.clone(),Direction::Down)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '/' && cur_direction == Direction::Right  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Up) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Up);
                        beam_queue.push_back((cur_point.clone(),Direction::Up)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '/' && cur_direction == Direction::Left  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Down) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Down);
                        beam_queue.push_back((cur_point.clone(),Direction::Down)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '/' && cur_direction == Direction::Up  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Right) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Right);
                        beam_queue.push_back((cur_point.clone(),Direction::Right)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '/' && cur_direction == Direction::Down  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Left) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Left);
                        beam_queue.push_back((cur_point.clone(),Direction::Left)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '\\' && cur_direction == Direction::Right  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Down) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Down);
                        beam_queue.push_back((cur_point.clone(),Direction::Down)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '\\' && cur_direction == Direction::Left  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Up) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Up);
                        beam_queue.push_back((cur_point.clone(),Direction::Up)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '\\' && cur_direction == Direction::Up  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Left) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Left);
                        beam_queue.push_back((cur_point.clone(),Direction::Left)); 
                    }
                }
                else if matrix[cur_point.x][cur_point.y] == '\\' && cur_direction == Direction::Down  {
                    matrix_seen[cur_point.x][cur_point.y].0 = true;
                    if !matrix_seen[cur_point.x][cur_point.y].1.contains(&Direction::Right) {
                        matrix_seen[cur_point.x][cur_point.y].1.push(Direction::Right);
                        beam_queue.push_back((cur_point.clone(),Direction::Right)); 
                    }
                }
            }

        }
    }

    

    for i in 0..row_len {
        for j in 0..col_len {
            if matrix_seen[i][j].0 == true {
                ans +=1;
            }
        }
    }
    ans
}

fn solve_part1(matrix: &Vec<Vec<char>>) {
    let mut ans: u64 = 0;
    
    let mut matrix_seen: Vec<Vec<(bool,Vec<Direction>)>> = Vec::new(); 
    //fill matrix seen 
    for i in 0..matrix.len(){
        let mut temp_matrix_row: Vec<(bool,Vec<Direction>)> = Vec::new(); 
        for j in 0..matrix[0].len(){
            let mut direction: Vec<Direction> = Vec::new(); 
            temp_matrix_row.push((false,direction));
        }
        matrix_seen.push(temp_matrix_row);
    }
    ans = get_num_active(&matrix,&matrix_seen,Point{x:0,y:0},Direction::Right);
    
    println!("Part 1 ans : {}",ans);
}

fn solve_part2(matrix: &Vec<Vec<char>>){
    let mut ans: u64 = 0;
    
    let mut matrix_seen: Vec<Vec<(bool,Vec<Direction>)>> = Vec::new(); 
    //fill matrix seen 
    for i in 0..matrix.len(){
        let mut temp_matrix_row: Vec<(bool,Vec<Direction>)> = Vec::new(); 
        for j in 0..matrix[0].len(){
            let mut direction: Vec<Direction> = Vec::new(); 
            temp_matrix_row.push((false,direction));
        }
        matrix_seen.push(temp_matrix_row);
    }

    //first and last cols 
    for i in 0..matrix.len(){
        ans = ans.max(get_num_active(&matrix,&matrix_seen,Point{x:i,y:0},Direction::Right));
        ans = ans.max(get_num_active(&matrix,&matrix_seen,Point{x:i,y:matrix[0].len()-1},Direction::Left));
    }

    //first and last rows 
    for j in 0..matrix[0].len() {
        ans = ans.max(get_num_active(&matrix,&matrix_seen,Point{x:0,y:j},Direction::Down));
        ans = ans.max(get_num_active(&matrix,&matrix_seen,Point{x:matrix.len()-1,y:j},Direction::Up));
    }
    
    println!("Part 2 ans : {}",ans);

}
pub fn solve() {
    let input = read_input("input/input_day16.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    let mut matrix: Vec<Vec<char>> = Vec::new(); 

    for i in 0..input_lines.len() {
        //append to start for easy processing
        matrix.push(input_lines[i].chars().collect::<Vec<_>>().clone());
    }
    println!("{:?}",matrix);

    solve_part1(&matrix); 
    solve_part2(&matrix);
}

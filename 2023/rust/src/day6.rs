use std::fs;
use std::collections::HashMap;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part(time_dist_map: &HashMap<u64,u64>) {
    let mut final_ans: u64 = 1; 
    for (time,dist) in time_dist_map {
        let mut left: u64 = 0 ; 
        let mut right: u64 = time.clone(); 
        let mut flag: bool = false ; 
        while !flag {
            if left*(*time-left) > *dist {
                flag = true; 
                break;
            }
            left += 1;
        }
        flag = false ; 
        while !flag {
            if right*(*time-right) > *dist {
                flag = true;
                break;
            }
            right -= 1;
        }
        // println!("{} {}",time,dist);

        // println!("ans :  right {} left {} ans {}",right,left,right-left+1);
        final_ans *= (right-left+1) as u64;

    }
    println!("final ans : {}",final_ans);

}

//TODO : Implement with binary search
// fn solve_part2(time: &u64, distance : &u64) {
//     
//     let mut left = 0; 
//     let mut right = time;
//     while left <= right {
//         let mut mid = left + (right-left)/2 ;
//         if mid*(time-1)
//     }

// }


pub fn solve() {
    let input = read_input("input/input_day6.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);

    let mut time_str: Vec<&str> = input_lines[0].split_whitespace().collect();
    time_str.remove(0);
    let mut distance_str: Vec<&str> = input_lines[1].split_whitespace().collect();
    distance_str.remove(0);
    let mut time_dist_map: HashMap<u64,u64> = HashMap::new(); 
    for i in 0..time_str.len() { 
        time_dist_map.insert(time_str[i].parse::<u64>().unwrap(),distance_str[i].parse::<u64>().unwrap()); 
    }
    println!("{:?}",time_dist_map);
    //part 1
    solve_part(&time_dist_map);

    let time: u64 = input_lines[0].replace(" ","").replace("Time:","").parse::<u64>().unwrap();
    let distance: u64 = input_lines[1].replace(" ","").replace("Distance:","").parse::<u64>().unwrap();
    println!("time : {}",time);
    println!("distance : {}",distance);
    let mut time_dist_map_full: HashMap<u64,u64> = HashMap::new(); 
    time_dist_map_full.insert(time.try_into().unwrap(),distance.try_into().unwrap());
    //part 2
    solve_part(&time_dist_map_full);
}

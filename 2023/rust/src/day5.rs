use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(seed_map_vector: &Vec<Vec<((u64,u64),(u64,u64))>>, seeds_int: &Vec<u64>) {

    let mut ans: u64 = u64::MAX ; 
    for seed in seeds_int {
        let mut seed_pos: u64 = seed.clone() ; //TODO : read about borrow checker 
        for each_map in 0..seed_map_vector.len() {
            //loop for each mapping , last position of the seed is the answer
            for point_idx in 0..seed_map_vector[each_map].len() {
                if seed_pos>= seed_map_vector[each_map][point_idx].0.0 && seed_pos<=seed_map_vector[each_map][point_idx].0.1 {
                    seed_pos = seed_map_vector[each_map][point_idx].1.0+seed_pos-seed_map_vector[each_map][point_idx].0.0;
                    break;
                }
                //if no match after loop then seed pos is same
            }
        }
        println!("seed pos for seed {} is {}",seed,seed_pos);
        ans = std::cmp::min(ans,seed_pos);
    }
    println!("Part 1 ans : {}",ans);
    
}
use std::collections::HashMap;
fn solve_part2(seed_map_vector: &Vec<Vec<((u64,u64),(u64,u64))>>, seeds_int: &Vec<u64>) {
    let mut ans: u64 = u64::MAX ; 
    //seeds definition id different even idx is seed , odd index is range
    let mut num: usize = 0 ; 
    //let mut ans_hash: HashMap<u64, u64> = HashMap::new();
    while num < seeds_int.len() {
        let mut seed_range = vec![seeds_int[num],seeds_int[num]+seeds_int[num+1]-1];
        for seed in seed_range{
            let mut seed_pos: u64 = seed.clone() ; //TODO : read about borrow checker 
            // if ans_hash.contains_key(&seed){
            //     seed_pos = *ans_hash.get(&seed).unwrap(); 
            // }
            // else {
                for each_map in 0..seed_map_vector.len() {
                    //loop for each mapping , last position of the seed is the answer
                    for point_idx in 0..seed_map_vector[each_map].len() {
                        if seed_pos>= seed_map_vector[each_map][point_idx].0.0 && seed_pos<=seed_map_vector[each_map][point_idx].0.1 {
                            seed_pos = seed_map_vector[each_map][point_idx].1.0+seed_pos-seed_map_vector[each_map][point_idx].0.0;
                            break;
                        }
                        //if no match after loop then seed pos is same
                    }
                }
            //     ans_hash.insert(seed,seed_pos);
            // }
            println!("seed pos for seed {} is {}",seed,seed_pos);
            ans = std::cmp::min(ans,seed_pos);
        }
        num += 2;
    }
    println!("Part 2 ans : {}",ans);
}

fn solve_part2_ranges(seed_map_vector: &Vec<Vec<((u64,u64),(u64,u64))>>, seeds_int: &Vec<u64>) {
    let mut ans: u64 = u64::MAX ; 
    //seeds definition id different even idx is seed , odd index is range
    let mut num: usize = 0 ; 
    let mut ans_hash: HashMap<(u64, u64),(u64,u64)> = HashMap::new();
    while num < seeds_int.len() {
        let mut seed_range = vec![seeds_int[num],seeds_int[num]+seeds_int[num+1]-1];
        for seed in seed_range{
            let mut seed_pos: u64 = seed.clone() ; //TODO : read about borrow checker 
            // if ans_hash.contains_key(&seed){
            //     seed_pos = *ans_hash.get(&seed).unwrap(); 
            // }
            // else {
                for each_map in 0..seed_map_vector.len() {
                    //loop for each mapping , last position of the seed is the answer
                    for point_idx in 0..seed_map_vector[each_map].len() {
                        if seed_pos>= seed_map_vector[each_map][point_idx].0.0 && seed_pos<=seed_map_vector[each_map][point_idx].0.1 {
                            seed_pos = seed_map_vector[each_map][point_idx].1.0+seed_pos-seed_map_vector[each_map][point_idx].0.0;
                            break;
                        }
                        //if no match after loop then seed pos is same
                    }
                }
            //     ans_hash.insert(seed,seed_pos);
            // }
            println!("seed pos for seed {} is {}",seed,seed_pos);
            ans = std::cmp::min(ans,seed_pos);
        }
        num += 2;
    }
    println!("Part 2 ans : {}",ans);
}



pub fn solve() {
    let input = read_input("input/input_day5.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    //println!("num lines : {} , size of line {}",input_lines.len(),input_lines[0].len());
    //declare 2d array
    // let mut number_map = vec![vec![' '; input_lines[0].len()]; input_lines.len()];
    // //fill number map 
    // for row in 0..number_map.len() {
    //     number_map[row] = input_lines[row].chars().collect();
    // }
    let mut seeds: Vec<&str> = input_lines[0].split_whitespace().collect();
    seeds.remove(0); //remove seed: 
    println!("{:?}",seeds);
    let mapping_names: Vec<String> = vec![ 
                            "seed-to-soil map:".to_string(),
                            "soil-to-fertilizer map:".to_string(),
                            "fertilizer-to-water map:".to_string(),
                            "water-to-light map:".to_string(),
                            "light-to-temperature map:".to_string(),
                            "temperature-to-humidity map:".to_string(),
                            "humidity-to-location map:".to_string()
                            ];
    let mut seeds_int: Vec<u64> = Vec::new(); 
    for seed in seeds {
        seeds_int.push(seed.parse::<u64>().unwrap());
    }
    println!("total number of seeds : {}",seeds_int.len());
    // let mut seed_soil_map ; 
    // let mut soil_fertilizer_map ; 
    // let mut fertilizer_water_map ; 
    // let mut water_light_map ; 
    // let mut light_temp_map ; 
    // let mut temp_humid_map ; 
    // let mut humid_loc_map ; 
    let mut seed_map_vector: Vec<Vec<((u64,u64),(u64,u64))>> = Vec::with_capacity(7); 
    let mut idx: usize = 0 ;
    let mut temp_vec: Vec<((u64,u64),(u64,u64))> = Vec::new(); 
    for each_line in 3..input_lines.len() {
        if input_lines[each_line] != "" {
            //println!("{}",input_lines[each_line]);
            if mapping_names.contains(&input_lines[each_line]) {
                seed_map_vector.push(temp_vec.clone());
                idx += 1 ;
                temp_vec.clear();
            }
            else {
                //process dest source and range 
                let dest_src: Vec<&str> = input_lines[each_line].trim().split_whitespace().collect();
                let dest_start = dest_src[0].parse::<u64>().unwrap();
                let src_start = dest_src[1].parse::<u64>().unwrap();
                let range = dest_src[2].parse::<u64>().unwrap();
                temp_vec.push(((src_start,src_start+range-1),(dest_start,dest_start+range-1)))
            }
        }
    }
    seed_map_vector.push(temp_vec.clone());
    // println!("{:?}",seed_map_vector);
    // println!("{:?}",seeds_int);
    solve_part1(&seed_map_vector,&seeds_int);
    solve_part2(&seed_map_vector,&seeds_int);
    // solve_part2(&input_lines);
    //solve_part2(&number_map);
}
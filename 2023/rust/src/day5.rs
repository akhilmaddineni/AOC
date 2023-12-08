use std::fs;
fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

fn solve_part1(seed_map_vector: &Vec<Vec<((i64,i64),(i64,i64))>>, seeds_int: &Vec<i64>) {

    let mut ans: i64 = i64::MAX ; 
    for seed in seeds_int {
        let mut seed_pos: i64 = seed.clone() ; //TODO : read about borrow checker 
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
        //println!("seed pos for seed {} is {}",seed,seed_pos);
        ans = std::cmp::min(ans,seed_pos);
    }
    println!("Part 1 ans : {}",ans);
    
}

fn solve_part2_ranges(seed_map_vector: &Vec<Vec<((i64,i64),(i64,i64))>>, seeds_int: &Vec<i64>) {
    let mut ans: i64 = i64::MAX ; 
    //seeds definition id different even idx is seed , odd index is range
    let mut num: usize = 0 ; 
    //let mut ans_hash: HashMap<(i64, i64),(i64,i64)> = HashMap::new();
    let mut seeds: Vec<(i64,i64)> = Vec::new();
    while num < seeds_int.len() {
        seeds.push((seeds_int[num],seeds_int[num]+seeds_int[num+1]-1)); 
        num+=2;
    }
    let mut input_layer_points = seeds.clone(); 
    let mut input_layer_change_points: Vec<(i64,i64)>  = Vec::new(); 
    for each_map in 0..seed_map_vector.len() {
        //once each map is processed input layer point contain output of other layer
        input_layer_points.append(&mut input_layer_change_points); // this should clear input_layer changed points
        // println!("while start of layer processing :");
        // println!("input_layer_points : {:?}",input_layer_points);
        // println!("input_layer_change_points : {:?}",input_layer_change_points);
        // println!("vector map : {:?}",seed_map_vector[each_map]);
        for process_layer_input in &seed_map_vector[each_map] {
            let process_pending: Vec<(i64,i64)>  = input_layer_points.clone();
            input_layer_points.clear(); 
            //println!("processing point : {:?}",process_layer_input);
            for input_point in &process_pending {
                /* 
                process : 
                input point is fully in the process range 
                    - process output and add output to input layer change points 
                input point is partially in process range 
                    - some part of range is in going to output 
                    - process that range and add output to input layer change points 
                    - unprocessed should go back to process pending list. 
                input point fully exceeds the process range 
                    - process range limits added to input layer change points 
                    - exceeding ranges on the left and right goes back to the process pending list
                input point is not in the process range 
                    - need to check if the point lies in other process layer input points so add back to pending process points 
                 */
                //println!("processing {:?}",input_point);
                if process_layer_input.0.0 <= input_point.0 && process_layer_input.0.1 >= input_point.1 {
                    //println!("completely inside {:?}",input_point);
                    input_layer_change_points.push(
                        (   process_layer_input.1.0-process_layer_input.0.0+input_point.0,
                            process_layer_input.1.0-process_layer_input.0.0+input_point.1)
                        )
                }
                //sliding window left  
                else if process_layer_input.0.0 >= input_point.0 && process_layer_input.0.1 >= input_point.1 && process_layer_input.0.0 < input_point.1 {
                    //println!("window left {:?}",input_point);
                    input_layer_change_points.push(
                        (
                            process_layer_input.1.0,
                            process_layer_input.1.0-process_layer_input.0.0+input_point.1
                        )
                    );
                    input_layer_points.push((input_point.0,process_layer_input.0.0-1));
                }
                //sliding window right 
                else if process_layer_input.0.0 <= input_point.0 && process_layer_input.0.1 <= input_point.1 && process_layer_input.0.1 > input_point.0 {
                    //println!("window right {:?}",input_point);
                    input_layer_change_points.push(
                        (
                            process_layer_input.1.0-process_layer_input.0.0+input_point.0,
                            process_layer_input.1.1
                        )
                    );
                    input_layer_points.push((process_layer_input.0.1+1,input_point.1));
                }
                //input fully exceeds 
                else if process_layer_input.0.0 >= input_point.0 && process_layer_input.0.1 <= input_point.1 {
                    //println!("fully exceed {:?}",input_point);
                    input_layer_change_points.push((process_layer_input.1.0,process_layer_input.1.1));
                    input_layer_points.push((input_point.0,process_layer_input.0.0-1));
                    input_layer_points.push((process_layer_input.0.1+1,input_point.1));
                }
                else {
                    //println!("no match {:?}",input_point);
                    input_layer_points.push((input_point.0,input_point.1));
                }
            }

        }
        //println!("input_layer_points : {:?}",input_layer_points);
        //println!("input_layer_change_points : {:?}",input_layer_change_points);
    }
    for each_ele in input_layer_points {
        ans = std::cmp::min(ans,each_ele.0);
    }
    for each_ele in input_layer_change_points {
        ans = std::cmp::min(ans,each_ele.0);
    }
    println!("Part 2 ans : {}",ans);
}



pub fn solve() {
    let input = read_input("input/input_day5.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
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
    let mut seeds_int: Vec<i64> = Vec::new(); 
    for seed in seeds {
        seeds_int.push(seed.parse::<i64>().unwrap());
    }
    println!("total number of seeds : {}",seeds_int.len());
    let mut seed_map_vector: Vec<Vec<((i64,i64),(i64,i64))>> = Vec::with_capacity(7); 
    let mut idx: usize = 0 ;
    let mut temp_vec: Vec<((i64,i64),(i64,i64))> = Vec::new(); 
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
                let dest_start = dest_src[0].parse::<i64>().unwrap();
                let src_start = dest_src[1].parse::<i64>().unwrap();
                let range = dest_src[2].parse::<i64>().unwrap();
                temp_vec.push(((src_start,src_start+range-1),(dest_start,dest_start+range-1)))
            }
        }
    }
    seed_map_vector.push(temp_vec.clone());
    // println!("{:?}",seed_map_vector);
    // println!("{:?}",seeds_int);
    solve_part1(&seed_map_vector,&seeds_int);
    solve_part2_ranges(&seed_map_vector,&seeds_int);
}
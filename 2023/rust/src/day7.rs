use std::fs;
use std::collections::HashMap;
use std::cmp::Ordering;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Error reading file")
}

fn parse_lines_to_vec(input: &str) -> Vec<String> {
    input.lines().map(|line| line.trim_end().to_string()).collect()
}

#[repr(C)] //ctype enum 
enum card_rank {
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIR,
    THREE_KIND,
    FULL_HOUSE,
    FOUR_KIND,
    FIVE_KIND,
}

fn find_rank(card_info: &str) -> card_rank {
    let mut freq_hash: HashMap<char,u8> = HashMap::new();
    for each_char in card_info.chars() {
        let count = freq_hash.entry(each_char).or_insert(0);
        *count += 1;
    }
    if freq_hash.len() == 1 {
        return card_rank::FIVE_KIND
    }
    else if freq_hash.len() == 2 {
        //fourkind or full house
        for key in freq_hash.keys() {
            if freq_hash[key] == 1 {
                return card_rank::FOUR_KIND
            }
            else if freq_hash[key] == 2 {
                return card_rank::FULL_HOUSE
            }
        }
    }
    else if freq_hash.len() == 3 {
        for key in freq_hash.keys() {
            if freq_hash[key] == 3 {
                return card_rank::THREE_KIND
            }
            else if freq_hash[key] == 2 {
                return card_rank::TWO_PAIR
            }
        }
    }
    else if freq_hash.len() == 4 {
        return card_rank::ONE_PAIR
    }
    card_rank::HIGH_CARD
}


fn solve_part1(card_bid_map: &Vec<(&str,u32)>,card_value: &HashMap<char,usize> ) {
    //println!("{}",find_rank("AAAAB") as i32);
    //find_rank("AAAAB");
    let mut ordered_hash: HashMap<i32,Vec<(&str,u32)>> = HashMap::new(); 
    let mut ans: u64 = 0;
    for &each_card in card_bid_map {
        let each_card_rank: i32 = find_rank(each_card.0) as i32 ;
        //println!("rank of {} is {}",each_card.0,each_card_rank as i32);
        ordered_hash.entry(each_card_rank)
                    .or_insert_with(Vec::new)
                    .push(each_card);
    }
    let mut rank = 0;
    for each_enum in 0..7 {
        if ordered_hash.contains_key(&each_enum) {
            // println!("{:?}",ordered_hash[&each_enum]);
            if ordered_hash[&each_enum].len() > 1 {
                let mut card_strings: Vec<&str> = Vec::new(); 
                let mut card_value_map: HashMap<&str,u32>= HashMap::new();
                for each_ele in &ordered_hash[&each_enum]
                {
                    card_strings.push(each_ele.0);
                    card_value_map.insert(each_ele.0,each_ele.1);
                } 
                //println!("{:?}",card_strings);
                card_strings.sort_unstable_by(|a, b| compare_strings(a, b, &card_value));
                //println!("{:?}",card_strings);
                for &each_ele in card_strings.iter().rev() {
                    rank += 1;
                    ans += card_value_map[each_ele] as u64 * rank as u64 ;
                }
            }
            else {
                rank += 1;
                ans += ordered_hash[&each_enum][0].1 as u64 * rank as u64;
            }
            
        }
    }
    println!("part 1 ans : {}",ans);
}

fn solve_part2(input_lines: &Vec<String>) {
}

fn compare_strings(a: &str, b: &str, order: &HashMap<char, usize>) -> Ordering {
    let mut a_chars = a.chars();
    let mut b_chars = b.chars();

    loop {
        match (a_chars.next(), b_chars.next()) {
            (Some(char_a), Some(char_b)) => {
                let order_a = order.get(&char_a).unwrap_or(&usize::MAX);
                let order_b = order.get(&char_b).unwrap_or(&usize::MAX);
                if order_a != order_b {
                    return order_a.cmp(order_b);
                }
            },
            (None, None) => return Ordering::Equal,
            (None, Some(_)) => return Ordering::Less,
            (Some(_), None) => return Ordering::Greater,
        }
    }
}

pub fn solve() {
    let input = read_input("input/input_day7.txt");
    let input_lines: Vec<String> = parse_lines_to_vec(&input);
    let card_value: HashMap<char,usize> = HashMap::from([
        ('2',12),
        ('3',11),
        ('4',10),
        ('5',9),
        ('6',8),
        ('7',7),
        ('8',6),
        ('9',5),
        ('T',4),
        ('J',3),
        ('Q',2),
        ('K',1),
        ('A',0)]);
    let mut card_bid_map: Vec<(&str,u32)> = Vec::new(); //string , bid , final rank
    for each_line in &input_lines {
        let temp_vec: Vec<&str> = each_line.split_whitespace().collect();
        card_bid_map.push((temp_vec[0],temp_vec[1].parse::<u32>().unwrap()))
    }
    //println!("{:?}",card_bid_map);
    solve_part1(&card_bid_map,&card_value);
    solve_part2(&input_lines);
}

use std::env;

mod day1;
mod day2;
mod day3;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: cargo run [day_num]");
        return;
    }
    match args[1].as_str() {
        "1" => day1::solve(),
        "2" => day2::solve(),
        "3" => day3::solve(),
        _=>println!("day {} not implemented",args[1].as_str()),
    }
}
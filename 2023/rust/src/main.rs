use std::env;

mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;
mod day9;
mod day10;
mod day11;
mod day13;
mod day15;

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
        "4" => day4::solve(),
        "5" => day5::solve(),
        "6" => day6::solve(),
        "7" => day7::solve(),
        "8" => day8::solve(),
        "9" => day9::solve(),
        "10" => day10::solve(),
        "11" => day11::solve(),
        "13" => day13::solve(),
        "15" => day15::solve(),
        _=>println!("day {} not implemented",args[1].as_str()),
    }
}

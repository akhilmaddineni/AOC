use std::env;

mod day1;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: cargo run [day_num]");
        return;
    }
    match args[1].as_str() {
        "1" => day1::solve(),
        _=>println!("{} day not implemented",args[1].as_str()),
    }
}

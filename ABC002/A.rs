use std::io;

fn main() {
  let mut input = String::new();
  io::stdin().read_line(&mut input)
    .expect("failed to read from stdin");
  let vec: Vec<&str> = input.split_whitespace().collect();
  let first_line = vec[0].parse().unwrap_or(0);
  let second_line = vec[1].parse().unwrap_or(0);
  if first_line > second_line {
    println!("{}", first_line);
  } else {
    println!("{}", second_line);
  }
}
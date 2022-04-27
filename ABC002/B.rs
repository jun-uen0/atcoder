use std::io;

fn main() {
  let mut input = String::new();
  io::stdin().read_line(&mut input)
    .expect("failed to read from stdin");
  let reduce_a = input.replace("a", "");
  let reduce_i = reduce_a.replace("i", "");
  let reduce_u = reduce_i.replace("u", "");
  let reduce_e = reduce_u.replace("e", "");
  let reduce_o = reduce_e.replace("o", "");
  println!("{}", reduce_o.trim());
}
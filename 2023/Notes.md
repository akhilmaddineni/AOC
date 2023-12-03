# Notes for 2023 

### From tour of rust 
- The data type for an array is [T;N] where T is the elements' type, and N is the fixed length known at compile-time.
- Functions can return multiple values by returning a tuple of values.
- infinite loop `loop` , `break` to break loop 
- The .. operator creates an iterator that generates numbers from a start number up to but not including an end number.
- The ..= operator creates an iterator that generates numbers from a start number up to and including an end number.
- `match` is like switch case in rust 
- return from loop can be done by break like `break "some_return_val";`
- if,match,function or scope block is expression without ; , rust will return value from a block
- static methods — methods that belong to a type itself are called using the :: operator. `String::from("Hello world!");`
- instance methods — methods that belong to an instance of a type are called using the . operator. `s.len()`
- Generic type allow us to partially define a struct or enum,enabling a compiler to create a fully defined version at compile time based off our code usage. 
- This can be explicitly defined by using the `::<T>` operator, also known by the name turbofish.
- Rust doesnt have null but providing a None alternative representation for one or many alternate values is common. 
- Rust has a builtin generic enum called Option that alows to represent nullable values without using null. 
- This Enum is common, instances of the enum can be created anywhere with the enum variants Some and None. 
- Rust has a built in generic enum called Result that allows us to return a value that has the possibility of failing.
- instances of the enum can be created anywhere with the enum variants Ok and Err.
- `unwrap` can be useful for getting a value in a quick and dirty manner , unwrap will get the value inside Option/Result. If the enum is of type None/Err, panic!


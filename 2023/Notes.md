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
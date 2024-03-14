# NS Commands

puts "Enter the value of a"
flush stdout
gets stdin a 
puts "Enter value of b"
flush stdout
gets stdin b

set c [expr $a + $b]
puts "The value of a = $a"
puts "The value of b = $b"
puts "The value of c= a+b = $c"

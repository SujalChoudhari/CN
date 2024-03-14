# NS Commands

set a 24
set b 15

puts $a
puts $b

puts "The value of a = $a"
puts "The value of b = $b"
puts "The value of a+b= $a+$b"
set c [expr $a + $b]
puts "The value is c is $c"
set d [expr [expr $b - $a] * $c]
puts "The value of d is $d"

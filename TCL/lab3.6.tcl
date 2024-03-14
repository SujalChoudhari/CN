proc print {k} {
	for {set i 0} { $i < $k} { incr i} {
		puts "node_($i) \t n$i"
		puts "n $i $k"
	}
}

print 10

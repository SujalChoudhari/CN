#lab8: Creating Wired Scenario
set ns [new Simulator]

set tr [ open out.tr w]
$ns trace-all $tr

set namtr [open out.nam w]
$ns namtrace-all $namtr


# Create Nodes
set n0  [$ns node]
set n1  [$ns node]
set n2  [$ns node]
set n3  [$ns node]
set n4  [$ns node]
set n5  [$ns node]

# Connect Nodes
$ns duplex-link $n1 $n0 10Mb 5ms DropTail
$ns duplex-link $n1 $n2 10Mb 5ms DropTail
$ns duplex-link $n1 $n3 10Mb 5ms DropTail

$ns duplex-link $n4 $n5 10Mb 5ms DropTail
$ns duplex-link $n4 $n2 10Mb 5ms DropTail
$ns duplex-link $n4 $n3 10Mb 5ms DropTail

# Position Nodes
$ns duplex-link-op $n1 $n0 orient left
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n1 $n3 orient right-down

$ns duplex-link-op $n4 $n5 orient right
$ns duplex-link-op $n4 $n2 orient left-up
$ns duplex-link-op $n4 $n3 orient left-down

# Create Packets
set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0

set null0 [new Agent/Null]
$ns attach-agent $n3 $null0

set udp1 [new Agent/UDP]
$ns attach-agent $n2 $udp1 

set null1 [new Agent/Null]
$ns attach-agent $n5 $null1

$udp0 set fid_ 1
$ns color 1 blue

$udp1 set fid_ 2
$ns color 2 red

# Connect
$ns connect $udp0 $null0
$ns connect $udp1 $null1

# Set Flow
set cbr0 [new Application/Traffic/CBR]
set cbr1 [new Application/Traffic/CBR]

$cbr0 attach-agent $udp0
$cbr1 attach-agent $udp1

# Timings
$ns at 2 "$cbr0 start"
$ns at 3 "$cbr1 start"

$ns at 8 "$cbr0 stop"
$ns at 7 "$cbr1 stop"
$ns at 10.5 "$ns halt"

# Start
$ns run

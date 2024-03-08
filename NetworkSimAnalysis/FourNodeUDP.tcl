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

# Connect Nodes
$ns duplex-link $n0 $n1 10Mb 5ms DropTail
$ns duplex-link $n2 $n0 10Mb 5ms DropTail
$ns duplex-link $n3 $n0 10Mb 5ms DropTail

# Position Nodes
$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n0 $n2 orient left-up
$ns duplex-link-op $n0 $n3 orient left-down

# Create Packets
set udp0 [new Agent/UDP]
$ns attach-agent $n3 $udp0

set null0 [new Agent/Null]
$ns attach-agent $n1 $null0

set udp1 [new Agent/UDP]
$ns attach-agent $n2 $udp1 

set null1 [new Agent/Null]
$ns attach-agent $n1 $null1


# Connect
$ns connect $udp0 $null0
$ns connect $udp1 $null1

# Set Flow
set cbr0 [new Application/Traffic/CBR]
set cbr1 [new Application/Traffic/CBR]

$cbr0 attach-agent $udp0
$cbr1 attach-agent $udp1

# Timings
$ns at 1.0 "$cbr0 start"
$ns at 1.5 "$cbr1 start"

$ns at 4.5 "$cbr0 stop"
$ns at 5.0 "$cbr1 stop"
$ns at 5.0 "$ns halt"

# Start
$ns run

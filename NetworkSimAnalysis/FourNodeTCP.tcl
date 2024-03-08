set ns [new Simulator]

set tr [ open out.tr w]
$ns trace-all $tr

set namtr [open out.nam w]
$ns namtrace-all $namtr

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]


$ns duplex-link $n0 $n1 10Mb 5ms DropTail

$ns duplex-link $n2 $n0 10Mb 5ms DropTail
$ns duplex-link $n3 $n0 10Mb 5ms DropTail

$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n0 $n2 orient left-up
$ns duplex-link-op $n0 $n3 orient left-down

set tcp0 [new Agent/TCP]
$ns attach-agent $n2 $tcp0

set sink0 [new Agent/TCPSink]
$ns attach-agent $n1 $sink0

$ns connect $tcp0 $sink0

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

set tcp1 [new Agent/TCP]
$ns attach-agent $n3 $tcp1

set sink1 [new Agent/TCPSink]
$ns attach-agent $n1 $sink1

$ns connect $tcp1 $sink1

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1

proc finish { } {
global tr namtr
close $tr
close $namtr
exec nam -r 10m out.nam &
exit 0
}

$ns at 2.0 "$ftp0 start"
$ns at 8.0 "$ftp0 stop"
#$ns at 3.0 "$ftp1 start"
#$ns at 9.0 "$ftp1 stop"

$ns at 10.0 "finish"


$ns run
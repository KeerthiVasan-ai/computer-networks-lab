set ns [new Simulator]
$ns color 1 Blue
$ns color 2 Red
set tf [open out.tr w]
set winFile [open WinFile w]
$ns trace-all $tf

set nf [open out.nam w]
$ns namtrace-all $nf

proc finish {} {
	global ns tf nf
	$ns flush-trace
	close $nf
	close $tf
	exec nam out.nam &
	exit 0
}

for {set i 0} {$i < 6} {incr i} {
	set n($i) [$ns node]
}

$n(1) color red
$n(1) shape box

$ns duplex-link $n(0) $n(2) 2Mb 10ms DropTail 
$ns duplex-link $n(1) $n(2) 2Mb 10ms DropTail 
$ns duplex-link $n(2) $n(3) 0.3Mb 100ms DropTail 
$ns duplex-link $n(3) $n(2) 0.3Mb 100ms DropTail

set lan [$ns newLan "$n(3) $n(4) $n(5)" 0.5Mb 40ms LL Queue/DropTailMAC/Csma/Cd Channel]

set tcp [new Agent/TCP/Newreno]
$ns attach-agent $n(0) $tcp

set sink [new Agent/TCPSink/DelAck]
$ns attach-agent $n(4) $sink

$ns connect $tcp $sink

$tcp set fid_ 1
$tcp set window_ 8000
$tcp set packetSize_ 552

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

$ns at 1.0 "$ftp start"
$ns at 124.0 "$ftp stop"

proc plotWindow {tcpSource file} {
	global ns
	set time 0.1
	set now [$ns now]
	set cwnd [$tcpSource set cwnd_]
	set wnd [$tcpSource set window_]
	puts $file "$now $cwnd"
	$ns at [expr $now+$time] "plotWindow $tcpSource $file"
}

$ns at 0.1 "plotWindow $tcp $winFile"
$ns at 5 "$ns trace-annotate \"packet drop\""
$ns at 125.0 "finish"

$ns run
 




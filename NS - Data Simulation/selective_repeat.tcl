set ns [new Simulator]
set nf [open selective_repeat.nam w]

set f [open selective_repeat.tr w]


$ns namtrace-all $nf 
$ns trace-all $f

proc finish {} {
	global ns nf
	$ns flush-trace
	close $nf
	exec nam selective_repeat.nam &
	exit 0
}

for {set i 0} {$i<6} {incr i} {
	set n($i) [$ns node]
}

set color {"red" "green" "chocolate"}

for {set i 0} {$i < 6} {incr i 2} {
	$n($i) color [lindex $color $i]
	$n([expr ($i+1)]) color [lindex $color $i]
}

for {set i 0} {$i < 6} {incr i} {
	$n($i) shape box;
	$ns at 0.0 "$n($i) label SYS($i)"
}

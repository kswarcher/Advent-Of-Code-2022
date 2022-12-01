$elfCal = gc .\AOCD1.txt
$elfTotCal = @()
[int]$oneElfCal = 0
$mostCal = -1

foreach($line in $elfCal){
    if($line -eq ""){
        $elfTotCal += $oneElfCal
        $oneElfCal = 0
    }else{
        $oneElfCal+=$line
    }

}

foreach($elf in $elfTotCal){
    if($elf -gt $mostCal){
        $mostCal = $elf
    }
}

$mostCal
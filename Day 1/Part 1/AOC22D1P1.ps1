#Read the calories in a from a file
$elfCal = gc .\AOCD1.txt

#Initialize variables in a scope that can be used/ won't be interferred with
$elfTotCal = @()
[int]$oneElfCal = 0
$mostCal = -1

#Get how many calories each elf is carrying
foreach($line in $elfCal){
    if($line -eq ""){
        $elfTotCal += $oneElfCal
        $oneElfCal = 0
    }else{
        $oneElfCal+=$line
    }

}

#Find the most calories carried by an elf
foreach($elf in $elfTotCal){
    if($elf -gt $mostCal){
        $mostCal = $elf
    }
}

#Print the most calories carried by an elf
$mostCal

#Read the calories in a from a file
$elfCal = gc .\AOCD1.txt

#Initialize variables in a scope that can be used/ won't be interferred with
$elfTotCal = @()
[int]$oneElfCal = 0
$mostCal = -1
$secondMostCal = -2
$thirdMostCal = -3

#Get how many calories each elf is carrying
foreach($line in $elfCal){
    if($line -eq ""){
        $elfTotCal += $oneElfCal
        $oneElfCal = 0
    }else{
        $oneElfCal+=$line
    }

}

#Find the most, 2nd most, and 3rd most calories carried by elfs
foreach($elf in $elfTotCal){
    if($elf -gt $mostCal){
        $thirdMostCal = $secondMostCal
        $secondMostCal = $mostCal
        $mostCal = $elf
    }elseif($elf -le $mostCal -and $elf -ge $secondMostCal){
        $thirdMostCal = $secondMostCal
        $secondMostCal = $elf
    }elseif($elf -le $secondMostCal -and $elf -ge $thirdMostCal){
        $thirdMostCal = $elf
    }
}

#Print the total of the top 3 amount of elfs
$mostCal+$secondMostCal+$thirdMostCal
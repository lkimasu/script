$FILE = Get-Content "D:\mount\MyLinuxServer.txt"
$servername = @()
foreach ($LINE in $FILE)
{
    $out = $LINE
    $servername+=$out
}

$FILE1 = Get-Content "D:\mount\MyLinuxcred.txt"
$password = @()
foreach ($LINE1 in $FILE1)
{
    $out1 = $LINE1
    $password+=$out1
}


for($j=0; $j -lt $password.Count; $j++) {

$command='hostname && df -h'
$username = 'root'
$servername1 = $servername[$j]
$password1 = $password[$j]
$plinkpath ='D:\mount\'
$commandoutput = echo y | &($plinkpath + "plink.exe") -pw $password1 $username@$servername1 $command
'-' * 30 |Out-File D:\mount\MyLinuxinfo.txt -Append
$commandoutput | Out-File D:\mount\MyLinuxinfo.txt -Append

}



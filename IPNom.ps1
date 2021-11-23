# Configuration IP   


#Debut du script : 

    echo `n "Bienvenue dans la configuration de l'adressage IP et du Nom du Serveur Windows."
    echo `n "Voici les informations de votre carte réseau : "
    Get-NetIPConfiguration


    $ipAddress = Read-Host -Prompt "Entrez l'adresse IP (IPv4) : "
    $Ethernet = Read-Host -Prompt "Entrez l'index de l'interface"
    $DGateway = Read-Host -Prompt "Entrez le Gateway : "
    $MasqueSousReseau = Read-Host -Prompt "Entrez le masque de sous-réseau en notation CIDR (24) : "
    $ServerAddress = Read-Host -Prompt "Entrez l'adresse DNS : "

    # Vérifier le numéro d'index avant

    New-NetIPAddress -IPAddress $ipAddress -InterfaceIndex $Ethernet -DefaultGateway $DGateway -AddressFamily IPv4 -PrefixLength $MasqueSousReseau
    Set-DnsClientServerAddress -InterfaceIndex $Ethernet -ServerAddresses $ServerAddress


# Configuration du Nom du Serveur   


#Debut du script : 

    $Nom = Read-Host -Prompt "Entrez le nom du serveur Windows : "

    Rename-Computer $Nom
    #Restart-Computer
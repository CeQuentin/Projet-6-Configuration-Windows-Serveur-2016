# Installation du service DHCP
# Source du code : IT-CONNECT.FR

    echo "Installation du service DHCP"
    Install-WindowsFeature -Name DHCP -IncludeManagementTools


# Création d'un groupe de sécurité DHCP
    
    Add-DhcpServerSecurityGroup
    Restart-Service dhcpserver


# Autoriser le serveur DHCP dans l'annuaire de l'Active Directory

    #$NomSrvDHCP = Read-Host -Prompt "Entrez le nom du serveur DHCP : "
    #$IPadd = Read-Host -Prompt "Entrez l'adresse IP du serveur : "

    #Add-DhcpServerInDC -DnsName $NomSrvDHCP -IPAddress $IPadd
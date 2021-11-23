# Installation du service AD
# Source du code : IT-CONNECT.FR

# Installation des rôles : AD, DNS, RSAT-AD-Tools

    $FeatureList = @("RSAT-AD-Tools","AD-Domain-Services","DNS")

        Foreach($Feature in $FeatureList)
       {
             Install-WindowsFeature $Feature -IncludeManagementTools -IncludeAllSubFeature
        }
    

# Création  du domaine Active Directory

    $DomainNameDNS = Read-Host -Prompt "Entrez le nom de domaine : "
    $DomainNameNetbios = Read-Host -Prompt "Entrez le nom Netbios du domaine : "


    $ForestConfiguration = @{
    '-DatabasePath'= 'C:\Windows\NTDS';
    '-DomainMode' = 'Default';
    '-DomainName' = $DomainNameDNS;
    '-DomainNetbiosName' = $DomainNameNetbios;
    '-ForestMode' = 'Default';
    '-InstallDns' = $true;
    '-LogPath' = 'C:\Windows\NTDS';
    '-NoRebootOnCompletion' = $false;
    '-SysvolPath' = 'C:\Windows\SYSVOL';
    '-Force' = $true;
    '-CreateDnsDelegation' = $false }

    Import-Module ADDSDeployment
    Install-ADDSForest @ForestConfiguration


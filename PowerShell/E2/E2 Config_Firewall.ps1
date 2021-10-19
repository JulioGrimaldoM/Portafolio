#Integrantes: Julio Alonso Grimaldo Mercado 
Import-Module -Name Modulo01
do{
    Write-Host "-----Configuracion de Firewall-----"
    Write-Host "Ver Status del Perfil..........[1]"
    Write-Host "Cambiar el status del Perfil...[2]"
    Write-Host "Ver perfil de red Actual.......[3]"
    Write-Host "Cambiar perfil de red Actual...[4]"
    Write-Host "Ver reglas de bloqueo..........[5]"
    Write-Host "Agregar reglas de Bloqueo......[6]"
    Write-Host "Eliminar Reglas de Bloqueo.....[7]"
    Write-Host "Salir..........................[8]"
    $opc= Read-Host -Prompt ">"
    switch($opc){
    1{
        ver-status
        break
    }
    2{
        Cambiar-StatusPerfil
        break
    }
    3{
        Ver-PerfilRedActual
        break
    }
    4{
        Cambiar-PerfilRedActual
        break
        }
    5{
        Ver-ReglasBloqueo
        break
        }
    6{
        Agregar-ReglasBloqueo
        break
        }
    7{
        Eliminar-ReglasBloqueo
        break
        }
    8{
        Write-Host "Saliendo..."
        break
    }
   
    }
}while($opc -ne 8)
Write-Host "Se salio exitosamente..."
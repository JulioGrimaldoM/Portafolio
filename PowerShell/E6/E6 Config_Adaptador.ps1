#Integrantes: Julio Alonso Grimaldo Mercado 
#https://www.solvetic.com/tutoriales/article/4293-comandos-red-utiles-windows-powershell/
Import-Module -Name E6Modulo
try{
    do{
        Write-Host "-------Configuracion de Adaptador Wifi-------"
        Write-Host "Informacion de todos los Adaptadores......[1]"
        Write-Host "Informacion de un Adaptador...............[2]"
        Write-Host "Habilitar Adaptador.......................[3]"
        Write-Host "Deshabilitar Adaptador....................[4]"
        Write-Host "Renombrar Adaptador.......................[5]"
        Write-Host "Detalles de Paquetes......................[6]"
        Write-Host "Salir.....................................[7]"

        $opc= Read-Host -Prompt ">" 
        switch($opc){
        1{
            Ver_Adaptadores
            break 
        }
        2{
            Informacion_Adaptador
            break
        }
        3{
            Habilitar_Adaptador
            break
        }
        4{
            Deshabilitar_Adaptador
            break
        }
        5{
            Renombrar_Adaptador
            break
        }
        6{
            Detalles_Router
            break
        }
        7{
            Write-Host "Saliendo..."
            break
        }
        }

}while($opc -ne 7)
}
catch{
    Write-Host "Ocurrio un Error"
    Write-Host $Error[0]    
}
Write-Host "Se salio exitosamente..."
Write-Host "Ocurrieron estos Errores"
Write-Host $Error
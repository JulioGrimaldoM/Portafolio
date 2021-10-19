function Ver_Adaptadores {
    Get-NetAdapter| ft Name, DriverName, DriverVersion, DriverFileName   
}
function Informacion_Adaptador {
    param([Parameter(Mandatory)] [string] $Nombre)
    Get-NetAdapter -Name $Nombre -ErrorAction "SilentlyContinue"
    
}
function Habilitar_Adaptador {
    param([Parameter(Mandatory)] [string] $Nombre)
    Enable-NetAdapter -Name $Nombre -ErrorAction "SilentlyContinue"
    
}
function Deshabilitar_Adaptador {
    param([Parameter(Mandatory)] [string] $Nombre)
    Disable-NetAdapter -Name $Nombre -ErrorAction "SilentlyContinue"
}
function Renombrar_Adaptador {
    param([Parameter(Mandatory)][string]$Nombre,[Parameter(Mandatory)][string]$Nuevo_Name)
    Rename-NetAdapter -Name $Nombre -NewName $Nuevo_Name -ErrorAction "SilentlyContinue"
}
function Detalles_Router {
    param([Parameter(Mandatory)][string]$Destino)
    Test-NetConnection $Destino -TraceRoute -ErrorAction "SilentlyContinue"
}
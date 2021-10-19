#! /bin/bash
Archivo=$1
function havepwend() {
i=1
while read line
do
  echo " "
  echo "Cuenta de $line"
  curl -H "hibp-api-key: $Apikey" -H "user-agent: PCL"  https://haveibeenpwned.com/api/v3/breachedaccount/"$line"?truncateResponse=false > cuentas"$i".json
  if [[ -s cuentas"$i".json ]]
  then
      echo " "
      echo "Si hay brechas de seguridad"
      echo " "
      cat cuentas"$i".json;
      echo " "
  else
      echo "No hay brechas de seguridad"
  fi
  i=$((i+1))
done < $Archivo
}
read -sp "Escribe Apikey: " Apikey
echo -e "\n"
havepwend $Apikey

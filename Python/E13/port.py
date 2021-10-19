import subprocess, argparse

info="""--------------- Ejemplos de Uso --------------- 
python port.py -ip "La ip" -p "Puerto" """
parser=argparse.ArgumentParser(description="Analizar puertos",
                                       epilog=info, formatter_class=argparse.
                                       RawDescriptionHelpFormatter)
parser.add_argument("-ip",metavar="IP", dest="IP",help="Ip del equipo",required=True)
parser.add_argument("-p", metavar="Puerto", dest="Puerto", help="Puerto para analizar", required=True)
args=parser.parse_args()

ips=args.IP
port=args.Puerto

try:
    comand="powershell -ExecutionPolicy ByPass -File Puertos_Abiertos.ps1 -ip \""+ips+"\" -p \""+port+"\""
    poweresults=subprocess.check_output(comand)
    print(poweresults.decode())
except Exception as e:
    print(str(e))

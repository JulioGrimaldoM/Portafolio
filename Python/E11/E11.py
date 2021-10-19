import argparse
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image


def ScrapingImg(url):
    print("Obteniendo imagenes de la url: "+ url)
    try:
        response = requests.get(url)  
        parsed_body = html.fromstring(response.text)
        images = parsed_body.xpath('//img/@src')
        print ('Imagenes %s encontradas' % len(images))
        os.system("mkdir imagenes")
        for image in images:
            if image.startswith("http") == False:
                download = url + image
            else:
                download = image
            r = requests.get(download)
            f = open('imagenes/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
    except Exception as e:
        print("Error de conexion con " + url)
        print(str(e))

def Metadata(ruta):
    try:
        os.chdir(ruta)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                f=open("%s.txt"%(name),"a")
                print(os.path.join(root, name))
                print ("[+] Metadata for file: %s " %(name))
                f.write("[+] Metadata for file: %s " %(name))
                try:
                    exifData = {}
                    exif = get_exif_metadata(name)
                    for metadata in exif:
                        print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                        f.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    print ("\n")
                except:
                    import sys, traceback
                    traceback.print_exc(file=sys.stdout)
    except Exception as e:
        print("Ocurrio un error")
        

def decode_gps_info(exif):
    try:
        gpsinfo = {}
        if 'GPSInfo' in exif:
            Nsec = exif['GPSInfo'][2][2] 
            Nmin = exif['GPSInfo'][2][1]
            Ndeg = exif['GPSInfo'][2][0]
            Wsec = exif['GPSInfo'][4][2]
            Wmin = exif['GPSInfo'][4][1]
            Wdeg = exif['GPSInfo'][4][0]
            if exif['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            if exif['GPSInfo'][3] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
            exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

    except Exception as e:
        print("Ups ocurrio un error")
        
def get_exif_metadata(image_path):
    try:
        ret = {}
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
        decode_gps_info(ret)
        return ret
    except Exception as e:
        print("Ocurrio un error"+str(e))

        
if __name__=="__main__":
    try:
        Opciones=""" Sxript Metadata
        Ejemplos de uso
        python E11.py -url "Link de la pagina" """
        parser=argparse.ArgumentParser(description="Scrip Metadata",epilog=Opciones, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-url", metavar="Url", dest="Url", help="Link de la pagina web", required=True)
        params=parser.parse_args()
    
        link=params.Url.encode()
        ScrapingImg(link.decode())
        ruta=os.path.abspath("imagenes")
        Metadata(ruta)
    except Exception as e:
        print("Ocurrio el siguiente error "+str(e))

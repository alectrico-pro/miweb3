#!/usr/bin/env python
import sys, requests, json, web3
from eth_tester import EthereumTester

payload       =  {'api_key': 'MIcd7Mas45NENV8FutQaQdMFw4lXh7hk05acCsrV'}
url           =  'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos'
key           =  'latest_photos'
max_reg       =  25

def build_web_page(fotos):
   #Construye un segmento html que muestra fotos
   webpage = "<html> <head> </head> <body> <ul>"
   cont = 1
   for foto in fotos:
       webpage = webpage + "<li> <img src =" + foto['img_src'] + "></li>" 
       cont += 1
   print("Registros procesados:" )
   print( cont )
   webpage = webpage + "</ul> </body> </html>"
   return webpage

response  =  requests.get( url, params=payload )

if ( response.status_code == 200 ):
    fotos = response.json()[key][1: max_reg]
    html  = build_web_page(fotos)
    #print( html )
    f     = open( 'index.html', 'w')
    f.writelines( html)
    f.close()
 
else:
  print("Ocurrió un error al bajar las fotos")








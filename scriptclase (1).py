
import urllib.request
import requests
import os 

updateURL= "curl -X GET https://ipv4.api.hosting.ionos.com/dns/v1/dyndns?q=N2IyY2IxMzcxY2QzNGUyYTlkMzZmODU0MDZkYjk1MjkuS0I4eGVIQkhwR2ZmVVM5R09aM2RDejQwQ2VvenZxQXA1cFlSMDBINFpDdnhnOVRYdF90OTFiM2UwTXJUX21SbVRCQVJCeF8tLUFUMHJfTjJsZ1lCekE"
#SACAMOS MI IP PUBLICA DE TIMOFONE

mi_ip=urllib.request.urlopen('https://ident.me').read().decode('utf-8')

ip_log = open('log_ip.txt','r')

with open('log_ip.txt','w') as f:
    f.write(mi_ip)

if(mi_ip!= ip_log):
   os.system(updateURL)
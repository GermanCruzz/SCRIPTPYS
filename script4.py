
# Script para crear un fichero .htaccess

import sys
import os
import hashlib

password = sys.argv[4]


if len(sys.argv) !=6:
        print("El programa necesita 6 argumentos.")
        sys.exit(1)
else:  
    file = open(sys.argv[1])
    #print(sys.argv[0])
    f = open(sys.argv[1]+"\.htaccess","w")
    f.write(f"{sys.argv[3]}:{sys.argv[4]}")
    f.write("DirectoryIndex "+sys.argv[2])
    f.write( "AuthName \"Dialog prompt\"")
    f.write("AuthType Basic")
    f.write({sys.argv[1]} + "\.htpasswd")
    #option indexes
    f.write("")
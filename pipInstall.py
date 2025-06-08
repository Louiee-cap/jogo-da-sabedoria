import sys
import subprocess
import os

try:
    import mysql.connector

except ImportError:
    print("Instalando dependencias")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector-python"])
        print("Reiniciando o programa")
        os.execv(sys.executable, [sys.executable] + sys.argv)
        
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao instalar a biblioteca.")
        print("Por favor, tente instalar manualmente usando 'pip install mysql-connector-python'")
        sys.exit(1)

#Louie, coloca isso aqui no código principal
#Se precisar de mais pip installs só adicionar aqui
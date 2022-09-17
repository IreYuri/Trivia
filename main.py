import random #Importamos la libreria random
import time #Tiempo

#COLOR
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
RED = '\033[31m'

#ESTILO
NORMAL = '\x1b[0;m'
YELLOWFONDO = '\033[1;33;43m'
WHITENEGRITA = '\x1b[1;37m'
WHITECURSIVA = '\033[3;37m'
GREENTACHADO = '\x1b[7;32m'
BLUECURSIVA = '\033[3;34m'



# BIENVENIDA A LA TRIVIA DE JUJUTSU KAISEN - ANIME
print(YELLOWFONDO + "✦✦✦  BIENVENIDO A MI TRIVIA DEL ANIME JUJUTSU KAIZEN  ✦✦✦\n" + NORMAL)
print(WHITECURSIVA + "Aqui pondras a prueba tus conocimientos con 10 PREGUNTAS del anime, yeih!!\n" )

#Preguntaremos su nombre
print("Mi nombre es Steffi-chan y te acompañare en esta travesia! \n " )
n = input( "Cuentame, ¿Como quieres que te llame?\n")
name = n.capitalize()
print("\nHi, %s." % name )
print("ENCANTADA DE CONOCERTE!! UWU")

# Es importante dar instrucciones sobre cómo jugar:
print( WHITENEGRITA +
"\nTe cuento %s," %name,"antes de iniciar la travesia de sabiduria,  necesitas saber esto... \n")

print(
    "Responder las siguientes preguntas escribiendo la letra de la alternativa en minuscula y presionando 'Enter' para enviar tu respuesta: \n" + NORMAL)

#Preguntamos los animos 
ready = input("¿Estas listo? Pon SI para avanzar --> ")

while ready not in ("yes", "si", "SI","Si", "YES"):
  ready = input("No quieres jugar? Dime que SI --> ")

#variables esenciales
points = 0
start_trivia = True 
intentos = 0
listpoints = []

#CONTADOR DE INICIO
print('\nInicia en...')
for t in range(5,0,-1):
  print(t)
  time.sleep(1)
print()
print("\n EMPECEM000S!! ヽ (o ^ – ^ o) ノ")
print()
print ("INICIAS CON", points," PUNTOS, VEAMOS CUANTOS PUNTOS CONSIGUES!")
print()
time.sleep(2)
print()

#---INICIO DEL CICLO DE LA TRIVIA---
while start_trivia == True: #si es True; se repite el ciclo
  intentos += 1
  points = 0

  print("\nNúmero de Intento:", intentos)
  input("Dale ENTER para continuar")
  print()
  

  # INICIO DE PREGUNTAS
  questions = []
  
  # Pregunta 1
  q_1 = "1) ¿Dónde se encuentra la escuela secundaria de Yuji Itadori? "
  print(MAGENTA , q_1 , RESET)
  print(CYAN)
  print("  a) Estudio conmigo")
  print("  b) Kioto")
  print("  c) Sugisawa")
  print("  d) Seul")
  print(RESET)


  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_1 == "c" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO +"Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  #Agregando a la lista de resultado
  listpoints.append(points)

  #Tiempo entre preguntas:
  time.sleep(2)
    
  # Pregunta 2
  q_2 = "2) ¿Cómo se llama la extensión de dominio de Sukuna? " 
  print(MAGENTA + q_2 + NORMAL)
  print(CYAN)
  print("  a) La Rosa de Guadalupe nivel dios")
  print("  b) Santuario malevólo")
  print("  c) Reino demoniaco")
  print("  d) Autoencarnacion bebito fiu fiu")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_2 == "b" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL )
  print()
  listpoints.append(points)
  time.sleep(2)
    
  # Pregunta 3
  q_3 = "3) ¿Cuál es el apodo de Satoru Gojo? "
  print(MAGENTA + q_3 + RESET)
  print(CYAN)
  print("  a) El chaman mas fuerte")
  print("  b) El tigre de la universidad")
  print("  c) El invencible")
  print("  d) El hijo de Medusa")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_3 == "a" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)

  # Pregunta 4
  q_4 = "4) ¿A que se dedica Yoshinobu Gokuganji? "
  print(MAGENTA + q_4 + RESET)
  print(CYAN)
  print("  a) Instructor del colegio de Tokio")
  print("  b) Director del colegio de Kioto")
  print("  c) Suplente de enfermeria")
  print("  d) Sensei de Class Assassination")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_4 == "b" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)

  # Pregunta 5
  q_5 = "5) ¿Quien no esta en segundo año? "
  print(MAGENTA + q_5 + RESET)
  print(CYAN)
  print("  a) Maki Zenin")
  print("  b) Mikaela Yu")
  print("  c) Aoi Todo")
  print("  d) Yo, no pase de año")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_5"
  respuesta_5 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_5 == "c" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)

  # Pregunta 6
  q_6 = "6) ¿Cuántos dedos de Sukuna tiene en su poder Suguru Geto? "
  print(MAGENTA + q_6 + RESET)
  print(CYAN)
  print("  a) No se sabe, se esta esperando la segunda temporada")
  print("  b) 5")
  print("  c) No lei el manga")
  print("  d) 6")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_6"
  respuesta_6 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_6 not in ("a", "b", "c", "d"):
    respuesta_6 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_6 == "a" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)

  # Pregunta 7
  q_7 = "7) ¿Cómo se llama el padre de Megumi Fushiguro? "
  print(MAGENTA + q_7 + RESET)
  print(CYAN)
  print("  a) Tenemos el mismo padre")
  print("  b) Alan Garcia")
  print("  c) Tsumiki Fushiguro")
  print("  d) Toji Fushiguro")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_7"
  respuesta_7 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_7 not in ("a", "b", "c", "d"):
    respuesta_7 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_7 == "d" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)
    
  # Pregunta 8
  q_8 = "8) ¿Dónde solía vivir Nobara Kugisaki? "
  print(MAGENTA + q_8 + RESET)
  print(CYAN)
  print("  a) Era mi vecina del cerro")
  print("  b) En el campo")
  print("  c) En un departamento de 8x8")
  print("  d) En Tokio")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_8"
  respuesta_8 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_8 not in ("a", "b", "c", "d"):
    respuesta_8 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_8 == "b" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)
  
  # Pregunta 9
  q_9 = "9) ¿ Como se llama el espíritu maldito que tiene Itadori y que se comió para tenerlo? "
  print(MAGENTA + q_9 + RESET)
  print(CYAN)
  print("  a) Inuyasha - un dedo")
  print("  b) Sukune - un chaufa")
  print("  c) Tomoe - una serpiente")
  print("  d) Sukuna - un dedo")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_9"
  respuesta_9 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_9 not in ("a", "b", "c", "d"):
    respuesta_9 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_9 == "d" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)

  # Pregunta 10
  q_10 = "10) ¿ Que animales son los shikigamis de Megumi Fushiguro? "
  print(MAGENTA + q_10 + RESET)
  print(CYAN)
  print("  a) Winnie Pooh y Tiger")
  print("  b) Lobos y zorros")
  print("  c) Tucanes y cocodrilos")
  print("  d) Perros y sapos")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_10"
  respuesta_10 = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_10 not in ("a", "b", "c", "d"):
    respuesta_10 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  # Verificacion de respuesta correcta o incorrecta.
  if respuesta_10 == "d" :
    suerte = random.randint(1,10)
    points += suerte
    print("Correcto %s" %name, "HAZ GANADO PUNTOS! 🌟 \n")
  else:
    suerte = random.randint(1,10)
    points -= suerte
    print("UY! Incorrecto %s" %name ,"PERDISTE PUNTOS!  \n")
    print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  listpoints.append(points)
  time.sleep(2)
  

  #AGREGAR LAS PREGUNTAS EN LA LISTA:
  questions.append(q_1)
  questions.append(q_2)
  questions.append(q_3)
  questions.append(q_4)
  questions.append(q_5)
  questions.append(q_6)
  questions.append(q_7)
  questions.append(q_8)
  questions.append(q_9)
  questions.append(q_10)

  #LISTA DE ANSWERS:
  answers = ['Sugisawa','Santuario malevólo','El chaman mas fuerte','Director del colegio de Kioto','Aoi Todo','No se sabe, se esta esperando la segunda temporada','Toji Fushiguro','En el campo','Sukuna - un dedo','Perros y sapos']
  
  #MOSTRAR LAS PREGUNTAS:
  input("DALE ENTER PARA CONOCER LA RESOLUCION\n")
  for resultado in range(0,10):
    print(RED + "RESOLUCIÓN:" + RESET)
    print("-",questions[resultado], "\nLa respuesta es: " ,answers[resultado])

  
  #MOSTRAR SUS PUNTAJES EN ORDEN:
  print(BLUECURSIVA +"\nDurante todo el juego estos fueron tus puntajes: ", listpoints )
  print(NORMAL)
  time.sleep(2)
  

  # COMODIN
  print("COMODIN COMODIN!! AQUI PUEDES RECUPERARTE SI TUVISTE UNA MALA RACHA \n")
  print(MAGENTA +" ------ Escoge una letra  ----- "+ RESET)
  print(CYAN)
  print("  a) Zorro ")
  print("  b) Oso")
  print("  c) Trigre")
  print("  d) Gato")
  print(RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_puntosExtras"
  respuesta_puntosExtras = input("\nTu respuesta: ")

  # Validacion de respuesta en general.
  while respuesta_puntosExtras not in ("a", "b", "c", "d"):
    respuesta_puntosExtras = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
  print()

  numero_azar = int(input("Dime un numero entre 1 al 100: "))
  if numero_azar in range(1,101):
    if respuesta_puntosExtras == "a" :
      points = points * numero_azar
      print("%s" %name, " 🌟 \n")
    elif respuesta_puntosExtras == "b":
      points = points - numero_azar
      print("%s" %name, " 🌟 \n")
    elif respuesta_puntosExtras == "c":
      points = points / numero_azar
      print("%s" %name, " 🌟 \n")
    else:
      points = points * 100 * numero_azar
      print("%s" %name, " 🌟 \n")
  else:
    numero_azar = int(input("Dime un numero entre 1 al 100: "))
    
  time.sleep(2)

  #Despedida y muestra de puntaje total
  print(WHITECURSIVA +"\n WHOUU GRACIAS POR JUGAR MI TRIVIA, ME DIVERTI MUCHO CONTIGO!!")
  print("\n Y REBLOBLEEE DE TAMBORES (‘• ω • `) ♡"+ NORMAL)
  print(GREENTACHADO +"SU PUNTAJE FINAL ES DE ", points, "PUNTOS"+ NORMAL)
  print()

  #PREGUNTA SI DESEA REINTENTAR LA TRIVIA
  print(WHITECURSIVA +"\n¿Deseas intentar la trivia nuevamente?"+ NORMAL)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ")

  if repetir_trivia != "si":  
    start_trivia = False  # Para evitar que se repita.


#DESPEDIDA OFICIAL DE LA TRIVIA 
print(YELLOWFONDO +"  ✦✦✦ FIN DE TRIVIA ✦✦✦  "+ NORMAL)
time.sleep(1)
print( YELLOWFONDO +"  ✦✦✦ BYE ✦✦✦  "+ NORMAL)
print()

#FRASE DEL DIA:
frase = ['«No te preocupes si no funciona bien.\nSi todo lo hiciera, no tendrías trabajo.»\n-La ley de Mosher sobre la ingeniería de Software','«Cualquiera puede hablar. Enséñame el código.»\n-Linus Torvalds']
for number in range(0,2):
  print(frase[number])
  time.sleep(1)
  print()



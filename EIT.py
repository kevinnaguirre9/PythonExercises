import numpy as np

'''1. Escribir una función en Python que, dada una lista de números, devuelva otra lista
en orden inverso. Para realizar este ejercicio se deberá utilizar un bucle o estructura
repetitiva. No se permite el uso de funciones miembro de la clase list (en especial
list.reverse()).'''

def get_reverse_list(num_list):
  reversed_list = [num_list[i] for i in range(len(num_list)-1, -1, -1)]
  print(reversed_list)

my_list = [23, 48, 10, 15, 3, 90]
get_reverse_list(my_list)


'''2. Escribir una función que, dado un número entero N, devuelva una lista con todos los
números primos hasta N. Para solucionar el ejercicio debéis crear una función
auxiliar que indique si un determinado número es primo (retornando un valor
booleano).'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True

def obtener_primos(num):
  list_primos = [i for i in range(num+1) if es_primo(i)]   
  return list_primos


result = obtener_primos(100)
print(result)


'''3. Escribir una función que reciba una tupla compuesta por caracteres, y devuelva una
lista con los caracteres en mayúsculas. Debéis recorrer la tupla carácter a carácter
para realizar la conversión. Para convertir un carácter a mayúscula podéis usar el
método upper(). Por ejemplo ’a’.upper() nos devuelve ’A’.'''

def get_upper(tupla):
  char_upper = [char.upper() for char in tupla]
  return char_upper

print(get_upper(('a', 'b', 'c', 'd', 'Elena')))


'''4. Convertir el texto ’ejemplo’ en una lista que contenga sus 7 caracteres. Después
convertirlo en una tupla y usando la función del ejercicio anterior obtener una lista
con el texto en mayúsculas.'''


texto = 'ejemplo'
letters_list = [letter for letter in texto]

letters_tuple = tuple(letters_list)
print(get_upper(letters_tuple))


'''5. Escribir una función que, dada una lista de números, devuelva una lista con sólo los
elementos en posición par.'''

def get_elements(num_list):
  pares_list = [num_list[pos] for pos in range(2, len(num_list), 2)]
  return pares_list

result = get_elements([21, 48, 32, 101, 50, 49, 300, 39, 87, 18])
print(result)


'''6. Extender la función anterior para que, dada una lista y unos índices, nos devuelva la
lista resultado de coger sólo los elementos indicados por los índices. Por ejemplo si
tenemos la lista [1,2,3,4,5,6] y los índices [0,1,3] debería devolver la lista [1,2,4].'''

def get_elements_by_pos(num_list, indices):
  try:
    final_list = [num_list[i] for i in indices]
    return final_list
  except IndexError as err:
    print(err)

result = get_elements_by_pos([1,2,3,4,5,6], [0, 1, 3, 5])
print(result)


'''7. Escribir una función que nos devuelva cuántas veces aparece cada una de las
palabras de un texto (frecuencia de aparición de las palabras). Para ello podéis usar
un diccionario donde la llave sea cada una de las palabras del texto y el contenido
guarde el número de apariciones de la palabra. Para simplificar el ejercicio, podéis
usar el método split(’ ’), que, dado un separador (el espacio), nos devuelve una lista
con todas las palabras de un texto de forma separada. Por ejemplo: ’hola esto es un
ejemplo’.split(’ ’) nos devolvería: [’hola’, ’esto’, ’es’, ’un’, ’ejemplo’]'''


def get_frequence(text):
  text = text.split()
  dict_freq = {}

  for word in text:
    count = 0
    for i in range(len(text)):
      if word.lower() == text[i].lower():
        count += 1
    dict_freq.update({word: count})

  return dict_freq


result = get_frequence('Elena Sofía Fernández Balladares')
print(result)


'''8. Escribir una función que devuelva un conjunto formado por los números
compuestos (no primos) menores que un N dado.'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True

def obtener_compuestos(num):
  list_no_primos = [i for i in range(2, num+1) if not es_primo(i)] 
  return list_no_primos


no_primos = obtener_compuestos(100)
print(no_primos)


'''9. Realiza una función separar(lista) que tome una lista de números enteros y devuelva
dos listas ordenadas. La primera con los números pares y la segunda con los
números impares.'''

def separar(lista):
  pares = [i for i in lista if i%2 == 0]
  impares = [j for j in lista if j%2 != 0]

  return sorted(pares), sorted(impares)


pares, impares = separar([4, 17, 9, 8, 20, 37, 15, 51, 33, 86, 90, 18, 99, 27])
print('Números pares:', pares)
print('Números impares:', impares)


'''10. Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del
rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15
de base y 10 de altura.'''

def area_rectangulo(base:float, altura:float):
  area = base * altura
  return area

result = area_rectangulo(15, 10)
print('El área es:', result)


'''11. Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo
siguiente:
a. Si el primer número es mayor que el segundo, debe devolver 1.
b. Si el primer número es menor que el segundo, debe devolver -1.
c. Si ambos números son iguales, debe devolver un 0.
d. Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'''

def relacion(a:float, b:float):
  if a > b:
    return 1
  elif a < b:
    return -1
  elif a == b:
    return 0

result1 = relacion(5, 10)
result2 = relacion(10, 5)
result3 = relacion(5, 5)
print(result1)
print(result2)
print(result3)


'''12. Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva
su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y
24.'''

def intermedio(a, b):
  p_intermedio = (a + b) / 2
  return p_intermedio

p_int = intermedio(-12, 24)
print(p_int)


'''13. Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres
parámetros. El primero es el número a recortar, el segundo es el límite inferior y el
tercero el límite superior. La función tendrá que cumplir lo siguiente:
a. Devolver el límite inferior si el número es menor que éste
b. Devolver el límite superior si el número es mayor que éste.
c. Devolver el número sin cambios si no se supera ningún límite.
d. Comprueba el resultado de recortar 15 entre los límites 0 y 10.'''

def recortar(numero, minimo, maximo):
  if numero < minimo:
    return minimo
  elif numero > maximo:
    return maximo
  return numero

print(recortar(15, 0, 10))


'''14. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección
se considerará válida si contiene el símbolo "@"'''

def validate_email():
  email = input("Please, enter your email: ")
  if '@' in email:
    print('Valid email') 
  else:
    print('Invalid email') 
  
validate_email()


'''15. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
de sus dígitos (utilizando una función que realice dicha suma).'''

def sum_digits():
  while True:
    try:
      number = int(input('Please, enter a number: '))

      if number == 0:
        break

      suma = 0
      for digit in str(number):
        suma += int(digit)

      print(suma)
    
    except ValueError:
      print('Invalid input')
    
    
sum_digits()


'''16. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y
la suma de sus dígitos'''

def sum_digits(number):
  suma = 0
  for digit in str(number):
    suma += int(digit)

  return suma

def main():
  input_numbers = []
  while True:
    try:
      number = int(input('Please, enter a number: '))

      if number == 0:
        len_numbers = len(input_numbers)
        total_sum = sum(input_numbers)
        digits_total_sum = sum_digits(total_sum)
        print('Total números ingresados:', len_numbers)
        print('Sumatoria de todos los números ingresados:', total_sum)
        print('Sumatoria de todos los números ingresados:', digits_total_sum)
        break
      
      input_numbers.append(number)
      number_digits_sum = sum_digits(number)
      print(number_digits_sum)
    
    except ValueError:
      print('Invalid input')
  
main()
  

'''17. Requerir al usuario que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True


def main():
  try: 
    num = int(input("INGRESE UN NÚMERO: "))

    if es_primo(num):
      print("EL NÚMERO {} ES PRIMO".format(num))
    else:
      print("EL NÚMERO {} NO ES PRIMO".format(num))
  except:
      print("Error: El numero debe ser entero")


main()


'''18. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de
ocurrencias del dígito en el número, utilizando para ello una función que calcule la
frecuencia'''

def frecuencia():
  try:
    num = int(input("INGRESE UN NÚMERO: "))
    digit = int(input("INGRESE UN DÍGITO: "))

    freq = 0
    
    for d in str(num):
      if digit == int(d):
        freq += 1
    
    print("El número de ocurrencias del dígito {} en el número {} es: {} ocurrencias".format(digit, num, freq))

  except ValueError:
    print("ERROR: El número debe ser entero")


frecuencia()


'''19. Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al 
finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según 
sea necesario'''

def factorial(n):
  fact = n
  
  for i in range(n-1,1,-1):
    fact = fact * i
  return fact


def main():
  input_numbers = []
  while True:
    try:
      number = int(input('Please, enter a number: '))

      if number == 0:
        len_numbers = len(input_numbers)
        print('Total números leídos:', len_numbers)
        break
      
      input_numbers.append(number)
      fact = factorial(number)
      print('El factorial de {} es: {}'.format(number, fact))
    
    except ValueError:
      print('Invalid input')

main()


'''20. Escribir un programa que pida números positivos al usuario. Mostrar el número cuya
sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue
menor que 10. Utilizar una o más funciones, según sea necesario.'''

def sum_digits(number):
  suma = 0
  for digit in str(number):
    suma += int(digit)

  return suma

def main():
    numbers = np.array([], dtype=int)
    digits = np.array([], dtype=int)
    while True:
        try:
            print('---'*15)
            num = int(input('POR FAVOR, INGRESE UN NUMERO POSITIVO: '))

            if num < 0:
                print('Saliendo')
                break

            numbers = np.append(numbers, num)
            digits = np.append(digits, sum_digits(num))

            #Mostrar el número cuya sumatoria de dígitos fue mayor
            numbers_max_digit = [numbers[i] for i in range(len(digits)) if digits[i] == max(digits)]

            #cantidad de números cuya sumatoria de dígitos fue menor que 10
            less_than_ten = len(digits[digits < 10])

            print('Número(s) cuya sumatoria de dígitos fue la mayor cantidad: {}'.format(numbers_max_digit))
            print('cantidad de números cuya sumatoria de dígitos fue menor que 10: {} número(s)'.format(less_than_ten))

        except ValueError:
            print("Input no válido")

main()








'''21. Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un
número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También
solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True

def sum_digits(number):
  suma = 0
  for digit in str(number):
    suma += int(digit)
  return suma

def get_freq(num, digit):
  freq = 0
  for d in str(num):
      if digit == int(d):
        freq += 1
  return freq

def factorial(n):
  fact = n
  
  for i in range(n-1,1,-1):
    fact = fact * i
  return fact


def primos_sum_digits():
  input_numbers = []
  while True:
    try:
      print('--'*20)
      num = int(input("INGRESE UN NÚMERO PRIMO: "))

      if not es_primo(num):
        print('El número no es primo')
        if len(input_numbers) > 0:
          max_number = max(input_numbers)
          fact = factorial(max_number)
          print('A continuación se muestra el factorial del mayor número primo ingresado: ')
          print('El factorial de {} es: {}'.format(max_number, fact))
        break

      input_numbers.append(num)  

      sum = sum_digits(num)
      print('La suma de los dígitos es {}'.format(sum))

      digit = int(input("INGRESE UN DÍGITO PARA SABER EL NÚMERO DE OCURRENCIAS EN EL NÚMERO INGRESADO PREVIAMENTE: "))
      freq = get_freq(num, digit)
      print("El número de ocurrencias del dígito {} en el número {} es: {} ocurrencias".format(digit, num, freq))
    except ValueError:
      print('Error. Debe ingresar un número entero.')

  
primos_sum_digits()


'''22. Escribir una función que, dado un número de Cedula de Identidad, retorne True si el número
es válido y False si no lo es. Para que un número de DNI sea válido debe tener 10 dígitos.'''

def is_valid(cedula):
  if not len(cedula) == 10:
    return False
  return True

print(is_valid('0953665551'))


'''23. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se
considera que las palabras están separadas por uno o más espacios. También podría haber
espacios al principio o al final del string pasado por parámetro.'''

def get_last_word_len(word):
  word_split = word.split()
  last_len = len(word_split[-1])
  return last_len

get_len = get_last_word_len('      Sergio Díaz  ')
print(get_len)


'''24. Escribir un programa que permita al usuario obtener un identificador para cada uno de los
socios de un club. Para eso ingresará nombre completo y número de Cedula de cada socio,
indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.'''

def get_id():
    n = 0
    while True:
        n +=1
        print('---'*9)
        name = input('POR FAVOR, INGRESE EL NOMBRE COMPLETO DEL SOCIO: ')

        if(not (name and not name.isspace())):
            break

        cedula = input('INGRESA NÚMERO DE CÉDULA DEL SOCIO: ')
        id_socio = 'S-' + str(n)
        print('Identificador del socio:', id_socio)

get_id()

'''25. Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse
más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más
de un apellido, el usuario sólo ingresará uno.'''

def get_id():
    n = 0
    while True:
        n +=1
        print('---'*9)
        primer_nombre = input('POR FAVOR, INGRESE EL PRIMER NOMBRE DEL SOCIO: ')
        if(not (primer_nombre and not primer_nombre.isspace())):
            break

        preguna = input("¿DESEA ESCRIBIR UN SEGUNDO NOMBRE? (S/N): ")
        if preguna.lower() == 's':
            segundo_nombre = input('POR FAVOR, INGRESE EL SEGUNDO NOMBRE DEL SOCIO: ')
        
        apellido = input('POR FAVOR, INGRESE EL PRIMER APELLIDO DEL SOCIO: ')   

        cedula = input('INGRESA NÚMERO DE CÉDULA DEL SOCIO: ')
        id_socio = 'S-' + str(n)
        print('Identificador del socio:', id_socio)

get_id()


'''26. Se debe validar que el número de CI tenga 10 dígitos. En caso contrario, el programa debe
dejar al usuario en un bucle hasta que ingrese una Cedula correcta.'''

def is_valid(cedula):
  if not len(cedula) == 10:
    return False
  return True

def get_id():
    n = 0
    while True:
        n +=1
        print('---'*9)
        primer_nombre = input('POR FAVOR, INGRESE EL PRIMER NOMBRE DEL SOCIO: ')
        if(not (primer_nombre and not primer_nombre.isspace())):
            break

        preguna = input("¿DESEA ESCRIBIR UN SEGUNDO NOMBRE? (S/N): ")
        if preguna.lower() == 's':
            segundo_nombre = input('POR FAVOR, INGRESE EL SEGUNDO NOMBRE DEL SOCIO: ')
        
        apellido = input('POR FAVOR, INGRESE EL PRIMER APELLIDO DEL SOCIO: ')   
        cedula = input('INGRESA NÚMERO DE CÉDULA DEL SOCIO: ')

        while not is_valid(cedula):
            cedula = input('INGRESA UN NÚMERO DE CÉDULA DEL VÁLIDO: ')
        
        id_socio = 'S-' + str(n)
        print('Identificador del socio:', id_socio)

get_id()


'''27. Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer
nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su CI. Ejemplo:
'''

def is_valid(cedula):
  if not len(cedula) == 10:
    return False
  return True

def get_id():
    n = 0
    while True:
        n +=1
        print('---'*18)
        primer_nombre = input('POR FAVOR, INGRESE EL PRIMER NOMBRE DEL SOCIO: ')

        if(not (primer_nombre and not primer_nombre.isspace())):
            break

        pregunta = input("¿DESEA ESCRIBIR UN SEGUNDO NOMBRE? (S/N): ")
        pregunta = pregunta.lower()
        while pregunta not in ['s', 'n']:
            pregunta = input("¿DESEA ESCRIBIR UN SEGUNDO NOMBRE? (S/N): ")

        if pregunta == 's':
            segundo_nombre = input('POR FAVOR, INGRESE EL SEGUNDO NOMBRE DEL SOCIO: ')
        
        else:
            segundo_nombre = ''
        
        apellido = input('POR FAVOR, INGRESE EL PRIMER APELLIDO DEL SOCIO: ')   
        cedula = input('INGRESA NÚMERO DE CÉDULA DEL SOCIO: ')

        while not is_valid(cedula):
            cedula = input('INGRESA UN NÚMERO DE CÉDULA VÁLIDO (10 dígitos): ')
        
        id_socio = primer_nombre.upper() + str(len(apellido)) + cedula[:3]

        if segundo_nombre != '':
            nombre_completo = primer_nombre + ' ' + segundo_nombre + ' ' + apellido
        else:
            nombre_completo = primer_nombre + ' ' + apellido

        print('**'*18)
        print('Nombre: {}'.format(nombre_completo))
        print('CI: {}'.format(cedula))
        print('Identificador del socio:', id_socio)
        print('**'*18)

get_id()


'''28. Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra
de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás
caracteres. Precondición: el separador de palabras es el espacio: " ".'''

def to_title(text):
    text_split = text.split()
    title_words = []

    for word in text_split:
        new_word = ''
        new_word += word[0].upper()
        new_word += word[1:len(word)].lower()        
        title_words.append(new_word)

    title_words = " ".join(title_words)
    print(title_words)


to_title('kEvin      natAnEel  agUIrre      sÁncheZ')
        
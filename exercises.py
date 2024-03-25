#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

my_string = "This is a string"
my_number = 547
my_list = ['one', 'two', 'three', 'four', 'five']
my_boolean = True


#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.

first_3_letters = my_string[:3]


#Exercise 3: Use an index to grab the first element from your list.

first_element = my_list[0]


#Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = my_number + 10


#Exercise 5: Use an index to get the last element in your list.

last_element = my_list[-1]


#Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'

names_list = names.split(',')


# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

first_word = my_string[:4]

new_string = first_word.upper() + my_string[4:]


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(f"My number is {my_number}")


# Exercise 9: Print “hello world”.

print("hello, world")


# Ejercicio extra: Crear una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

my_string = 'Entró y lo primero que hizo fue decir "Hola".'

word_index = my_string.find('Hola')

my_string = my_string.replace('Hola', 'adiós')
# Variables
from cmath import pi


my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, my_int_to_str_variable, my_bool_variable)

print("Este es el valor de:", my_bool_variable)

# Variables en una sola linea
name, surname, alias, age ="Mariela", "Benitez", "Marie", "24"
print("Me llamo:", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)
# Algunas Funciones del sistema
print(len(my_variable))


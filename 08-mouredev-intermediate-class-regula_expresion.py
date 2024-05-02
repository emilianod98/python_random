import re

my_string = "Esta es la lección número 8:\nLección de Expresiones Regulares"
my_other_string = "Esta no es la lección número 7: Manejo de ficheros"


### match ###
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string, re.I)
# if not(match == None): #Otra forma de hacerlo de comprobar el None
# if match != None: #Otra forma de hacerlo de comprobar el None
if match is not None: #Otra forma de hacerlo de comprobar el None
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

### search ###
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

### findall ###
findall = re.findall("lección", my_string, re.I)
print(findall)

### split ###
print(re.split("\n", my_string))
print(re.split(":", my_other_string))

### sub ###
print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("[L|l]ección", "LECCIÓN", my_string))

### Patterns ###
pattern = r'[Ll]ección'
print(re.findall(pattern, my_string))

pattern = r'[Ll]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

###  
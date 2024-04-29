### File Handling ###

import os

# .txt file
file_txt = open("./filers/07-file.txt", "w+") # W+ -> Write + Read
file_txt.write("Nombre: Julio\nApellido: Roca\n50 Años\nLenguaje C+, R, SQL")

# Coloca el cursor al principio del archivo antes de leer
file_txt.seek(0)

print(file_txt.readline())

for x in file_txt.readlines():
    print(x)

# Coloca el cursor al final del archivo antes de escribir
file_txt.seek(0, os.SEEK_END)

file_txt.write("\nY otros conocimientos en HTML & CSS")
file_txt.seek(0)  # Coloca el cursor al principio del archivo antes de leer

print(file_txt.readline())

file_txt.close()
# os.remove("./filers/07-file.txt")


# .json file
import json

# Abre el archivo en modo escritura
with open("./filers/07-file.json", "w+") as file_json:
    json_text = {
        "name": "Julio",
        "surname": "Roca",
        "age" : 50,
        "lenguaje": ["C+", "R", "SQL"],
        "website": "https://jroca.dev",
        "email": "jroca@gmail.com",
        "phone": "123456789",
    }

    # Escribe el JSON serializado en el archivo
    json.dump(json_text, file_json, indent=2)
    file_json.close()

# Abre el archivo en modo lectura
with open("./filers/07-file.json", "r") as file_json:
    # Deserializa el JSON
    json_text = json.load(file_json)

    # Imprime el JSON deserializado
    print(json_text)
    print(json_text["name"])   
    print(type(json_text))

    file_json.close()

# .csv file
import csv
file_csv = open("./filers/07-file.csv", "w+")
file_csv_writer = csv.writer(file_csv)
file_csv_writer.writerow(["name", "surname", "age"])
file_csv_writer.writerow(["Julio", "Roca", 50])
file_csv_writer.writerow(["Julia", "Sosa", 28])


# with open("./filers/07-file.csv") as fil_csv:


# .xlsx file
# import xlrd #instalar modulo

# .xml file
import xml
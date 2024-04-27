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
        "lenguaje": "C+",
        "website": "https://jroca.dev",
        "email": "jroca@gmail.com",
        "phone": "123456789",
    }

    # Escribe el JSON serializado en el archivo
    json.dump(json_text, file_json, indent=2)

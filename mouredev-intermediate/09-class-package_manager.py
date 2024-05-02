### PYTHON PACKAGE MANAGER ###

# PIP

# pip --version
# (python 3.12)

# pip install numpy
import numpy

import mypackage.arithmetics
print(numpy.version.version)
# pip install pandas
import pandas as pd
print(pd.__version__)
# pip install matplotlib
import matplotlib as mpl
print(mpl.__version__)
# pip install requests
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=150')
print(response)
print(response.status_code)
print(response.json())

#

# pip list
# Package               Version
# --------------------- --------------
# Flask                 3.0.3
# numpy                 1.26.4
# pip                   24.0

#pip unistall numpy
#pip unistall pandas
#pip unistall matplotlib

#### PYTHON VIRTUAL ENVIRONMENT ###

# VIRTUAL ENVIRONMENT           (Crear entorno virtual)
# python3 -m venv venv 
# source venv/bin/activate      (Activar el enorno virtual)
# deactivate                    (Desactivar el enorno virtual)

# pip freeze > requirements.txt
# pip install -r requirements.txt

### PACKAGE ARITHMETICS ###
import mypackage
# print(mypackage.arithmetics.sum(2,4))
# print(mypackage.arithmetics.sum(12,4))
from mypackage import arithmetics 
print(arithmetics.sum(2,4))
print(arithmetics.sum(12,4))
# **Python PIP**

## What is PIP?
PIP is a package manager for Python packages, or modules if you like.
*Note: If you have Python version 3.4 or later, PIP is included by default.*

## What is a Package?
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

## Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:

**Check PIP version:**
```C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version```

**Install PIP**
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

**Download a Package**
Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
Navigate your command line to the location of Python's script directory, and type the following:
```C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase```

**Using a Package**
Once the package is installed, it is ready to use.
Import the "camelcase" package into your project.

```
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```

**Find Packages**
Find more packages at https://pypi.org/.

**Remove a Package**
Use the uninstall command to remove a package:

```C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase```

The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:

```
Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
Proceed (y/n)?
```

Press **y** and the package will be removed.

**List Packages**
Use the list command to list all packages that are currently installed:

```C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list```

Result:
```
Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1
```
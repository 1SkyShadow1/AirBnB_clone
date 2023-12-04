		#0x00.AirBnB clone - The console

This is a clone to the AirBnB web Application that has functionality resembling the well known AirBnB web Apllication

## Contents

[Title](#0x00.AirBnB clone - The console)
[Description](#description)
[Table of Contents] (#contents)
[Installation] (#installation)
[Usage](#usage)
[Testing](#Tests)
[Authors](#Authors)

## Installation
1. Clone this repository: 

git clone https://github.com/JonaNdawula/AirBnB_clone.git

2. Navigate to the project directory:

cd AirBnb_clone

3. To Execute the console:

./console.py

### Execution 

interactive mode 
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
=======================================

EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$

non-interactive mode
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
=======================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
=======================================
EOF help quit
(hbnb)
$

##Tests

unittest module
file extension .py
prefix of testing folders: test_
Execution: python3 -m unittest discover test

### Run the test in interactive mode

echo "python3 -m unittest discover tests" | bash

### Run test in non-interactive mode

echo python3 -m unittest discover texts

## Authors:

- [Evans Ncube](https://github.com/1SkyShadow)
- [Jonathan Ndawula](https://github.com/JonaNdawula)


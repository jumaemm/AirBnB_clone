# AirBnB Clone
---
This is the first step of implementing an AirBnB clone style project.
The first phase consists of creating an interactive console for the project and implementing the models required for the full project as well as handling file storage.

## Components
---
    - BaseModel Class
    - Subclasses
        - User
        - Amenity
        - Review
        - State
        - City
        - Place
    - Command Interpreter

## Directions
---
The command interpreter can be started by executing the ***console.py*** file. The command interpreter cna then be used to **create**, **update**, **destroy**, and show all instances of a particular class or all classes. Additional details can be obtained by using the **help** command.

#### Example Usage:

    vagrant@ubuntu-focal:~$ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit update destroy all show

    (hbnb) help quit
    Quit command to exit the program
    (hbnb) quit
    vagrant@ubuntu-focal:~$

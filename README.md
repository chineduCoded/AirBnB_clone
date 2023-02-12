# AirBnB clone - The console<br/>
![hbnb image](https://res.cloudinary.com/dtzzqvuzs/image/upload/v1675740710/Github/git_image1_pi5d6q.png)
# Table of Contents
* Description
* Purpose
* Requirements
* File Structure
* Usage Examples
* Bugs
* Authors
* Licence

# Description
![architecture map](https://res.cloudinary.com/dtzzqvuzs/image/upload/v1675742665/Github/git_image2_q3obv3.png)

This is the first step towards building full web application: the AirBnB clone. This first step is very important because it will be used to build during the project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

# What’s a command interpreter?
A command interpreter allows the user to interact with a program using commands in the form of text lines. But in our case we will use python module called `cmd` to manage the objects of the project:
* Create a new object (ex: a new User or new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# Purpose
The purpose of this project is to understand how to:<br/>
* create a Python package
* create a command interpreter using the cmd module
* serialize and deserialize a Class
* write and read a JSON file
* manage `datetime`
* use `*args` and `**kwargs`
* handle named arguments in a function
# Execution

## Interactive Mode
<pre>
<code>
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit<br/>
(hbnb)
(hbnb)
(hbnb) quit
$
</code>
</pre>

## Non-Interactive Mode
<pre>
<code>
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
</code>
</pre>

#Authors
*Chinedu Elijah Okoronkwo <chinedujohn17@gmail.com>
*Patrick Victor Ugochukwu <iampatrickugo@gmail.com>









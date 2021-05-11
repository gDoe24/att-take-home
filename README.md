# AT&T Take Home

## Getting Started

* Begin by navigating to the downloaded .zip folder in which the project is stored via the command line
* Start a Python interactive session by typing in `python` or `python3` depending on your installation, then hit enter.

Here is an example of what it would look like on Linux
```
$ python
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

* Import all classes and functions from app.py

Run:
```
>>> from app import *
```

## Operations
Now we are set up to begin adding animals.
The input format is going to be a string with commas and **no spaces** separating each field in the following order:

* name: string
* color: string
* species: string (dog/cat/sheep)
* birthday: string formatted as MM/DD/YYYY 
    * ex. "04/13/2011"

Ex. `Happy,blue,cat,08/15/2016`

The add_animals() function is the driving function for adding animal objects. The function, add_animals, continues a loop asking the user to input the string which represents the animal they wish to add and wether or not they would like to continue. The function prints the oldest animal of the most common species, "NAME, the COLOR SPECIES says SOUND!".

*Note: An invalid birthday will cause the animal to not be created.*
      *An invalid species will cause the animal to not be created*
      *Any input other than Y will be considered as N*
      

Ex.
```
>>> add_animals()
Please input your animal: Erza,red,cat,08/14/2014
Continue with more animals? (Y/N): Y
Please input your animal: Happy,blue,cat,08/15/2016
Continue with more animals? (Y/N): n
Please input your animal: Natsu,black,dog,08/15/2016
Continue with more animals? (Y/N): n
```
Prints:
```
Erza, the red cat says meow!
```

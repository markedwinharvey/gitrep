gitrep.py is a python (2.7) script to simplify the creation of new repositories on github from the command line. 

gitrep.py prompts to save user_name and token data into a file called user_data.p, which will be retrieved when gitrep.py is run again. 
Saving the data is optional. 

To streamline repo creation and avoid unnecessary script copying, I invoke gitrep.py from a folder in my home directory, using a bash function `gitrep`.  

function in .bashrc:

gitrep () {
	python ~/p/gitrep.py
}

Now typing the command `gitrep` runs the python script using the previously-saved credentials to create a new repo from within any target directory. 

################################
README for using the CreateSlotTypeFromList.py file
---------------------------------------------------

This python script will generate a .JSON and .zip file for importing ito amazon lex

#####
RUNNING THE SCRIPT
#
You call the function in the command line in the following manner:
$ python CreateSlotTypeFromList.py [inputList] [outputFileName]
	for example:
		
		$ python CreateSlotTypeFromList.py ListOfCarManufacturers.txt CarManufacturers_Lex

	The List used in the example is supplied in the lab directory for you to try this out with.
	
#####
THE LIST FILE
#
The File you supply the python script must take the format of:

line 1 contains the name of the slot type
line 2 contains the slot type description
line 3 containts the valueSelectionStrategy(either: ORIGINAL_VALUE or TOP_RESOLUTION)
line 4 onwards is just each value line by line

see the example file: ListOfCarManufacturers.txt for further clarification

#####
IMPORTING INTO LEX
#
To import the .zip file, you must press the blue + symbol in the [slot types] tab in amazon lex.
Then select [Import Slot Type]
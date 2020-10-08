# Python program to add card to trello.com


## Description

This Python CLI code which will add the card to trello.com. This program take user input to add a Trello card with labels and a comment to the specified column of board.

## Requirements

- Python 3.7
- Python packages

  - requests (v 2.22.0)
  - json

 ## How to run

To run the code go to trello/main.py:
  python -m trello.main
  
  - Enter the card name: (considered as string)
  - Enter the label: (string)
      - Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime
      - To create new label enter label name and color in given format = new_label:blue (color should be given from above valid value)
  - Enter list name: (string)
  
 ## Sample
 
 - Create card with existing label and list
   - Enter the card name: task_one
   - Enter the label: blue
   - Enter list name: Done
   
 - Create card with custom label and list
   - Enter the card name: task_two
   - Enter the label: blue,custom_lb1:red,sky
   - Enter list name: custom_list1
   
 ## Details
 
 - To add card you required Key, Token and Board id which is at moment incorporated in code.
 - User will provide input to create card with card name, label, and column
	- Card Name:(data type)string
	- Label:(data type)string
	  - Multilple labels can be passed. If its not present with specific format you can create new label and attach it to card
	  - custom label format : name of label:color(color can be selected from valid color values)
	- Column: (data type)string
		- If column in not available on board then it will create new column with specified column name and then card to it.


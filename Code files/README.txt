- For running the code follow the below procedures:
First check if your local machine have nltk and python installed. Make sure you
download "averaged_perceptron_tagger", "punkt", "wordnet". For this you
uncomment 3 to 5 lines in utlities.py file.

After this just type "python3 main.py" for running the code and it will give the 
output in output.txt file.


- For adding new natural language input follow below procedure:
-----input.txt---------
Each line in this file corresponds to one input sentence. This file can
be manipulated according to the users. 


- For adding new rule follow the below procedure:
-----rules.txt file---------

In this file, we can add new rules if there is new type of English Sentence.
Add a new rule in the new line at the bottom
Format of Input - {English Pattern} predicate1,predicate2 constant1,constant2

-----rules.py file--------

After the rule in the rules.txt file, add the FOL representation of that rule. 
Name the function of rule corresponding to the line number in rules.txt file.
Example- If we add a rule in 13th line of rules.txt file then the function name 
        in rules.py file will be "rule_13".


- For adding the correct form of predicates:
-----predicates.txt--------

Add the correct form of a predicate in a new line in this file.
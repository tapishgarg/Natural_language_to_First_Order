from utilities import *
from rules import *    

def main():

    all_predicates = get_all_predicates('./Data/predicates.txt')

    sentences = get_inputs('./Data/input.txt')
    
    rules = get_rules('./Data/rules.txt')
    
    results = []
    for sentence in sentences:
    
        txt = getPosTag(sentence)

        values = find_predicates_and_constants(txt, rules, all_predicates)
        if values is not None:
            predicates, constants, rule_no = values
            result = eval("rule_" + str(rule_no) + "(predicates, constants)")
            results.append(result)
            print(result)
        else:
            results.append("No rule matches")
            print("No rule matches")
        
       
        
    with open("./Data/output.txt", "w") as f:
        f.writelines("\n".join(results))

if __name__ =="__main__":
    main()


 

import nltk
import re
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')


# Input = "Mary teaches Maths"
# Output = "Mary/JJ teaches/NNS Maths/NNS"
def getPosTag(s):
  tokens = nltk.word_tokenize(s)
  ps = nltk.pos_tag(tokens)
  result = ""
  result = result + ps[0][0]
  result = result + "/" + ps[0][1]
  for i in range(1, len(ps)):
    result = result + " " + ps[i][0]
    result = result + "/" + ps[i][1]
  print(result)
  return result

# Input = "courses"
# Ouput = "course"
def lemmatize(token):
    lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
    return lemmatizer.lemmatize(token.lower())

# Inputs
# txt = "Mary/JJ teaches/NNS Maths/NNS"
# rules = [{'rule': '\\w+/(NN|NNP|NNS)\\sis/VBZ\\s(a|the|an)/DT\\s\\w+/(NN|NNP|NNS)', 
#           'predicates': [4], 
#           'constants': [1]}]
# all_predicates = list of possible predicates

# Output: 
# predicates = ['teaches']
# constants = ['Mary', 'Maths']
# rule_no = 2

def find_predicates_and_constants(txt, rules, all_predicates):
  rule_no = -1

  for i in range(len(rules)):
    x = re.fullmatch(rules[i]['rule'], txt)
    # print(x)
    if x is not None:
      rule_no = i
      break

  if rule_no == -1:
    return None
  
  tokens = txt.split(' ') 
  for i in range(len(tokens)):
    tokens[i] = tokens[i].split('/')[0]

  print(tokens)

  predicates = []
  constants = []

  for i in rules[rule_no]['predicates']:
    predicate = tokens[i-1]
    if predicate in all_predicates:
      predicates.append(predicate)
    else:
      predicates.append(lemmatize(predicate))

  for i in rules[rule_no]['constants']:
    constants.append(tokens[i-1])

  return predicates, constants, rule_no+1


# Output = [{'rule': '\\w+/(NN|NNP|NNS)\\sis/VBZ\\s(a|the|an)/DT\\s\\w+/(NN|NNP|NNS)', 
#           'predicates': [4], 
#           'constants': [1]}]
def get_rules(path):
    rules = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
          rule_arr = line.strip().split(' ')
          dic = {}
          dic['rule'] = rule_arr[0]
          dic['predicates'] = list(map(int,rule_arr[1].split(',')))
          if len(rule_arr)>2:
            dic['constants'] = list(map(int,rule_arr[2].split(',')))
          else:
            dic['constants'] = []
          rules.append(dic)
    return rules
 
def get_inputs(path):
    file = open(path, "r")
    doclist = [ line for line in file ]
    docstr = '' . join(doclist)
    sentences = re.split(r'[.!?]', docstr)
    new_sentences = []
    for sentence in sentences:
      if sentence != "":
        sentence = sentence.strip(' \n')
        new_sentences.append(sentence)
        
    return new_sentences

def get_all_predicates(path):
    file = open(path, "r")
    doclist = [ line.strip() for line in file ]
    return doclist

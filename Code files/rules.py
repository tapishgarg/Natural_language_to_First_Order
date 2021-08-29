from core_rules import * 

def rule_1(predicates, constants):
  return simple(predicates[0], constants[0])

def rule_2(predicates, constants):
  return simple_2(predicates[0], constants[0], constants[1])

def rule_3(predicates, constants):
  return simple_2(predicates[0], constants[0], constants[1])

def rule_4(predicates, constants):
  return And(simple(predicates[0], constants[0]), simple(predicates[0], constants[1]))

def rule_5(predicates, constants):
  return Or(simple(predicates[0], constants[0]), simple(predicates[0], constants[1]))

def rule_6(predicates, constants):
  return And(simple(predicates[0],constants[0]), simple(predicates[1],constants[1]))

def rule_7(predicates, constants):
  return forall('X',implies(simple(predicates[0],'X'), simple(predicates[1],'X')))

def rule_8(predicates, constants):
  return exists('X', simple(predicates[0],'X'))

def rule_9(predicates, constants):
  return exists('X', And(simple(predicates[0],'X'),simple(predicates[1],'X')))

def rule_10(predicates, constants):
  return Not(simple(predicates[0],constants[0]))

def rule_11(predicates, constants):
  return forall('X0', implies(simple(predicates[0],'X0'),exists('X1', implies(simple(predicates[2],"X1"),simple_2(predicates[1],'X0','X1')))))

def rule_12(predicates, constants):
  return exists('X0',And(simple(predicates[0],'X0'),forall('X1',And(simple(predicates[2],"X1"),simple_2(predicates[1],'X0','X1')))))
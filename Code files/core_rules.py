def simple(predicate, constant):
  return "{}({})".format(predicate,constant)

def simple_2(predicate, constant1, constant2):
  return "{}({},{})".format(predicate,constant1,constant2)

def And(arg1, arg2):
  return "{} and {}".format(arg1,arg2)

def Or(arg1, arg2):
  return "{} or {}".format(arg1,arg2)

def implies(arg1, arg2):
  return "{} implies {}".format(arg1,arg2)

def Not(arg):
  return "not ({})".format(arg)

def exists(x, arg):
  return "exists {} ({})".format(x,arg)

def forall(x, arg):
  return "forall {} ({})".format(x,arg)
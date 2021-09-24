def add(a,b):return float(a+b)
def sub(a,b):return float(a-b)
def mul(a,b):return float(a*b)
def div(a,b):return float(a/b)
def pow(a,b):return float(a**b)

operators = {
  '+':add,
  '-':sub,
  '*':mul,
  '/':div,
  '^':pow
}

def calculate(s):
    try:
        return float(s)
    except:
        for c in operators:
            left, operator, right = s.partition(c)
            if operator in operators:
                return operators[operator](calculate(left), calculate(right))

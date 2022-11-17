# Bonus Question

# ^ = AND
# v = OR
# → = CONDITIONAL
# ↔ = BICONDITIONAL
# ⊕ = XOR
# ¬ = NOT

express = input("Enter your expression with p, q and r:").split()
expression = []

for i in range(len(express)):
  match express[i]:
    case "^":
      expression.append("and")
    case "V":
      expression.append("or")
    case "→":
      expression.append("not " + express[i-1] + " or " + express[i+1])
    case "↔":
      expression.append("not " + express[i-1] + " or " + express[i+1] + \
                        " and " + "not " + express[i+1] + " or " + express[i-1])
    case "¬":
      expression.append("not")
    case "⊕":
      expression.append(" not " + express[i-1] + " and " + express[i+1] + " or " + \
                        " not " + express[i+1] + " and " + express[i-1])
    case _:
        expression.append(express[i])

print(expression)
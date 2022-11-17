from Exceptions.DigitException import DigitsConstraint
from Exceptions.NumericException import NumericConstraint
from Exceptions.OperatorException import OperatorConstraint


OPERATORS = ("+", "-")


def operator_constraint(string):
    if string not in OPERATORS:
        raise OperatorConstraint()


def numeric_constraint(string):
    if not string.isnumeric():
        raise NumericConstraint()
    elif len(string) > 4:
        raise DigitsConstraint()


def line1_arithmetic_format(operand, operand2):
    numeric_constraint(operand)
    if len(operand) > len(operand2):
        return f"{' ' * 2}{operand}"
    return f'{" "*(2+len(operand2)-len(operand))}{operand}'


def line2_arithmetic_format(operator, operand, operand2):
    numeric_constraint(operand)
    operator_constraint(operator)
    if len(operand2) > len(operand):
        return f"{operator}{' ' * (len(operand2) - len(operand)+1)}{operand}"
    return f'{operator} {operand}'


def line3_arithmetic_format(longest):
    return f"{'-'*(longest+2)}"


def line4_arithmetic_format(operand1, operator, operand2, longest):
    if operator == "+":
        result = str(int(operand1) + int(operand2))
    else:
        result = str(int(operand1) - int(operand2))
    if len(result) == longest: return f'  {result}'
    elif len(result) > longest: return f' {result}'
    return f'{" "*(longest-len(result))}{result}'


def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    try:
        line1_format = []
        line2_format = []
        line3_format = []
        line4_format = []
        for p in problems:
            operands = p.split()
            operand1, operator, operand2 = operands[:]
            longest = len(operand1) if len(operand1) > len(operand2) else len(operand2)
            line1_format.append(line1_arithmetic_format(operand1, operand2))
            line2_format.append(line2_arithmetic_format(operator, operand2, operand1))
            line3_format.append(line3_arithmetic_format(longest))
            if result:
                line4_format.append(line4_arithmetic_format(operand1, operator, operand2, longest))
        arranged_problems = "    ".join(line1_format) \
                            + "\n" + "    ".join(line2_format) \
                            + "\n" + "    ".join(line3_format)
        if result:
            arranged_problems += "\n" + "    ".join(line4_format)
    except NumericConstraint:
        return "Error: Numbers must only contain digits."
    except OperatorConstraint:
        return "Error: Operator must be '+' or '-'."
    except DigitsConstraint:
        return "Error: Numbers cannot be more than four digits."
    return arranged_problems


if __name__ == "__main__":
    print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))

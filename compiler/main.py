import sys

from lang.context import Context
from lang.eval_visitor import Eval
from lang.semantic_checker_visitor import SemanticChecker
from parser_1 import parser

def main():
    # Ensure that a file path argument was provided
    if len(sys.argv) < 2:
        print("Error: No file path provided.")
        sys.exit(1)

    filePath = sys.argv[1]

    with open(filePath, 'r') as file:
        data = file.read()

    ast = parser.parse(data)
    c =  Context()

    errors = ast.accept(SemanticChecker(c))
    if len(errors)==0:
        ast.accept(Eval(Context()))
    else :
        print(errors)


if __name__ == "__main__":
    main()
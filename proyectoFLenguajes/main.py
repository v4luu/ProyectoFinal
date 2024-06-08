#main.py

from antlr4 import *
from pynumsLexer import pynumsLexer
from pynumsParser import pynumsParser
from pynumsVisitor import pynumsVisitor
from MyVisitor import MyVisitor

def main():
    input_stream = FileStream('input.txt')
    lexer = pynumsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = pynumsParser(stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
    
    
    

if __name__ == '__main__':
    main()

from parser.lexer import lex
from parser.parser import parse


def from_string(string):
    tokens = lex(string)
    return parse(tokens)


string = '[{"some": "Body"}]'
from_string(string)

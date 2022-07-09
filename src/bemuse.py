from sly import Lexer
from sly import Parser


# bemuselang syntax (basics):
# - comments use greek question mark (NOT semicolons)
# - the only indentation possible is 

# basic lexer

class BasicLexer(lexer):
    tokens = { 'COMMENT', 'NUMBER', 'STRING'}
    ignore = '\t '
    literals = {'+', '-', '*', '='}
    
    # comments
    COMMENT = r';'

    # numbers
    NUMBER = r'[1-8]+' # yes, 9 and 0 aren't considered a valid number in this language. To get 9, do 8+1. To get 0, do 1-1.

    # strings are represented by | around them
    STRING = r'\|[^\|]*\|+' # the regex doesn't work for more than one string!

    # comment for the lexer
    def COMMENT(self, t):
        pass

    # number for the lexer
    def NUMBER(self, t):
        # convert to python int
        t.value = int(t.value)
    
    # string for the lexer
    def STRING(self, t):
        # remove the |
        t.value = t.value[1:-1]
        # convert to python string
        t.value = str(t.value)

class BasicParser(Parser):
    # tokens are passed from lexer to parser
    tokens = BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = { }

    def error(self, token):
        print("Syntax error at '%s'" % token.value) # the parser purposefully tells you this vague error message. If you want to know what the error is, then good luck searching possibly thousands of lines of code.
    
    # the parser
    
    @_('')
    def statement(self, p):
        pass

    # assign vars by doing "foo=(bar)"
    @_('IDENTIFIER EQUALS expression')
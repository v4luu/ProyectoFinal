grammar pynums;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE?        # assign
    |   NEWLINE                     # blank
    |   if_statement                # ifStatement
    |   for_statement               # forStatement
    |   while_statement             # whileStatement
    |   print_statement             # printStatement
    |   func_def                    # functionDefinition
    |   func_call1                  # functionCall
    |   return_stat                 # returnStatement
    |   file_op                     # fileOperation
    |   csv                         # fileCSV
    |   graficar                    # grafica
    |   modArray                    # modificarArray
    ;

modArray:   ID '.append(' expr ')'       # append
        |   ID '.remove(' expr ')'       # remove
        ;

if_statement: IF expr ':' '{' stat+ '}' NEWLINE* (elif_statement)* NEWLINE* (else_statement)? ;

csv: read1csv                                    # readCSV
    |'write_csv' '(' STR ',' expr ')' NEWLINE    # writeCSV
    ;

graficar : 'graf' '(' STR ',' expr ',' expr (',' expr)? ')' NEWLINE ;

read1csv: 'read_csv' '(' STR ')' NEWLINE;

elif_statement: ELIF expr ':' '{' stat+ '}' ;

else_statement: ELSE ':' '{' stat+ '}' ;

for_statement: FOR ID '=' range_expr ':' '{' NEWLINE stat+ '}' ;
range_expr: expr '..' expr ;
while_statement: WHILE expr ':' '{' NEWLINE stat+ '}' ;

print_statement: PRINT '(' expr ')' NEWLINE ;

func_def: DEF ID '(' params ')' ':' '{' NEWLINE stat*   '}' ;
return_stat: RETURN expr NEWLINE? ;

params: (ID (',' ID)*)? ;

file_op: read    # fileRead
       | FILE_WRITE '(' STR ',' expr ')' NEWLINE  # fileWrite
       | FILE_APPEND '(' STR ',' expr ')' NEWLINE # fileAppend
       ;

read : FILE_READ '(' STR ')' NEWLINE;
args: (expr (',' expr)*) ;

expr:   expr op=('*'|'/'|'%') expr    # MulDivMod   
    |   expr op=('+'|'-') expr        # AddSub
    |   expr '^'  '(' expr ')'        # Exponent
    |   sign=('-'|'+') expr           # unary
    |   INT                           # int
    |   FLOAT                         # float
    |   ID                            # id
    |   BOOL                          # bool
    |   '(' expr ')'                  # parens
    |   SQRT '(' expr ')'             # sqrt
    |   TRIG '(' expr ')'             # trig
    |   expr COMP expr                # comparison
    |   list_expr                     # list
    |   matrix_expr                   # matrix
    |   func_call1                    # func_call
    |   STR                           # str
    |   read                          # readd
    |   read1csv                      # readdcsv
    |   split                         # splitt
    
    ;

split : ID '.split' '('   expr ')';

func_call1: ID '(' args? ')' ;

list_expr: '[' (expr (',' expr)*)? ']' ;

matrix_expr: '[' (list_expr (',' list_expr)*)? ']' ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
ADD :   '+' ;
SUB :   '-' ;
POW :   '^' ;
BOOL :   'False' | 'True' ;
SQRT:   'sqrt' ;
TRIG:   ('sin' | 'cos' | 'tan') ;
COMP:   ('<'|'>'|'=='|'<='|'>=');
DEF:    'def' ;
RETURN: 'return' ;
IF  :   'if' ;
ELIF:   'elif' ;
ELSE:   'else' ;
FOR :   'for' ;
WHILE:  'while';
PRINT:  'print';
FILE_READ: 'read_file' ;
FILE_WRITE: 'write_file' ;
FILE_APPEND: 'append_file' ;
STR : '"' ( ~["\r\n] | '""' )* '"' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT  :   [0-9]+ ;
FLOAT :    [0-9]+ ('.' [0-9]+ )? ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)

WS  :   [ \t]+ -> skip ; // toss out whitespace

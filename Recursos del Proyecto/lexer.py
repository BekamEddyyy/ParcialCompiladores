# --BEKAM--------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 


 # List of token names.   This is always required
tokens = [
    # Inicio y Fin
    'Principality',
    'End',
    'TipoFuncion',
    'EndFuncion',
    # Atributos
    'int',
    'float',
    'double',
    'char',
    'bool',
    'string',
    # Numeros
    'Num',
    # Valores de Bool
    'bool_True',
    'bool_False',
    # Controladores / Palabras Clave
    'If',
    'Else',
    'Endif',
    'For',
    'Endfor',
    'While',
    'Endwhile',
    'cout',
    'SaltoLinea',
    'Cin',
    'Return',
    #'P_Romper',

    # Simbolos y Signos
    'parentesisIZQ',
    'parentesisDER',
    'And',
    'Or',
    'pcoma',
    'Suma',
    'Resta',
    'Mult',
    'Div',
    'Asignacion',  #'='
    'mayor_que',
    'menor_que', 
    'maIgual_que',
    'meIgual_que',
    'iguales_que',
    'diferente_que', #'!='
    'llaveIZQ',
    'llaveDER',
    'CometariosLineal',
    'CometariosMultiple',
    'comillasSimples',
    'modulo',
    'decimal',
    'SumaunoAuno',
    'opuesto_que',
    #'S_ascender',
    #'S_descender',
    
    # Textos
    'Print',
    # Variables y Funciones (ID)
    'ID',
    'IFD',
    
]


# Expresiones regulares
# Tokens prioritarios
def t_Principality(t):
  r'Principality'
  return t

def t_End(t):
  r'end'
  return t

def t_TipoFuncion(t):
  r'TipoFuncion'
  return t

def t_EndFuncion(t):
  r'EndFuncion'
  return t

def t_int(t):
  r'int'
  return t

def t_float(t):
  r'float'
  return t

def t_char(t):
  r'char'
  return t

def t_bool(t):
  r'bool'
  return t

def t_bool_True(t):
  r'true'
  return t

def t_bool_False(t):
  r'false'
  return t

def t_string(t):
  r'string'
  return t

###
def t_If(t):
  r'if'
  return t

def t_Else(t):
  r'else'
  return t

def t_Endif(t):
  r'EndIf'
  return t

def t_For(t):
  r'for'
  return t

def t_Endfor(t):
  r'Endfor'
  return t

def t_While(t):
  r'while'
  return t

def t_Endwhile(t):
  r'EndWhile'
  return t

def t_cout(t):
  r'cout'
  return t

def t_SaltoLinea(t):
  r'S'
  return t

def t_Cin(t):
  r'cin'
  return t

def t_Return(t):
  r'return'
  return t


# Textos
def t_Print(t):
    r'("[a-zA-Z0-9 ]*")'
    return t

# Variables y Funciones
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t
def t_IFD(t):
    r'_[a-zA-Z][a-zA-Z0-9]*_'
    return t

# Numeros
def t_Num(t):
  r'\d+(\.\d+)?'
  if '.' in t.value:
      t.value = float(t.value)
  else:
      t.value = int(t.value)
  return t



 # Regular expression rules for simple tokens
t_Suma    = r'\+' #
t_Resta   = r'-' #
t_Mult   = r'\*' #
t_Div  = r'/'  #
t_parentesisIZQ  = r'\(' #
t_parentesisDER  = r'\)' #
t_And = r'&&' #
t_Or = r'\|\|'  #
t_pcoma = r',' #
t_Asignacion  = r'\=' # 
t_menor_que  = r'\<' # 
t_mayor_que  = r'\>' #
t_diferente_que  = r'\!\=' #
t_opuesto_que  = r'\!' 
t_maIgual_que  = r'\>\=' #
t_meIgual_que  = r'\<\='#
t_iguales_que = r'=='
t_llaveIZQ  = r'\['
t_llaveDER  = r'\]'
t_CometariosLineal = r'//.*'
t_CometariosMultiple = r'/\*(.|\n)*?\*/'
#t_S_comillasdobles = r'\".*\"'
t_comillasSimples = r'\'.*?\''
t_modulo = r'%'
t_SumaunoAuno = r'\+\+'
#t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_decimal = r'[0-9]+\.[0-9]+'

# Regla para manejar espacios en blanco
def t_whitespace(t):
    r'\s+'
    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


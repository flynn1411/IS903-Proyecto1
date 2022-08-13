from core.lexer import Lexer
from core.parser_ import Parser
from core.interpreter import Interpreter
import sys

param = sys.argv[1:]
if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")
fileName = param[0]

f = open(fileName,"r")
text_rows = f.read()
f.close()

try:
	print("\nAnálisis Léxico")
	print("-"*30)
	lexer = Lexer(text_rows)
	tokens = lexer.generate_tokens()


	print("\nParseo")
	print("-"*30)
	parser = Parser(tokens)
	trees_list = parser.parse()
	
	print("Árbol por linea:")
	for tree in trees_list:
		print(tree)

	interpreter = Interpreter()

	print("\nInterpretación")
	print("-"*30)

	for tree in trees_list:			
		value = interpreter.visit(tree)
		print(f'{tree} = {value}')

except Exception as e:
	print(e)

from core.tokens import Token, TokenType

WHITESPACE = ' \t'
NEW_LINE = "\n"
DIGITS = '0123456789'
EOF = '$'

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.tokens:list = []
		self.advance()
		self.current_line = 0

	def insert_token(self, token:Token) -> None:
		print(f'Line: {self.current_line} | Type: {token.type} | Value: {token.value}')
		self.tokens.append(token)


	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char == NEW_LINE:
				self.advance()
				self.insert_token(Token(TokenType.NEW_LINE))
				self.current_line += 1
			elif self.current_char == "$":
				self.advance()
				self.insert_token(Token(TokenType.EOF, 8))
				return self.tokens
			elif self.current_char == '.' or self.current_char in DIGITS:
				self.insert_token(self.generate_number())
			elif self.current_char == '+':
				self.advance()
				self.insert_token(Token(TokenType.PLUS))
			elif self.current_char == '-':
				self.advance()
				self.insert_token(Token(TokenType.MINUS))
			elif self.current_char == '*':
				self.advance()
				self.insert_token(Token(TokenType.MULTIPLY))
			elif self.current_char == '/':
				self.advance()
				self.insert_token(Token(TokenType.DIVIDE))
			elif self.current_char == '(':
				self.advance()
				self.insert_token(Token(TokenType.LPAREN))
			elif self.current_char == ')':
				self.advance()
				self.insert_token(Token(TokenType.RPAREN))
			else:
				raise Exception(f"Illegal character '{self.current_char}'")
		return self.tokens

	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					raise Exception(f"Illegal character '{self.current_char}'")
			
			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'

		return Token(TokenType.NUMBER, float(number_str))

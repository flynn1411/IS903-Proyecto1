from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	NUMBER    = 0
	PLUS      = 1
	MINUS     = 2
	MULTIPLY  = 3
	DIVIDE    = 4
	LPAREN    = 5
	RPAREN    = 6
	NEW_LINE = 7
	EOF = 8

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name

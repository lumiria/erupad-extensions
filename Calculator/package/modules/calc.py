# -*- coding: utf-8 -*-
import decimal

class Calculator:

	def __init__(self, formula, reverse=False):
		self.__formula = ''.join(formula.split())
		if reverse:
			self.__formula = ''.join(self.__formula[::-1])
		self.__reverse = reverse
		self.__length = len(self.__formula)
		self.__stack = []
	
	def get_evaluated_formula(self):
		if not self.__reverse:
			return ''.join(self.__stack)
		
		stack = self.__stack[:]
		formula = ''
		while len(stack):
			formula += stack.pop()
		return formula
	
	def evaluate(self):
		val, _ = self.__expr(0)
		if not self.__reverse:
			print('Caclulator | formula:', self.__formula, ' = ', val)
		return val
	
	def __expr(self, i):
		return self.__expr_term_core(i, self.__term, ['+', '-'])
	
	def __term(self, i):
		return self.__expr_term_core(i, self.__factor, ['*', '/'])
	
	def __expr_term_core(self, i, method, operators):
		val, i = method(i)
		if val is None or i > self.__length:
			return (val, i)
			
		def get_operator():
			nonlocal i, val
			op = self.__get_at(i)
			if self.__reverse and op == '-' and self.__get_at(i+1) in ['+', '-', '*', '/']:
				self.__stack.append(op)
				i += 1
				op = self.__get_at(i)
			return op
		
		op = get_operator()
		while op in operators:
			self.__stack.append(op)
			val2, i = method(i+1)
			if val2 is None:
				if not self.__reverse or op != '-':
					self.__stack.pop()
				break
			val = self.__calc(val, val2, op)
			op = self.__get_at(i)
		
		return (val, i)
		
	def __factor(self, i):
		if i >= self.__length:
			return (None, i)
			
		chr = self.__get_at(i)
		
		if chr.isdigit() or (not self.__reverse and chr == '-'):
			return self.__number(i)
		
		if not self.__is_char(chr, '(', ')'):
			return (None, i)
		self.__stack.append(chr)
		sp = i
		
		val, i = self.__expr(i+1)
		
		chr = self.__get_at(i)
		if not self.__is_char(chr, ')', '('):
			return (None, i)
		self.__stack.append(chr)
		ep = i+1
		
		return (val, i+1)
	
	def __number(self, i):
		def isdigit(c):
			return c.isdigit() or (not isdicimals and c == '.')
		
		head = i
		isdicimals = False
		
		while i < self.__length and isdigit(self.__get_at(i)) or head == i:
			chr = self.__get_at(i)
			if chr == '.':
				isdicimals = True
			i += 1	
			self.__stack.append(chr)
		
		number = self.__get_range(head, i)
		return (decimal.Decimal(number), i)
	
	def __calc(self, val1, val2, op):
		if op == '+':
			return val1 + val2
		elif op == '-':
			return val1 - val2
		elif op == '*':
			return val1 * val2
		elif op == '/':
			return val1 / val2 if val2 != 0 else 0
		return 0
	
	def __is_char(self, chr, value, reverse_value):
		return not (self.__reverse and chr != reverse_value
			or not self.__reverse and chr != value)
	
	def __get_at(self, i):
		return self.__formula[i] if i < self.__length else None
	
	def __get_range(self, start, end):
		return self.__formula[start:end]


def get_formula(text):
	calc = Calculator(text, True)
	calc.evaluate()
	return calc.get_evaluated_formula()
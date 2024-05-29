# -*- coding: utf-8 -*-
import_as("modules.calc", "calc")

def is_trigger_key(key):
	return key == '='

def get_text(_):
	(line_text, caret_pos) = notepad.editor.get_current_line_text_with_caret_pos()
	return line_text[0:caret_pos - 1]

def get_calculation_formula(text):
	return calc.get_formula(text)

def create_calculator(formula):
	return calc.Calculator(formula)

def evaluate(calc):
	result = calc.evaluate()
	if not not result or result == 0:
		notepad.editor.show_completion_list(str(result))

registered = notepad.editor.observe_text_entered(rxlike.pipe(
	rxlike.filter(is_trigger_key),
	rxlike.map(get_text),
	rxlike.observe_on_task(),
	rxlike.map(get_calculation_formula),
	rxlike.filter(lambda formula: not not formula),
	rxlike.map(create_calculator),
))
registered.subscribe(evaluate) 
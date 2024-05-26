# -*- coding: utf-8 -*-
import sys

def get_target_type(text, file_type):
	"""
	Get the type string to format.
	
	Args:
		text (str): File contents.
		file_type (str): File extension.
	Returns:
		The type string to format.
	"""
	if file_type == "json" or file_type == "xml":
		return file_type
	elif file_type == "xaml":
		return "xml"
	
	if text.startswith("{"):
		return "json"
	elif text.startswith("<"):
		return "xml"
	return file_type


def format_data():
	"""
	Formats the contents of a text editor.
	
	Returns:
		None
	"""
	texteditor = notepad.window.texteditor
	text = texteditor.text.strip()
	if not text:
		return

	target_type = get_target_type(
		text, texteditor.file_type.lower())

	print("Data.Styler | FileType: " + target_type)
	
	formatted_text = None
	
	if target_type == "json":
		import_as("modules.json", "formatter")
		formatted_text = formatter.format(text, notepad.settings)
	elif target_type == "xml":
		import_as("modules.xml", "formatter")
		formatted_text = formatter.format(text, notepad.settings)
	
	if formatted_text != None:
		notepad.window.texteditor.text = formatted_text

print ('')
format_data()
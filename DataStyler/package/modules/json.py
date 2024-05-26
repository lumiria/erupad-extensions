# -*- coding: utf-8 -*-
import sys
import json
import collections
from json import encoder

def format(text, settings):
	"""
	Formats the specified text in Json format.
	
	Args:
		text (str): Text to format.
		settings (object): Interface where settings are sotred.
	Returns:
		Formatted text. If it fails, None.
	"""

	try:
		indent = settings.data_styler.indent or 2
		float_ndigits = settings.data_styler.float_ndigits
		
		if float_ndigits:
			encoder.FLOAT_REPR = lambda o: f'{o:.{int(float_ndigits)}f}'
		decoder = json.JSONDecoder(
			object_pairs_hook=collections.OrderedDict)
		data = decoder.decode(text)
		
		return json.dumps(data, indent=int(indent), ensure_ascii=False)
	except Exception as e:
		print('Data.Styler | [error] JSON parsing failed.')
		print(sys.exc_info())
		return None
	else:
		return None
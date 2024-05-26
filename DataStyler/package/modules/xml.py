# -*- coding: utf-8 -*-
import sys
import xml.dom.minidom

def format(text, settings):

	try:
		xml = xml.dom.minidom.parseString(text)
		return xml.toprettyxml()
	except Exception as e:
		print('Data.Styler | [error] JSON parsing failed.')
		print(sys.exc_info())
		return False
	else:
		return True
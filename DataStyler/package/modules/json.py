# -*- coding: utf-8 -*-
import sys
import json
import collections
import re
from json import encoder

JSONDecodeError = getattr(json, "JSONDecodeError", ValueError)


def __decode(text, settings):
    decoder = json.JSONDecoder(
        object_pairs_hook=collections.OrderedDict)

    try:
        obj, _ = decoder.raw_decode(text)
        return obj
    except JSONDecodeError:
        pass

    if settings.data_styler.allow_escaped_json_string:
        try:
            text, _ = decoder.raw_decode(f'"{text}"')
        except JSONDecodeError:
            pass

    if settings.data_styler.accept_decimal_string:
        text = re.sub(r"Decimal\('(\d+)'\)", r'\1', text)

    if settings.data_styler.allow_single_quotes:
        text = text.replace('\'', '"')

    return decoder.raw_decode(text)[0]


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

        data = __decode(text, settings)

        return json.dumps(data, indent=int(indent), ensure_ascii=False)
    except Exception:
        print('Data.Styler | [error] JSON parsing failed.')
        print(sys.exc_info())
        return None
    else:
        return None

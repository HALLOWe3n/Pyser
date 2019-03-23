from .constants import *


def parse_array(tokens):
    json_array = []
    
    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        return json_array, tokens[1:]
    
    while True:
        json, tokens = parse(tokens)
        json_array.append(json)
        
        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise Exception('Expected end-of-array bracket')


def parse_object(tokens):
    json_object = {}

    t = tokens[0]
    if t == JSON_RIGHTBRACE:
        return json_object, tokens[1:]
    
    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expected string key, got: {}'.format(json_key))
        if tokens[0] != JSON_COLON:
            raise Exception('Expected colon after key in object, got: {}'.format(t))
        
        json_value, tokens = parse(tokens[1:])
        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after pair in object, got: {}'.format(t))

        t = tokens[1:]
        raise Exception('Expected end-of-object brace')


def parse(tokens):
    t = tokens[0]

    if t == JSON_LEFTBRACKET:
        parse_array(tokens[1:])
    elif t == JSON_LEFTBRACE:
        parse_object(tokens[1:])
    else:
        return t, tokens[1:]
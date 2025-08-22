

class JsonParser:
    def __init__(self):
        self.tokens = []

        self.JSON_QUOTE = '"'
        self.JSON_WHITESPACE = [' ', '\t', '\n', '\r', '\b']
        self.JSON_SYNTAX = ['{', '}', '[', ']', ':', ',']

        self.TRUE_LEN = len('true')
        self.FALSE_LEN = len('false')
        self.NULL_LEN = len('null')

    def lex_string(self, string):
        json_string = ''

        if string[0] == self.JSON_QUOTE:
            string = string[1:]
        else:
            return None, string

        for c in string:
            if c == self.JSON_QUOTE:
                return json_string, string[len(json_string)+1:]
            else:
                json_string += c

        raise Exception('Expected end-of-string quote')

    # TODO : Create parse_array and parse_object

    def lex_number(self, string):
        json_number = ''

        number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']

        for c in string:
            if c in number_characters:
                json_number += c
            else:
                break

        rest = string[len(json_number):]

        if not len(json_number):
            return None, string

        if '.' in json_number:
            return float(json_number), rest

        return int(json_number), rest

    def lex_bool(self, string):
        string_len = len(string)

        if string_len >= self.TRUE_LEN and string[:self.TRUE_LEN] == 'true':
            return True, string[self.TRUE_LEN:]
        elif string_len >= self.FALSE_LEN and string[:self.FALSE_LEN] == 'false':
            return False, string[self.FALSE_LEN:]
        return None, string

    def lex_null(self, string):
        string_len = len(string)

        if string_len >= self.NULL_LEN and string[:self.NULL_LEN] == 'null':
            return True, string[self.NULL_LEN:]

        return None, string

    def lex(self, string):
        while len(string):
            json_string, string = self.lex_string(string)
            if json_string is not None:
                self.tokens.append(json_string)
                continue

            json_number, string = self.lex_number(string)
            if json_number is not None:
                self.tokens.append(json_number)
                continue

            json_bool, string = self.lex_bool(string)
            if json_bool is not None:
                self.tokens.append(json_bool)
                continue

            json_null, string = self.lex_null(string)
            if json_null is not None:
                self.tokens.append(json_null)
                continue

            if string[0] in self.JSON_WHITESPACE:
                string = string[1:]
            elif string[0] in self.JSON_SYNTAX:
                self.tokens.append(string[0])
                string = string[1:]
            else:
                raise Exception(f"Unexpected character : {string[0]}")

        return self.tokens

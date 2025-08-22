import unittest
from main import JsonParser


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.parser = JsonParser()

    def test_lex_string(self):
        value, rest = self.parser.lex_string('"hello" world')
        self.assertEqual(value, 'hello')
        self.assertEqual(rest, ' world')

    def test_lex_number_int(self):
        value, rest = self.parser.lex_number('1234,')
        self.assertEqual(value, 1234)
        self.assertEqual(rest, ',')

    def test_lex_number_float(self):
        value, rest = self.parser.lex_number('12.34 rest')
        self.assertEqual(value, 12.34)
        self.assertEqual(rest, ' rest')

    def test_lex_bool_true(self):
        value, rest = self.parser.lex_bool('true,')
        self.assertTrue(value)
        self.assertEqual(rest, ',')

    def test_lex_bool_false(self):
        value, rest = self.parser.lex_bool('false}')
        self.assertFalse(value)
        self.assertEqual(rest, '}')

    def test_lex_null(self):
        value, rest = self.parser.lex_null('null,')
        self.assertTrue(value)
        self.assertEqual(rest, ',')

    def test_lex(self):
        tokens = self.parser.lex('{"a": 1, "b": false, "c": null}')
        self.assertIn('{', tokens)
        self.assertIn('a', tokens)
        self.assertIn(':', tokens)
        self.assertIn(1, tokens)
        self.assertIn('b', tokens)
        self.assertIn(False, tokens)
        self.assertIn('c', tokens)
        self.assertIn(True, tokens)  # null returns True in lex_null
        self.assertIn('}', tokens)


if __name__ == '__main__':
    unittest.main()

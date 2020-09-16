import Lab4_camelCase
from unittest import TestCase
class CamelCaseTest(TestCase):
    
    def test_camelcase_sentence(self):
        self.assertEqual('filaFila', Lab4_camelCase.camel_case('Fila Fila'))
    
    def test_checkingemptystring(self):
        self.assertEqual('please enter your input',Lab4_camelCase.camel_case(''))
    
    def test_checkingonlywords(self):
        self.assertEqual("enter only words",Lab4_camelCase.camel_case('1123376978698'))
 #   def test_always_out_put_incamelcase(self):
        #self.assertEqual('helloHelloWorld',Lab4_camelCase.camelcase_class('heLLo hELlo WpytoRld'))
    
    def test_justone_word(self):
        self.assertEqual('hello',Lab4_camelCase.camel_case('hello'))
    def test_doubleormorespaceses_betweenwords(self):
        self.assertEqual('helloHelloHelloWorld', Lab4_camelCase.camel_case('hello   hello    hello world'))
    def test_spacecing_before_and_after(self):
        self.assertEqual('helloHelloWorld',Lab4_camelCase.camel_case(' hello hello world '))

    def test_camel_case_emojis(self):
        input_and_expected_outputs = {
            '😊🥺😉😍😘': '😊🥺😉😍😘',
            '💁👌🎍😍': '💁👌🎍😍',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, Lab4_camelCase.camel_case(input_val))




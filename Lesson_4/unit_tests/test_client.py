import unittest
import client
import common.variables as var

class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.user_name = 'Sergey'
        self.correct_msg = {
            var.ACTION: var.PRESENCE,
            var.TIME: 111.111,
            var.USER: {
                var.ACCOUNT_NAME: self.user_name
            }
        }
        self.correct_response = {
            var.RESPONSE: 200
        }
        self.incorrect_response = {
            var.RESPONSE: 400,
            var.ERROR: "Bad Request"
        }
        self.incorrect_request_msg = {
            'random_field': 'random_value'
        }

    def test_create_presence(self):
        test = client.create_presence(self.user_name)
        test[var.TIME] = 111.111
        self.assertEqual(test, self.correct_msg)

    def test_process_ans_200(self):
        test = client.process_ans(self.correct_response)
        self.assertEqual(test, '200 : OK')

    def test_process_ans_400(self):
        test = client.process_ans(self.incorrect_response)
        self.assertEqual(test, '400 : Bad Request')

    def test_process_ans_bad(self):
        self.assertRaises(ValueError, client.process_ans, self.incorrect_request_msg)


if __name__ == '__main__':
    unittest.main()

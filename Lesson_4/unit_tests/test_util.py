import json
import unittest
import common.utils as utils
import common.variables as var


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, msg):
        self.encoded_message = json.dumps(self.test_dict).encode(var.ENCODING)
        self.received_message = msg

    def recv(self, max_len):
        return json.dumps(self.test_dict).encode(var.ENCODING)


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.test_request = {
            var.ACTION: var.PRESENCE,
            var.TIME: 111111.111111,
            var.USER: {
                var.ACCOUNT_NAME: 'test_user'
            }
        }

        self.response_ok = {var.RESPONSE: 200}

        self.reponse_400 = {
            var.RESPONSE: 400,
            var.ERROR: 'Bad Request'
        }

    def test_get_message(self):
        test_ok = TestSocket(self.response_ok)
        test_err = TestSocket(self.reponse_400)
        self.assertEqual(utils.get_message(test_ok), self.response_ok)
        self.assertEqual(utils.get_message(test_err), self.reponse_400)

    def test_send_message(self):
        test = TestSocket(self.test_request)
        utils.send_message(test, self.test_request)
        self.assertEqual(test.encoded_message, test.received_message)


if __name__ == '__main__':
    unittest.main()

import unittest
import server
import common.variables as var


class TestServer(unittest.TestCase):

    def setUp(self) -> None:
        self.user_name = 'Guest'
        self.correct_msg = {
            var.ACTION: var.PRESENCE,
            var.TIME: 111.111,
            var.USER: {
                var.ACCOUNT_NAME: self.user_name
            }
        }
        self.msg_without_action = {
            var.TIME: 111.111,
            var.USER: {
                var.ACCOUNT_NAME: self.user_name
            }
        }
        self.msg_without_time = {
            var.ACTION: var.PRESENCE,
            var.USER: {
                var.ACCOUNT_NAME: self.user_name
            }
        }
        self.msg_without_user = {
            var.ACTION: var.PRESENCE,
            var.TIME: 111.111,
        }

    def test_process_client_message_ok(self):
        test = server.process_client_message(self.correct_msg)
        self.assertEqual(test, {var.RESPONSE: 200})

    def test_process_client_message_no_action(self):
        test = server.process_client_message(self.msg_without_action)
        self.assertEqual(test, {var.RESPONDEFAULT_IP_ADDRESSSE: 400, var.ERROR: 'Bad Request'})

    def test_process_client_message_no_time(self):
        test = server.process_client_message(self.msg_without_time)
        self.assertEqual(test, {var.RESPONDEFAULT_IP_ADDRESSSE: 400, var.ERROR: 'Bad Request'})

    def test_process_client_message_no_user(self):
        test = server.process_client_message(self.msg_without_user)
        self.assertEqual(test, {var.RESPONDEFAULT_IP_ADDRESSSE: 400, var.ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()

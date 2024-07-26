import unittest
from app.models.chat import Chat
from app.models.player import Player

class TestChat(unittest.TestCase):
    def test_send_message(self):
        chat = Chat()
        player = Player(1, "Wellington", "well@example.com", "wwagner", "password123")
        chat.send_message(player, "Hello, world!")
        self.assertEqual(len(chat.messages), 1)
        self.assertEqual(chat.messages[0], "wwagner: Hello, world!")
        chat.send_message(player, "Another message")
        self.assertEqual(len(chat.messages), 2)
        self.assertEqual(chat.messages[1], "wwagner: Another message")

if __name__ == "__main__":
    unittest.main()

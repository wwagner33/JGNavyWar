import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def test_create_player(self):
        player = Player(1, "Wellington", "well@example.com", "wwagner", "password123")
        self.assertEqual(player.name, "Wellington")
        self.assertEqual(player.email, "well@example.com")
        self.assertEqual(player.username, "wwagner")
        self.assertEqual(player.password, "password123")
        self.assertEqual(player.score, 0)

    def test_update_score(self):
        player = Player(1, "Wellington", "well@example.com", "wwagner", "password123")
        player.update_score(100)
        self.assertEqual(player.score, 100)

if __name__ == "__main__":
    unittest.main()

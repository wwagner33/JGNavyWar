import unittest
from datetime import datetime
from app.models.move import Move
from app.models.player import Player

class TestMove(unittest.TestCase):
    def test_create_move(self):
        player = Player(1, "Wellington", "well@example.com", "wwagner", "password123")
        move = Move(player, (0, 0), 'hit')
        self.assertEqual(move.player, player)
        self.assertEqual(move.target, (0, 0))
        self.assertEqual(move.result, 'hit')
        self.assertIsNotNone(move.timestamp)

if __name__ == "__main__":
    unittest.main()

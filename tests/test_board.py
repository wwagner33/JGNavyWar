import unittest
from app.models.board import Board
from app.models.ship import Ship

class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = Board()
        self.assertEqual(board.size, 20)
        self.assertEqual(len(board.grid), 20)
        self.assertEqual(len(board.grid[0]), 20)
        self.assertEqual(board.ships, [])

    def test_place_ship(self):
        board = Board()
        ship = Ship("Porta-aviões", 8)
        success = board.place_ship(ship, (0, 0), "horizontal")
        self.assertTrue(success)
        self.assertEqual(board.grid[0][:8], ['S'] * 8)

    def test_receive_attack(self):
        board = Board()
        ship = Ship("Porta-aviões", 8)
        board.place_ship(ship, (0, 0), "horizontal")
        result = board.receive_attack((0, 0))
        self.assertEqual(result, 'hit')
        self.assertEqual(board.grid[0][0], 'X')
        result = board.receive_attack((1, 1))
        self.assertEqual(result, 'miss')

if __name__ == "__main__":
    unittest.main()

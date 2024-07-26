import unittest
from app.models.ship import Ship

class TestShip(unittest.TestCase):
    def test_create_ship(self):
        ship = Ship("Porta-aviões", 8)
        self.assertEqual(ship.name, "Porta-aviões")
        self.assertEqual(ship.size, 8)
        self.assertEqual(ship.positions, [])
        self.assertFalse(ship.is_sunk)

    def test_place_ship(self):
        ship = Ship("Porta-aviões", 8)
        ship.place((0, 0), "horizontal")
        self.assertEqual(ship.positions, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
        ship.place((0, 0), "vertical")
        self.assertEqual(ship.positions, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])

    def test_check_if_sunk(self):
        ship = Ship("Porta-aviões", 8)
        ship.place((0, 0), "horizontal")
        hits = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        ship.check_if_sunk(hits)
        self.assertTrue(ship.is_sunk)
        hits = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        ship.check_if_sunk(hits)
        self.assertFalse(ship.is_sunk)

if __name__ == "__main__":
    unittest.main()

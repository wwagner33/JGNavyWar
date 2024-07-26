import unittest
from app.models.player import Player
from app.models.ship import Ship
from app.models.board import Board
from app.models.game import Game
from app.models.chat import Chat
from app.models.move import Move

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

    def test_check_if_sunk(self):
        ship = Ship("Porta-aviões", 8)
        ship.place((0, 0), "horizontal")
        ship.check_if_sunk([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
        self.assertTrue(ship.is_sunk)

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
        self.assertEqual(board.grid[0][:8], ["S"] * 8)

    def test_receive_attack(self):
        board = Board()
        ship = Ship("Porta-aviões", 8)
        board.place_ship(ship, (0, 0), "horizontal")
        result = board.receive_attack((0, 0))
        self.assertEqual(result, "hit")
        self.assertEqual(board.grid[0][0], "X")
        result = board.receive_attack((1, 1))
        self.assertEqual(result, "miss")

class TestGame(unittest.TestCase):
    def test_start_game(self):
        players = [
            Player(1, "Wellington", "well@example.com", "wwagner", "password123"),
            Player(2, "Patricia", "pat@example.com", "ppaula", "password123")
        ]
        game = Game(players)
        game.start()
        self.assertEqual(len(game.players), 2)
        for player in game.players:
            board = game.boards[player]
            self.assertEqual(len(board.ships), 7)  # Total de 7 navios
            for ship in board.ships:
                self.assertTrue(ship.positions)  # Verifica se os navios têm posições

    def test_make_move(self):
        players = [
            Player(1, "Wellington", "well@example.com", "wwagner", "password123"),
            Player(2, "Patricia", "pat@example.com", "ppaula", "password123")
        ]
        game = Game(players)
        game.start()
        ship = Ship("Porta-aviões", 8)
        game.boards[players[1]].place_ship(ship, (0, 0), "horizontal")
        result = game.make_move(players[0], (0, 0))
        self.assertEqual(result, "hit")
        result = game.make_move(players[0], (1, 1))
        self.assertEqual(result, "miss")

    def test_check_winner(self):
        players = [
            Player(1, "Wellington", "well@example.com", "wwagner", "password123"),
            Player(2, "Patricia", "pat@example.com", "ppaula", "password123")
        ]
        game = Game(players)
        game.start()
        ship = Ship("Porta-aviões", 8)
        game.boards[players[1]].place_ship(ship, (0, 0), "horizontal")
        for i in range(8):
            game.make_move(players[0], (0, i))
        self.assertTrue(game.check_winner())

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

class TestMove(unittest.TestCase):
    def test_create_move(self):
        player = Player(1, "Wellington", "well@example.com", "wwagner", "password123")
        move = Move(player, (0, 0), "hit")
        self.assertEqual(move.player, player)
        self.assertEqual(move.target, (0, 0))
        self.assertEqual(move.result, "hit")
        self.assertIsNotNone(move.timestamp)

if __name__ == "__main__":
    unittest.main()


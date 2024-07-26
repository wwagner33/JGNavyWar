import psycopg2
import unittest

class TestDatabaseCreation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = psycopg2.connect(
            dbname="jgnavywar",
            user="postgres",
            password="Asdsee;*30",
            host="localhost"
        )
        cls.cursor = cls.conn.cursor()
        cls.create_tables()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def create_tables(cls):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                score INT DEFAULT 0
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS games (
                id SERIAL PRIMARY KEY,
                status VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS ships (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                size INT NOT NULL,
                game_id INT REFERENCES games(id) ON DELETE CASCADE,
                player_id INT REFERENCES players(id) ON DELETE CASCADE,
                positions TEXT NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS moves (
                id SERIAL PRIMARY KEY,
                game_id INT REFERENCES games(id) ON DELETE CASCADE,
                player_id INT REFERENCES players(id) ON DELETE CASCADE,
                target VARCHAR(5) NOT NULL,
                result VARCHAR(10) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS chats (
                id SERIAL PRIMARY KEY,
                game_id INT REFERENCES games(id) ON DELETE CASCADE,
                player_id INT REFERENCES players(id) ON DELETE CASCADE,
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        ]

        for query in queries:
            cls.cursor.execute(query)
        cls.conn.commit()

    def setUp(self):
        # Limpeza do banco de dados antes de cada teste
        self.cursor.execute("DELETE FROM moves")
        self.cursor.execute("DELETE FROM ships")
        self.cursor.execute("DELETE FROM chats")
        self.cursor.execute("DELETE FROM games")
        self.cursor.execute("DELETE FROM players")
        self.conn.commit()

    def test_create_player(self):
        query = """
        INSERT INTO players (name, email, username, password)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        values = ("Wellington", "well@example.com", "wwagner", "password123")
        self.cursor.execute(query, values)
        player_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.assertIsNotNone(player_id)

    def test_create_game(self):
        query = """
        INSERT INTO games (status)
        VALUES (%s) RETURNING id;
        """
        values = ("ongoing",)
        self.cursor.execute(query, values)
        game_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.assertIsNotNone(game_id)

    def test_create_ship(self):
        # First, create a player and a game
        self.cursor.execute(
            "INSERT INTO players (name, email, username, password) VALUES (%s, %s, %s, %s) RETURNING id",
            ("Patricia", "pat@example.com", "ppaula", "password123")
        )
        player_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO games (status) VALUES (%s) RETURNING id",
            ("ongoing",)
        )
        game_id = self.cursor.fetchone()[0]
        self.conn.commit()

        # Now, create the ship
        query = """
        INSERT INTO ships (name, size, game_id, player_id, positions)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        values = ("Porta-aviões", 8, game_id, player_id, "[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]")
        self.cursor.execute(query, values)
        ship_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.assertIsNotNone(ship_id)

    def test_create_move(self):
        # First, create a player and a game
        self.cursor.execute(
            "INSERT INTO players (name, email, username, password) VALUES (%s, %s, %s, %s) RETURNING id",
            ("Patricia", "pat@example.com", "ppaula", "password123")
        )
        player_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO games (status) VALUES (%s) RETURNING id",
            ("ongoing",)
        )
        game_id = self.cursor.fetchone()[0]
        self.conn.commit()

        # Now, create the move
        query = """
        INSERT INTO moves (game_id, player_id, target, result)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        values = (game_id, player_id, "A1", "hit")
        self.cursor.execute(query, values)
        move_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.assertIsNotNone(move_id)

    def test_create_chat_message(self):
        # First, create a player and a game
        self.cursor.execute(
            "INSERT INTO players (name, email, username, password) VALUES (%s, %s, %s, %s) RETURNING id",
            ("Patricia", "pat@example.com", "ppaula", "password123")
        )
        player_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO games (status) VALUES (%s) RETURNING id",
            ("ongoing",)
        )
        game_id = self.cursor.fetchone()[0]
        self.conn.commit()

        # Now, create the chat message
        query = """
        INSERT INTO chats (game_id, player_id, message)
        VALUES (%s, %s, %s) RETURNING id;
        """
        values = (game_id, player_id, "Hello, world!")
        self.cursor.execute(query, values)
        chat_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.assertIsNotNone(chat_id)

if __name__ == "__main__":
    unittest.main()

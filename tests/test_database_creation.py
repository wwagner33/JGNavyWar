import psycopg2
import unittest

class TestDatabaseCreation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = psycopg2.connect(
            dbname="jgnavywar",
            user="yourusername",
            password="yourpassword",
            host="localhost"
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    def test_create_tables(self):
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
            self.cursor.execute(query)
        self.conn.commit()

        # Verifica se as tabelas foram criadas
        self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = public")
        tables = self.cursor.fetchall()
        expected_tables = ["players", "games", "ships", "moves", "chats"]
        created_tables = [table[0] for table in tables]

        for table in expected_tables:
            self.assertIn(table, created_tables)

if __name__ == "__main__":
    unittest.main()


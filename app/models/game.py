from datetime import datetime
import random
from .board import Board
from .player import Player
from .ship import Ship
from .chat import Chat
from .move import Move

class Game:
    """
    Classe que representa uma partida do jogo JGNavyWar.

    Atributos:
    - players: Lista de jogadores na partida.
    - boards: Dicionário mapeando jogadores para seus tabuleiros.
    - chat: Instância da classe Chat para comunicação entre jogadores.
    - start_time: Hora de início da partida.
    - moves: Lista de movimentos realizados na partida.
    """
    def __init__(self, players: list):
        self.players = players
        self.boards = {player: Board() for player in players}
        self.chat = Chat()
        self.start_time = datetime.now()
        self.moves = []

    def start(self):
        """
        Inicia a partida.
        """
        for player in self.players:
            self.setup_board(player)

    def setup_board(self, player: Player):
        """
        Configura o tabuleiro para o jogador com posicionamento aleatório dos navios.

        :param player: Jogador para quem o tabuleiro será configurado.
        """
        ship_types = [
            ("Porta-aviões", 8),
            ("Couraçado", 7),
            ("Cruzador", 6),
            ("Destróier", 5),
            ("Fragata", 4),
            ("Submarino", 4),
            ("Lancha", 2),
        ]
        board = self.boards[player]
        for ship_type in ship_types:
            placed = False
            while not placed:
                start = (random.randint(0, board.size - 1), random.randint(0, board.size - 1))
                direction = random.choice(["horizontal", "vertical"])
                ship = Ship(ship_type[0], ship_type[1])
                placed = board.place_ship(ship, start, direction)

    def make_move(self, player: Player, target: tuple) -> str:
        """
        Realiza um movimento no jogo.

        :param player: Jogador que está fazendo o movimento.
        :param target: Posição alvo do movimento (linha, coluna).
        :return: Resultado do movimento ("hit" ou "miss").
        """
        opponent = self.get_opponent(player)
        result = self.boards[opponent].receive_attack(target)
        self.moves.append(Move(player, target, result))
        if result == "hit" and self.check_winner():
            return "win"
        return result

    def get_opponent(self, player: Player) -> Player:
        """
        Obtém o oponente de um jogador.

        :param player: Jogador cujo oponente deve ser obtido.
        :return: Oponente do jogador.
        """
        for p in self.players:
            if p != player:
                return p
        return None

    def check_winner(self) -> bool:
        """
        Verifica se há um vencedor na partida.

        :return: Verdadeiro se há um vencedor, falso caso contrário.
        """
        for player in self.players:
            opponent = self.get_opponent(player)
            if self.boards[opponent].all_ships_sunk():
                return True
        return False

from datetime import datetime

class Move:
    """
    Classe que representa um movimento no jogo JGNavyWar.

    Atributos:
    - player: Jogador que fez o movimento.
    - target: Posição alvo do movimento (linha, coluna).
    - result: Resultado do movimento ("hit" ou "miss").
    - timestamp: Momento em que o movimento foi realizado.
    """
    def __init__(self, player: Player, target: tuple, result: str):
        self.player = player
        self.target = target
        self.result = result
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Move(player={self.player.username}, target={self.target}, result={self.result}, timestamp={self.timestamp})"

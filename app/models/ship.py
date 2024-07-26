class Ship:
    """
    Classe que representa um navio no jogo JGNavyWar.

    Atributos:
    - name: Nome do navio.
    - size: Tamanho do navio (número de células ocupadas).
    - positions: Posições ocupadas pelo navio no tabuleiro.
    - is_sunk: Indica se o navio foi afundado.
    """
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.positions = []  # Lista de tuplas (linha, coluna)
        self.is_sunk = False

    def place(self, start: tuple, direction: str):
        """
        Posiciona o navio no tabuleiro.

        :param start: Posição inicial do navio (linha, coluna).
        :param direction: Direção do navio (horizontal ou vertical).
        """
        if direction == "horizontal":
            self.positions = [(start[0], start[1] + i) for i in range(self.size)]
        elif direction == "vertical":
            self.positions = [(start[0] + i, start[1]) for i in range(self.size)]

    def check_if_sunk(self, hits: list):
        """
        Verifica se o navio foi afundado.

        :param hits: Lista de posições atingidas.
        """
        self.is_sunk = all(pos in hits for pos in self.positions)

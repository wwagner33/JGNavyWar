class Board:
    """
    Classe que representa o tabuleiro de um jogador no jogo JGNavyWar.

    Atributos:
    - size: Tamanho do tabuleiro (número de linhas e colunas).
    - grid: Grid representando o tabuleiro.
    - ships: Lista de navios no tabuleiro.
    """
    def __init__(self, size: int = 20):
        self.size = size
        self.grid = [["~" for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship: Ship, start: tuple, direction: str) -> bool:
        """
        Posiciona um navio no tabuleiro.

        :param ship: Instância da classe Ship a ser posicionada.
        :param start: Posição inicial do navio (linha, coluna).
        :param direction: Direção do navio ("horizontal" ou "vertical").
        :return: Verdadeiro se o navio foi posicionado com sucesso, falso caso contrário.
        """
        # Verifica se o navio cabe no tabuleiro na direção escolhida
        if direction == "horizontal" and start[1] + ship.size > self.size:
            return False
        if direction == "vertical" and start[0] + ship.size > self.size:
            return False

        # Verifica se as células estão disponíveis
        if direction == "horizontal":
            for i in range(ship.size):
                if self.grid[start[0]][start[1] + i] != "~":
                    return False
        elif direction == "vertical":
            for i in range(ship.size):
                if self.grid[start[0] + i][start[1]] != "~":
                    return False

        # Posiciona o navio
        ship.place(start, direction)
        for pos in ship.positions:
            self.grid[pos[0]][pos[1]] = "S"
        self.ships.append(ship)
        return True

    def receive_attack(self, position: tuple) -> str:
        """
        Processa um ataque no tabuleiro.

        :param position: Posição do ataque (linha, coluna).
        :return: Resultado do ataque ("hit" ou "miss").
        """
        if self.grid[position[0]][position[1]] == "S":
            self.grid[position[0]][position[1]] = "X"
            for ship in self.ships:
                ship.check_if_sunk(
                    [(row, col) for row in range(self.size) for col in range(self.size) if self.grid[row][col] == "X"]
                )
            return "hit"
        return "miss"

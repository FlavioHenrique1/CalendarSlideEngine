import csv
import random


class LeitorVersiculos:
    """
    Lê um arquivo CSV no formato:

    versiculo,localizacao
    "Cada um dê conforme determinou em seu coração...",2 Coríntios 9:7
    """

    def __init__(self, caminho_csv):
        self.caminho_csv = caminho_csv

    def carregar_todos(self):
        """
        Retorna TODOS os versículos do CSV.
        """
        versiculos = []

        with open(self.caminho_csv, newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                versiculos.append({
                    "versiculo": linha["versiculo"].strip(),
                    "localizacao": linha["localizacao"].strip()
                })

        return versiculos

    def carregar_curtos(self, limite=116):
        """
        Retorna apenas os versículos que têm menos que 'limite' caracteres.
        Ideal para garantir que o texto caiba no rodapé da agenda.
        """
        todos = self.carregar_todos()
        # Filtra a lista mantendo apenas os textos menores que o limite
        curtos = [v for v in todos if len(v["versiculo"]) < limite]
        return curtos

    def sortear_curtos(self, quantidade, limite=116):
        """
        Filtra os versículos curtos e sorteia uma quantidade específica.
        """
        curtos = self.carregar_curtos(limite)

        if quantidade > len(curtos):
            print(f"Aviso: Solicitado {quantidade}, mas apenas {len(curtos)} versículos atendem ao critério de tamanho.")
            return random.sample(curtos, len(curtos))

        return random.sample(curtos, quantidade)

    def sortear(self, quantidade):
        """
        Retorna apenas 'quantidade' versículos aleatórios (sem filtro de tamanho).
        """
        todos = self.carregar_todos()

        if quantidade > len(todos):
            raise ValueError(
                f"Quantidade solicitada ({quantidade}) maior que o total ({len(todos)})"
            )

        return random.sample(todos, quantidade)
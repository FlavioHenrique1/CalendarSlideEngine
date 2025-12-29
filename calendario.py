# calendario.py
from datetime import date, timedelta


class Calendario:
    MESES = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março",
        4: "Abril", 5: "Maio", 6: "Junho",
        7: "Julho", 8: "Agosto", 9: "Setembro",
        10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    DIAS_SEMANA = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }

    def __init__(self, ano: int, mes: int):
        self.ano = ano
        self.mes = mes

    def gerar_calendario(self):
        datas = []

        data_atual = date(self.ano, self.mes, 1)

        if self.mes == 12:
            proximo_mes = date(self.ano + 1, 1, 1)
        else:
            proximo_mes = date(self.ano, self.mes + 1, 1)

        while data_atual < proximo_mes:
            dia = data_atual.day

            datas.append({
                "dia": f"{dia:02d}",
                "mes": self.MESES[data_atual.month],
                "dia_semana": self.DIAS_SEMANA[data_atual.weekday()],
                "par_ou_impar": "Par" if dia % 2 == 0 else "Ímpar",
                "ano": data_atual.year,
                "data_completa": data_atual.strftime("%d/%m/%Y")
            })

            data_atual += timedelta(days=1)

        return datas

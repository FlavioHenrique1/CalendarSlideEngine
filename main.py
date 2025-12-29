# main.py
from calendario import Calendario
from gerador_ppt import GeradorPPT
from LeitorVersiculos import LeitorVersiculos


def main():
    ano=2026
    mes=2
    calendario = Calendario(ano, mes).gerar_calendario()
    leitor = LeitorVersiculos("jsonformatter.txt")

    versiculos = leitor.carregar_curtos(104)
    ppt = GeradorPPT(
        modelo_ppt="modelo.pptx",
        saida_ppt= f"calendario_{mes}_{ano}.pptx"
    )

    ppt.gerar_slides(calendario,versiculos,indice_slide_base=0)

    print("Apresentação criada com sucesso!")


if __name__ == "__main__":
    main()

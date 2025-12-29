from pptx import Presentation
from copy import deepcopy


class GeradorPPT:
    def __init__(self, modelo_ppt, saida_ppt):
        self.prs = Presentation(modelo_ppt)
        self.saida_ppt = saida_ppt

    def _duplicar_slide_fiel(self, slide_modelo):
        """
        Duplica o slide mantendo:
        - layout
        - imagens
        - fundo
        - fontes
        - tamanhos
        """
        # cria slide em branco (evita placeholders padrão)
        layout = slide_modelo.slide_layout
        slide_novo = self.prs.slides.add_slide(layout)

        # copia TODOS os shapes do slide modelo (imagens, textos, fundos, etc)
        for shape in slide_modelo.shapes:
            slide_novo.shapes._spTree.insert_element_before(
                deepcopy(shape.element),
                'p:extLst'
            )

        return slide_novo

    def _substituir_textos_sem_perder_formatacao(self, slide, dados, versiculo):
        substituicoes = {
            "{{DIA}}": dados["dia"],
            "{{MES}}": dados["mes"],
            "{{DIA_SEMANA}}": dados["dia_semana"],
            "{{ANO}}": str(dados["ano"]),
            "{{versiculo}}": versiculo["versiculo"],
            "{{localizacao}}": versiculo["localizacao"]
        }

        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue

            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    for chave, valor in substituicoes.items():
                        if chave in run.text:
                            run.text = run.text.replace(chave, valor)

    def gerar_slides(self, calendario, versiculos, indice_slide_base=0):
        slide_modelo = self.prs.slides[indice_slide_base]

        # Garante que não falte versículo
        total = min(len(calendario), len(versiculos))

        for i in range(total):
            dados = calendario[i]
            versiculo = versiculos[i]

            novo_slide = self._duplicar_slide_fiel(slide_modelo)
            self._substituir_textos_sem_perder_formatacao(
                novo_slide,
                dados,
                versiculo
            )

        # remove apenas o slide modelo
        self.prs.slides._sldIdLst.remove(
            self.prs.slides._sldIdLst[indice_slide_base]
        )

        self.prs.save(self.saida_ppt)

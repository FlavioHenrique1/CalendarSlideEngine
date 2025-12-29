# 📅 Projeto Calendário em PowerPoint (PPT)

Este projeto gera automaticamente uma **agenda/calendário em PowerPoint** a partir de:

- um **slide modelo (.pptx)** já formatado
- datas geradas via Python
- versículos bíblicos lidos de um arquivo CSV

O layout, imagens, fontes e tamanhos do slide modelo são **preservados fielmente**.  
Apenas os textos dinâmicos são substituídos.

---

## 📂 Estrutura do Projeto

# 📅 Projeto Calendário em PowerPoint (PPT)

Este projeto gera automaticamente uma **agenda/calendário em PowerPoint** a partir de:

- um **slide modelo (.pptx)** já formatado
- datas geradas via Python
- versículos bíblicos lidos de um arquivo CSV

O layout, imagens, fontes e tamanhos do slide modelo são **preservados fielmente**.  
Apenas os textos dinâmicos são substituídos.

---

## 📂 Estrutura do Projeto

projeto_calendario_ppt/
│
├── calendario.py # Gera as datas do calendário
├── gerador_ppt.py # Duplica slides e substitui textos
├── leitor_versiculos.py # Lê e sorteia versículos do CSV
├── main.py # Orquestra todo o processo
├── modelo.pptx # Slide base (template)
├── versiculos.csv # Versículos bíblicos
└── README.md


---

## ⚙️ Dependências

Instale a dependência principal:

```bash
pip install python-pptx

```
Recomendado usar ambiente virtual (venv).

---
🧠 Como Funciona o Fluxo
---
calendario.py

Gera uma lista de datas com:

dia

mês (nome)

dia da semana

ano

leitor_versiculos.py

Lê o arquivo versiculos.csv

Retorna apenas a quantidade necessária (ex: 30 ou 50)

Evita carregar dados desnecessários

gerador_ppt.py

Duplica o slide modelo fielmente

Mantém:

imagens

layout

fontes

cores

tamanhos

Substitui apenas os textos marcados

main.py

Coordena todo o processo

Gera o arquivo final .pptx

---
📝 Marcadores no Slide Modelo
---
No arquivo modelo.pptx, utilize exatamente os seguintes marcadores:
```bash


{{DIA}}
{{MES}}
{{DIA_SEMANA}}
{{ANO}}
{{versiculo}}
{{localizacao}}

```
⚠️ Importante:
---
Os marcadores devem estar em um único bloco de texto

Evite quebrar o texto em múltiplos estilos no mesmo marcador

▶️ Como Executar
---
Na raiz do projeto:

python main.py


Após a execução, o arquivo final será gerado, por exemplo:

calendario_janeiro_2026.pptx

✅ Características Principais
---
✔ Layout preservado fielmente

✔ Imagens não são perdidas

✔ Fontes e tamanhos mantidos

✔ 1 slide por dia

✔ 1 versículo por slide

✔ CSV grande (1000+ linhas) suportado

🚀 Possíveis Extensões
---
Não repetir versículos

Versículo aleatório por slide

Exportação para PDF

Integração com Canva

Interface gráfica

📌 Observação Técnica
---
Este projeto utiliza operações internas do python-pptx para duplicação fiel de slides.
Essa abordagem é necessária porque a biblioteca não oferece cópia nativa de slides.

👤 Autor
---
Projeto desenvolvido para automação de agendas e materiais gráficos personalizados.


---
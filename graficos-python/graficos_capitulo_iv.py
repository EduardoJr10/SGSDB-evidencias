# -*- coding: utf-8 -*-
"""
Gráficos do Capítulo IV - Análise e interpretação dos dados
Monografia: Desenvolvimento de um sistema web para apoio aos processos de
inscrição e supervisão de estágios curriculares (ISDB).
 
Reproduz, a partir dos dados do questionário e das entrevistas, as figuras
quantitativas do Capítulo IV. Requer apenas matplotlib.
Execução:  python graficos_capitulo_iv.py
Gera ficheiros PNG (300 dpi, largura 15,5 cm) prontos a inserir no documento.
"""
from pathlib import Path
Path("figs").mkdir(exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
 
# --- Estilo comum (coerente com a monografia: serifa, preto, impressão) ---
rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "savefig.dpi": 300,
    "figure.dpi": 300,
})
AZUL = "#2F6690"      # cor primária (uma só série -> um só tom)
REALCE = "#B4452F"    # realce pontual para categorias críticas
INK = "#1A1A1A"
LARGURA_CM = 15.5
CM = 1 / 2.54
 
def nova_fig(altura_cm):
    return plt.subplots(figsize=(LARGURA_CM * CM, altura_cm * CM))
 
def barra_horizontal(labels, valores, ficheiro, unidade="n",
                     realce_idx=None, dec=0, xmax=None):
    """Barras horizontais, ordenadas de cima para baixo pela ordem dada."""
    fig, ax = nova_fig(0.9 * len(labels) + 3.2)
    y = range(len(labels))
    cores = [REALCE if (realce_idx and i in realce_idx) else AZUL for i in y]
    ax.barh(y, valores, color=cores, height=0.62, zorder=3)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, color=INK)
    ax.invert_yaxis()
    ax.set_xlabel(unidade, color=INK)
    ax.xaxis.grid(True, color="#D9D9D9", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    if xmax: ax.set_xlim(0, xmax)
    for i, v in zip(y, valores):
        txt = f"{v:.{dec}f}".replace(".", ",")
        ax.text(v + (max(valores) * 0.012), i, txt, va="center",
                ha="left", color=INK, fontsize=9)
    fig.tight_layout()
    fig.savefig(ficheiro, bbox_inches="tight"); plt.close(fig)
 
def barra_vertical(labels, valores, ficheiro, unidade="n",
                   realce_idx=None, dec=0):
    fig, ax = nova_fig(8.5)
    x = range(len(labels))
    cores = [REALCE if (realce_idx and i in realce_idx) else AZUL for i in x]
    ax.bar(x, valores, color=cores, width=0.64, zorder=3)
    ax.set_xticks(list(x)); ax.set_xticklabels(labels, color=INK, rotation=0)
    ax.set_ylabel(unidade, color=INK)
    ax.yaxis.grid(True, color="#D9D9D9", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for i, v in zip(x, valores):
        txt = f"{v:.{dec}f}".replace(".", ",")
        ax.text(i, v + max(valores) * 0.02, txt, ha="center",
                va="bottom", color=INK, fontsize=9)
    fig.tight_layout()
    fig.savefig(ficheiro, bbox_inches="tight"); plt.close(fig)
 
# ---------- Figura 1 - Distribuição dos estudantes por curso (Tabela 1) ----
cursos = ["Programação Informática", "Electricidade Industrial",
          "Administração de Sistemas", "Contabilidade e Gestão",
          "Mecânica Industrial", "Administração e Gestão"]
n_cursos = [10, 7, 7, 6, 6, 5]
barra_horizontal(cursos, n_cursos, "figs/fig_4_1_cursos.png", unidade="n.º de estudantes")
 
# ---------- Figura 2 - Situação face ao estágio (Tabela 2) -----------------
sit = ["Já concluiu", "Está a realizar", "Ainda não iniciou"]
n_sit = [23, 15, 3]
barra_horizontal(sit, n_sit, "figs/fig_4_2_situacao.png", unidade="n.º de estudantes")
 
# ---------- Figura 3 - Percepção do estado do pedido de carta (Tabela 5) ---
estado = ["Sempre", "Na maioria\ndas vezes", "Algumas\nvezes", "Raramente", "Nunca"]
pct_estado = [0.0, 6.3, 40.6, 37.5, 15.6]   # % de 32 requerentes
barra_vertical(estado, pct_estado, "figs/fig_4_3_estado_carta.png",
               unidade="% dos requerentes (n = 32)", realce_idx=[3, 4], dec=1)
 
# ---------- Figura 4 - Acompanhamentos recebidos (Tabela 7, D12) -----------
acomp = ["Nenhum", "Um", "Dois", "Três ou\nmais", "Não se\naplica"]
n_acomp = [1, 13, 21, 4, 2]
barra_vertical(acomp, n_acomp, "figs/fig_4_4_acompanhamentos.png",
               unidade="n.º de estudantes")
 
# ---------- Figura 5 - Orientação depois da supervisão (Tabela 8, D15) -----
orient = ["Sempre", "Frequente-\nmente", "Algumas\nvezes", "Raramente",
          "Nunca", "Ainda não\nsupervis."]
n_orient = [3, 7, 14, 10, 5, 2]
barra_vertical(orient, n_orient, "figs/fig_4_5_orientacao.png",
               unidade="n.º de estudantes", realce_idx=[3, 4])
 
# ---------- Figura 6 - Dificuldades na supervisão (Tabela 9) ---------------
dific = ["Disponibilidade e tempo do supervisor",
         "Marcação e coordenação das datas",
         "Acompanhamento, orientação e feedback",
         "Indisponibilidade do tutor da empresa",
         "Nervosismo do estudante",
         "Nenhuma dificuldade referida"]
n_dific = [5, 5, 4, 1, 1, 7]
barra_horizontal(dific, n_dific, "figs/fig_4_6_dificuldades.png",
                 unidade="n.º de respostas")
 
# ---------- Figura 7 - Importância das funcionalidades, médias (Tabela 10) -
func = ["Consultar datas de supervisão",
        "Fazer pedido de carta pelo sistema",
        "Notificação de carta pronta",
        "Consultar o supervisor atribuído",
        "Consultar o estado do pedido",
        "Notificações de supervisão",
        "Histórico das supervisões",
        "Histórico dos pedidos"]
medias = [4.49, 4.41, 4.35, 4.34, 4.27, 4.15, 3.95, 3.78]
barra_horizontal(func, medias, "figs/fig_4_7_importancia.png",
                 unidade="média (escala 1 a 5)", dec=2, xmax=5.0)
 
# ---------- Figura 8 - Indicadores centrais do diagnóstico (Tabela 11) -----
ind = ["Solicitaram carta",
       "Pediram por aplicações de mensagens",
       "Dificuldade em saber o estado da carta",
       "Contactos/deslocações pela carta",
       "Desconheciam o supervisor atribuído",
       "Querem documentos na plataforma",
       "Dificuldade em saber a data de supervisão",
       "Orientações raramente ou nunca recebidas"]
pct_ind = [78.0, 75.0, 53.1, 81.3, 43.9, 85.4, 34.1, 36.6]
barra_horizontal(ind, pct_ind, "figs/fig_4_8_indicadores.png",
                 unidade="%", dec=1, xmax=100)
 
print("Figuras geradas:")
import os
for f in sorted(os.listdir("figs")):
    print("  figs/" + f)

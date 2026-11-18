# Gráficos Python do Capítulo IV

Código Python e oito gráficos da monografia sobre o Sistema de Gestão de Estágios do Instituto Superior Dom Bosco. Este material é referido no Apêndice F; as imagens permanecem no corpo do trabalho.

## Conteúdo

- [graficos_capitulo_iv.py](graficos_capitulo_iv.py): gera os oito gráficos a partir dos valores agregados incluídos no próprio código.
- [figs/](figs/): gráficos exportados em PNG a 300 ppp.
- [requirements.txt](requirements.txt): versão da biblioteca utilizada na execução verificada.

O código foi extraído do Apêndice F da versão 10 da monografia. Os dados, as legendas e as instruções de desenho foram conservados. A única adaptação foi criar automaticamente a pasta `figs/`, caso ainda não exista.

## Como reproduzir

Execução verificada com Python 3.12.14 e Matplotlib 3.11.2.

Depois de descarregar ou clonar o repositório, abrir um terminal na pasta `graficos-python` e executar:

```sh
python -m pip install -r requirements.txt
python graficos_capitulo_iv.py
```

O programa guarda os oito PNG na pasta `figs/` e apresenta os respectivos nomes no terminal. Uma nova execução substitui esses ficheiros pelos gráficos novamente gerados.

## Correspondência com o trabalho

| Figura do Capítulo IV | Tema | Imagem |
| --- | --- | --- |
| 1 | Distribuição dos estudantes por curso | [PNG](figs/fig_4_1_cursos.png) |
| 2 | Situação dos estudantes face ao estágio curricular | [PNG](figs/fig_4_2_situacao.png) |
| 3 | Percepção do estado do pedido de carta | [PNG](figs/fig_4_3_estado_carta.png) |
| 4 | Acompanhamentos de supervisão recebidos | [PNG](figs/fig_4_4_acompanhamentos.png) |
| 5 | Frequência da orientação recebida depois da supervisão | [PNG](figs/fig_4_5_orientacao.png) |
| 6 | Principais dificuldades no processo de supervisão | [PNG](figs/fig_4_6_dificuldades.png) |
| 7 | Importância média atribuída às funcionalidades | [PNG](figs/fig_4_7_importancia.png) |
| 8 | Indicadores centrais do diagnóstico | [PNG](figs/fig_4_8_indicadores.png) |

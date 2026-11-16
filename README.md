# SGSDB diagramas

Diagramas UML do Sistema de Gestão de Estágios do Instituto Superior Dom Bosco, disponibilizados como material complementar da monografia de 2026.

Este repositório reúne os dez códigos PlantUML retirados do Apêndice D da monografia e as respectivas imagens. As imagens dos diagramas permanecem no trabalho.

## Consultar os diagramas

| Nº | Diagrama | Código UML | Imagem vectorial | Imagem PNG |
|---|---|---|---|---|
| 01 | Arquitectura do sistema | [PlantUML](uml/01-arquitectura.puml) | [SVG](svg/01-arquitectura.svg) | [PNG](png/01-arquitectura.png) |
| 02 | Casos de uso — Cartas e documentos | [PlantUML](uml/02-casos-uso-cartas.puml) | [SVG](svg/02-casos-uso-cartas.svg) | [PNG](png/02-casos-uso-cartas.png) |
| 03 | Casos de uso — Supervisão | [PlantUML](uml/03-casos-uso-supervisao.puml) | [SVG](svg/03-casos-uso-supervisao.svg) | [PNG](png/03-casos-uso-supervisao.png) |
| 04 | Diagrama de classes | [PlantUML](uml/04-classes.puml) | [SVG](svg/04-classes.svg) | [PNG](png/04-classes.png) |
| 05 | Estados do pedido de carta | [PlantUML](uml/05-estados-carta.puml) | [SVG](svg/05-estados-carta.svg) | [PNG](png/05-estados-carta.png) |
| 06 | Estados da marcação e da visita | [PlantUML](uml/06-estados-supervisao.puml) | [SVG](svg/06-estados-supervisao.svg) | [PNG](png/06-estados-supervisao.png) |
| 07 | Actividades do pedido de carta | [PlantUML](uml/07-actividades-carta.puml) | [SVG](svg/07-actividades-carta.svg) | [PNG](png/07-actividades-carta.png) |
| 08 | Actividades da supervisão | [PlantUML](uml/08-actividades-supervisao.puml) | [SVG](svg/08-actividades-supervisao.svg) | [PNG](png/08-actividades-supervisao.png) |
| 09 | Sequência do pedido de carta | [PlantUML](uml/09-sequencia-carta.puml) | [SVG](svg/09-sequencia-carta.svg) | [PNG](png/09-sequencia-carta.png) |
| 10 | Sequência das operações de supervisão | [PlantUML](uml/10-sequencia-supervisao.puml) | [SVG](svg/10-sequencia-supervisao.svg) | [PNG](png/10-sequencia-supervisao.png) |

## Organização

- `uml/`: códigos editáveis em PlantUML (`.puml`).
- `svg/`: imagens vectoriais, adequadas para ampliar sem perder definição.
- `png/`: imagens para consulta e inserção em documentos.

Os três ficheiros com o mesmo nome representam o mesmo diagrama. Para consultar o código, abrir a ligação PlantUML; para ver a imagem, abrir SVG ou PNG.

## Reprodução das imagens

Com Java e o compilador PlantUML instalados, executar a partir da raiz deste repositório:

```sh
java -jar plantuml.jar -tsvg -o ../svg uml/*.puml
java -jar plantuml.jar -tpng -o ../png uml/*.puml
```

Os diagramas descrevem os fluxos e entidades principais do protótipo. Não incluem credenciais, dados de estudantes ou documentos privados.

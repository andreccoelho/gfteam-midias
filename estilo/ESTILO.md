# Identidade visual dos reels da GFTeam Nova Iguaçu

Baseada no reel de horários (`referencia_reel_horarios.mp4`). Formato 1080x1920, 30 fps.

## Cores
- Fundo: verde escuro em gradiente, de `#0B2A25` (centro) a `#05140F` (bordas). Arquivo: `bg_shadow.png` (já com a sombra da moldura).
- Destaque: amarelo `#FFDD00` para a palavra-chave. Detalhe azul `#0050C8` (linha curta ao lado da barra amarela).
- Etiqueta (chip): fundo `#1F5E57`, ponto amarelo, texto `#DCF0EB`.
- Texto: branco.

## Fontes (pasta `fontes/`)
- **Anton**: títulos, etiquetas e legenda. Sempre em caixa alta.
- **Inter** (Regular e Bold): linha de apoio abaixo do título.

## Cena com título (padrão)
- Gradiente escuro no topo (até ~820 px, opacidade ~240) e embaixo (a partir de 1250 px).
- Etiqueta no canto superior esquerdo: x=60, y=140, Anton 46, ex.: `1º MOTIVO`.
- Título: x=60, y=245, Anton 100, linhas de 112 px. Palavra-chave em amarelo. Sombra preta deslocada 3 px.
- Linha de apoio: Inter Regular 34, branca, 32 px abaixo da última linha do título.
- Barra amarela (70x5) + azul (40x5) logo abaixo.
- O título entra com fade de 0,45 s na primeira cena da seção e permanece nas seguintes.

## Mídias
- **Verticais** (fotos e vídeos): tela cheia, recorte `scale=increase,crop=1080:1920`. Fotos com zoom lento de 6%.
- **Horizontais**: moldura 1000x562, x=40, y=760, cantos arredondados (raio 24), borda amarela de 4 px (`mask.png`, `cardfx.png`), sobre `bg_shadow.png`. Sem fundo desfocado.
- Transição: dissolve (`xfade=fade`) de 0,3 s. Cada trecho é renderizado 0,3 s mais longo para a duração total não mudar.

## Legenda (`scripts/gerar_legenda.py`)
- ASS gravado no vídeo (libass), Anton 88, branca, contorno preto 6, centralizada, margem inferior 300.
- 3 a 4 palavras por trecho. Palavras-chave em amarelo. Entrada com fade de 70 ms e pequeno zoom.
- Não usar legenda sobre o cartão final de horários.

## Cartão final
Os últimos ~7 s do `referencia_reel_horarios.mp4` (a partir de 26,0 s): logo, HORÁRIOS (Baby, Infantil 1, Teen) e botão "Chame no direct e agende uma visita".

## Capa
Fundo verde, etiqueta, título gigante (Anton 128) com palavras-chave em amarelo, foto de baixo para cima com degradê e rodapé com nome e @ da academia. Manter título e rosto dentro da área central 4:5 (y 285 a 1635), que é o que o grid do perfil mostra.

## Estrutura do reel "5 motivos" (120 s, áudio em `audio/`)
| Trecho | Conteúdo |
|---|---|
| 0:00 | Abertura: 5 motivos para colocar seu filho na luta |
| 0:08 | 1º Regulação emocional |
| 0:27 | 2º Consciência corporal |
| 0:46 | 3º Atenção sustentada |
| 1:00 | 4º Autoestima construída em cima de competência real |
| 1:16 | 5º Contato físico e hierarquia |
| 1:33 | Duas coisas importantes (saúde mental e escolha do professor) |
| 1:53 | Cartão de horários |

Mistura de turmas em todas as seções: kids, juvenil e mistas.

## Cuidados
- O áudio do reel é de outro criador. Conferir se o Instagram libera o som antes de postar.
- Revisar a legenda: ela vem de transcrição automática com correções manuais.

# 🌱 The Farmer Was Replaced

Código desenvolvido durante o progresso em **The Farmer Was Replaced**.

O repositório serve para registrar as automações feitas durante o jogo e deixar o código disponível para quem quiser **usar ou adaptar**.

> **A lógica e a programação do código foram desenvolvidas sem uso de IA.**

## 📂 Arquivos

```text
main.py       # Rota e estratégia da fazenda
mega.py       # Movimentação e execução das rotas
utility.py    # Funções auxiliares
```

## ⚙️ Como funciona

### `main.py`

Define a rota da fazenda, indicando:

- Coluna
- Direção
- O que plantar
- Ordem de execução

Rota atual:

```text
0 ↑ Cenoura
1 ↓ Madeira
2 ↑ Árvore
3 ↓ Árvore
4 ↑ Árvore
5 ↓ Abóbora / Grama
6 ↑ Grama / Abóbora
7 ↓ Grama
```

### `mega.py`

Possui as funções para percorrer as colunas:

- `sobe()` → percorre a coluna de baixo para cima
- `desce()` → percorre a coluna de cima para baixo

Durante o percurso, o código:

```text
Colhe → Planta → Rega → Move
```

### `utility.py`

Funções utilizadas pela automação:

- `planta()` → escolhe o que plantar
- `colhe()` → verifica e realiza a colheita
- `mov_direita()` → passa para a próxima coluna
- `agua_solo()` → rega quando necessário
- `centralizar()` → retorna à posição inicial

## 🔧 Adaptando

A rota e as plantações podem ser alteradas diretamente no `main.py`.

Exemplo:

```python
mega.sobe(0, "cenoura")
mega.desce(1, "madeira")
mega.sobe(2, "arvore")
```

Também é possível adicionar novos tipos de plantação e modificar as funções do `utility.py` conforme novas necessidades.

## 📈 Progresso

O código será atualizado conforme novos recursos, áreas e automações forem desbloqueados.

A ideia é manter aqui as versões utilizadas durante o progresso, além de disponibilizar uma base que possa ser adaptada para diferentes fazendas e estratégias.

## ⚠️ Observação

O código representa as estratégias desenvolvidas até o momento e não necessariamente a forma mais eficiente de automatizar cada recurso.

Use, modifique e adapte como quiser.

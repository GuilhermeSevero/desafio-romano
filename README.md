# Desafio - Números Romanos
Algoritmo de Conversão de Números Romanos


## Detalhes de Implementação

Realizada implementação orientada à funcionalidade. Pensando na possibilidade em extrair o pacote para um repositorio 
privado/publico (Ex.: https://pypi.org/). <br>
Não achei necessário usar OOP, pois não faz sentido criar um objeto, visto não há a necessidade de guardar qualquer estado nas conversões. 


---

## Exemplo de Uso
###### Obs.: Implementado alguns exemplos de uso.  (Disponível em: `./index.py`)

**Romano para Decimal:**

```python
from roman import to_decimal

romano = 'CXXXVIII'
decimal = to_decimal(romano)

print(decimal)

```

**Decimal para Romano:**

```python
from roman import to_roman

decimal = 138
romano = to_roman(decimal)

print(decimal)

```

---

## Unit Tests

```bash
$ python -m unittest discover -s ./tests/
```

---

## Implementação Futura

Como o foco da implementação é a simplicidade, não foi realizada validação para identificar se o numeral romano 
passado para conversão. <br>
###### Ex.: Se for passado um valor de `CMXCVVIIII`, a função `to_decimal` irá converter com sucesso para `1004`.

Dessa forma, as funções estão abertas para a implementação de validação dos valores. 

# SombraSP — Alerta de Calor em São Paulo

## Ficha da CitizenTech

| Campo | Resposta |
|---|---|
| **Nome da CitizenTech** | SombraSP |
| **Cidade e bairro** | São Paulo — Bela Vista (região da Av. Paulista, onde fica a FIAP) |
| **Cidadão beneficiado** | Idosos e trabalhadores de rua que passam o dia ao ar livre na região, principalmente nos dias mais quentes |
| **Problema, em uma frase** | Em dias de calor extremo, quem fica na rua não sabe se o calor já está perigoso nem onde encontrar sombra e água por perto |
| **Como funciona** | O usuário registra a temperatura de um bairro; o programa classifica o risco (normal, atenção ou perigo) conforme o grupo observado, dá uma orientação e mostra os pontos de apoio (sombra/hidratação) cadastrados no bairro. Tudo é salvo em JSON |
| **O que cada parte faz** | **Python (Lógica):** menu que registra temperatura e pontos de apoio em JSON e classifica o risco. **Demais partes do projeto:** _(completar com as outras disciplinas da equipe)_ |
| **Link do repositório** | _(colar aqui o link do repositório no GitHub)_ |
| **Indicador de impacto** | Quantidade de registros em nível "perigo" e de pontos de apoio cadastrados por bairro (opção 6 do menu) |
| **ODS conectados** | ODS 3 (Saúde e Bem-Estar), ODS 11 (Cidades e Comunidades Sustentáveis) e ODS 13 (Ação contra a Mudança Global do Clima) |

## Integrantes

| Nome | RM |
|---|---|
| Leonardo Teodoro Leitão | 569724 |
| Gustavo Almeida Lopes do Nascimento | 571070 |
| João Gabriel Mosqueti Agra Cunha | 572017 |
| Rafael Yuta Nischida | 570552 |

## Sobre o projeto

Aplicação de terminal em Python feita para a **Global Solution 2026.2 (FIAP)**, disciplina **Computational Thinking with Python**. O tema escolhido foi **calor extremo**, um dos pontos de partida sugeridos para São Paulo. A ideia é que moradores, voluntários ou agentes locais registrem a temperatura de um bairro e ajudem a mapear onde há sombra e água.

## Como executar

Requisito: **Python 3.10 ou superior** (o programa usa `match/case`). Não é preciso instalar nenhuma biblioteca.

Abra o terminal dentro da pasta do projeto e rode:

```bash
python main.py
```

O arquivo `dados.json` é criado/atualizado automaticamente (rode sempre de dentro da pasta, para ele ficar junto do código).

## Menu

| Opção | O que faz |
|---|---|
| 1 | Registra temperatura (bairro, °C, grupo observado) e classifica o risco |
| 2 | Cadastra ponto de apoio (nome, tipo, bairro, referência) |
| 3 | Lista os registros de temperatura |
| 4 | Lista os pontos de apoio, com filtro por tipo |
| 5 | Consulta a situação de um bairro (último risco + pontos de apoio do bairro) |
| 6 | Resumo geral (quantidade por risco, mínima/máxima/média e total de pontos) |
| 7 | Remove um registro de temperatura |
| 8 | Remove um ponto de apoio |
| 0 | Sai do programa |

Depois de cada opção, o programa pergunta **"Deseja mais alguma coisa?"**. Assim o resultado fica visível na tela antes de o menu aparecer de novo.

Cada registro de temperatura mostra: **Bairro, dia e hora, temperatura, grupo observado e risco**.

## Regras de classificação de risco

| Grupo observado | Normal | Atenção | Perigo |
|---|---|---|---|
| Geral | abaixo de 30 °C | 30 °C a 34,9 °C | 35 °C ou mais |
| Idosos, Trabalhadores de rua, Crianças | abaixo de 27 °C | 27 °C a 31,9 °C | 32 °C ou mais |

Os limites são **didáticos**, definidos pela equipe (não são limites oficiais) e podem ser ajustados na função `classificar_risco` do arquivo `services.py`.

## Estrutura do projeto

```
SombraSP/
├── main.py          # Ponto de entrada: menu e laço principal
├── controller.py    # O que cada opção do menu faz (cadastrar, listar, consultar, remover)
├── services.py      # Regras do sistema: classificação de risco, buscas e cálculos
├── database.py      # Leitura e gravação do arquivo JSON
├── validacoes.py    # Leitura e validação das entradas do usuário
├── dados.json       # Dados salvos (registros e pontos de apoio)
├── prompts.md       # Documentação do uso de IA
├── README.md        # Este arquivo
└── .gitignore
```

## Requisitos da atividade e onde estão no código

| Requisito | Onde |
|---|---|
| Menu de opções | `main.py` — `exibir_menu()` e `main()` |
| Validação das entradas | `validacoes.py` — `ler_texto`, `ler_inteiro`, `ler_float`, `escolher_opcao`, `confirmar` |
| Tratamento de exceções (try/except) | `validacoes.py` (`ValueError`, quando o usuário digita texto no lugar de número), `database.py` (`FileNotFoundError`, `JSONDecodeError` e erro ao salvar) |
| Decisão (if/elif/else e match/case) | `services.classificar_risco` (if/elif/else); `services.gerar_recomendacao` e `main.main` (match/case) |
| Repetição (while e for) | `while`: menu e validações; `for`: listagens, contagens e buscas |
| Funções com parâmetros e retorno | `services.py`, `validacoes.py`, `database.py` e `controller.py` |
| Listas, tuplas e dicionários | Listas: `registros` e `pontos`; tuplas: `GRUPOS`, `TIPOS_PONTO`, `FILTROS_PONTO`, `NIVEIS` e o retorno de `calcular_estatisticas`; dicionários: cada registro/ponto e `contar_por_risco` |
| Arquivos JSON (leitura e gravação) | `database.py` — `carregar_dados` e `salvar_dados` |
| Boas práticas | Arquivos separados por responsabilidade, nomes descritivos, constantes no topo, funções pequenas e sem repetição de código |
| Experiência do usuário | Menu claro, mensagens de erro explicando o que digitar, pergunta "Deseja mais alguma coisa?" ao final de cada ação, confirmação antes de remover, orientação ao cidadão por nível de risco |

## Limites e restrições adotados

Seguindo o enunciado da atividade:

- Só usamos recursos vistos na disciplina: `input`/`print`, variáveis, `if/elif/else`, `match/case`, `while`, `for`, funções, listas, tuplas, dicionários, `try/except` e arquivos JSON.
- **Nenhuma biblioteca externa**: apenas módulos que já vêm com o Python (`json` e `datetime`). Não usamos frameworks (como FastAPI ou Streamlit), banco de dados, classes ou bibliotecas de gráficos.
- A persistência é feita somente em arquivo JSON local.
- O programa funciona em terminal, sem interface gráfica.
- Os limites de temperatura são didáticos e a classificação não substitui alertas oficiais de órgãos de meteorologia ou de saúde.

## Formato do `dados.json`

```json
{
    "registros": [
        {
            "bairro": "Bela Vista",
            "data_hora": "10/11/2026 14:30",
            "temperatura": 36.5,
            "grupo": "Geral",
            "risco": "perigo"
        }
    ],
    "pontos": [
        {
            "nome": "Praça Exemplo",
            "tipo": "Sombra e hidratação",
            "bairro": "Bela Vista",
            "referencia": "Perto do metrô"
        }
    ]
}
```

## Uso de IA

O uso de ferramentas de IA está documentado no arquivo [`prompts.md`](prompts.md).

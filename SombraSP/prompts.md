# Uso de IA no projeto SombraSP

Projeto: **SombraSP — Alerta de Calor em São Paulo** (Global Solution 2026.2 · Computational Thinking with Python)

## 1. Ferramentas de IA utilizadas e finalidades

| Ferramenta | Finalidade |
|---|---|
| Claude (Anthropic) | Escolher o problema do tema (calor extremo), explicar o passo a passo do projeto, gerar a base inicial do código (menu, funções de validação, funções de regras de risco e funções de persistência em JSON), sugerir o nome do projeto, ajudar a preencher a Ficha do README e revisar a estrutura do repositório |
| ChatGPT (OpenAI) | Revisar o código para ter uma segundo opnião de se tem alguma coisa faltando ou deixe de seguir alguma das regras |

## 2. Prompts utilizados

**Prompt 1** (resumo do pedido, junto com prints do enunciado da atividade)

> Gere uma estrutara básica para o meu projeto seguindo o que as prints falam: aplicação em Python com menu, validações, try/except, if/elif/else e match/case, while e for, funções com parâmetros e retorno, listas, tuplas e dicionários e persistência em JSON. Tema: menu que registra temperatura e pontos de apoio em JSON e classifica o risco (normal, atenção, perigo).

Finalidade: gerar a base do projeto

**Prompt 2** (Correções)

> Arrume o README.md do meu projeto conforme as alterações que foram feitas.

Finalidade: Correções do documento README.md

**Prompt 3** (Revisão)

> Faça uma revisão clara no código, verifique seguindo os parâmetros que se pedem no enunciado da atividade e me mande o que devo alterar 

Finalidade: Correções finais do projeto

## 3. Funcionalidades desenvolvidas, sugeridas ou modificadas com ajuda da IA

| Arquivo | Funções | O que faz |
|---|---|---|
| `main.py` | `exibir_menu`, `main` | Menu principal em laço `while` com `match/case` e a pergunta "Deseja mais alguma coisa?" |
| `controller.py` | `registrar_temperatura`, `cadastrar_ponto` | Cadastro de dados, salvando no JSON |
| `controller.py` | `remover_registro`, `remover_ponto` | Remoção por número da lista, com confirmação |
| `controller.py` | `mostrar_registros`, `mostrar_pontos`, `listar_registros`, `listar_pontos`, `consultar_bairro`, `resumo_geral` | Consultas e indicadores |
| `services.py` | `classificar_risco` | Classifica em normal, atenção ou perigo (if/elif/else) |
| `services.py` | `gerar_recomendacao` | Orientação ao cidadão por nível de risco (match/case) |
| `services.py` | `contar_por_risco`, `calcular_estatisticas`, `buscar_ultimo_registro`, `buscar_pontos_por_bairro`, `filtrar_pontos` | Buscas, contagens e filtros em listas e dicionários |
| `validacoes.py` | `ler_texto`, `ler_inteiro`, `ler_float`, `escolher_opcao`, `confirmar` | Validação de entradas com `try/except` |
| `database.py` | `carregar_dados`, `salvar_dados` | Leitura e gravação em JSON, com tratamento de arquivo ausente ou com problema |

A IA gerou a primeira versão de todo o código e dos textos do README. O tema (calor extremo), o nome e os limites de temperatura devem ser entendidos e validados pela equipe.

## 4. Limites adotados no uso da IA e no código

Seguindo as restrições do enunciado, pedimos e mantivemos o código dentro destes limites:

- Apenas estruturas listadas no enunciado: menu, validações, `try/except`, `if/elif/else`, `match/case`, `while`, `for`, funções com parâmetros e retorno, listas, tuplas, dicionários e JSON.
- Sem bibliotecas externas: somente `json` e `datetime`, que já vêm com o Python.
- Sem frameworks, API web, banco de dados, classes ou gráficos, mesmo que esses assuntos tenham aparecido nas aulas, porque o enunciado pede só o que está na lista acima.
- Persistência apenas em arquivo JSON local; interface apenas em terminal.

## 5. Como o grupo verificou, testou e ajustou os resultados

**Testes feitos durante a geração do código** (execução do programa com entradas simuladas):

- Classificação nos limites exatos de cada faixa para o grupo "Geral" e para os grupos sensíveis.
- Entradas inválidas: texto no lugar de número, temperatura fora do intervalo, opção de menu inexistente e textos curtos demais. O programa repetiu a pergunta sem travar.
- Persistência: registros e pontos gravados no `dados.json` e lidos novamente.
- Remoção de registro de temperatura e de ponto de apoio, com o `dados.json` atualizado.
- Pergunta "Deseja mais alguma coisa?" após cada opção, encerrando o programa quando a resposta é não.
- Arquivo JSON ausente ou corrompido: o programa abre com dados vazios, sem quebrar.

**Conferência manual do grupo** (marcar conforme cada integrante testar):

- [ ] Rodar `python main.py` em cada computador e percorrer todas as opções do menu
- [ ] Conferir se o `dados.json` é atualizado após registrar e após remover
- [ ] Conferir se cada integrante consegue explicar o que cada função faz
- [ ] Confirmar com o professor se o módulo `datetime` pode ser usado
- [ ] Ajustar bairros, tipos de apoio e limites de temperatura à realidade escolhida pela equipe

## 6. Análise crítica

**Benefícios:** a IA acelerou a estruturação do projeto (divisão em arquivos), sugeriu uma organização clara de funções e ajudou a relacionar cada requisito do enunciado com o código. Também ajudou a pensar em casos de erro que costumam ser esquecidos, como o JSON corrompido.

**Limitações:** a IA não conseguiu abrir o código dos repositórios de referência (só os READMEs), então os nomes dos arquivos foram inspirados na estrutura deles e o restante foi guiado pelo enunciado. Os limites de temperatura são didáticos e não vêm de uma fonte oficial. O código gerado precisa ser entendido e testado pelo grupo antes da entrega.

**Dificuldades:** os repositórios anteriores da equipe usavam bibliotecas externas que o enunciado desta atividade restringe, então foi preciso adaptar o estilo para usar apenas a biblioteca padrão. Também foi necessário manter o código simples o bastante para o grupo conseguir ajusta-lo e explica-lo.

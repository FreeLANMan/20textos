# 20textos
Script em Python para um LLM criar 20 textos em formato .txt sobre um tema automaticamente.

## Aviso:
- **Não me responsabilizo pelo material produzido por esse script.** A qualidade do material produzido é diretamente relacionada com o modelo escolhido. E se você utilizar esse script para produzir material danoso ou ilegal a responsabilidade é sua.
- **Não me responsabilizo se seu computador superaquecer ou pegar fogo.** Deixar um LLM funcionando por vários minutos ou horas pode superaquecer o seu computador. Monitore a temperatura e utilize ferramentas de controle de temperatura (como por exemplo [RyzenAdj](https://github.com/FlyGoat/RyzenAdj)).


## Função e Limitações 
O que você pode fazer com esse script:
- Automatizar a produção de conteúdos diversos com características que você escolher. Tutoriais, posts em redes sociais, etc.

O que você não consegue fazer com esse script:
- Criar automaticamente 20 aplicativos.

## O que você precisa e como usar:
Para executar o script Python que gerencia a comunicação com o **LM Studio** através da biblioteca da OpenAI, você precisará configurar tanto o ambiente de software quanto o ambiente de execução local.

Abaixo estão os requisitos detalhados:

### 1. Aplicativo Principal (Backend de IA)

* **LM Studio:** É o software essencial para carregar e servir os modelos de linguagem (LLMs) localmente. Você deve baixá-lo em [lmstudio.ai](https://lmstudio.ai).
* **Configuração:** Após baixar um modelo (recomendo o google/gemma-3n-e4b: gemma-3n-E4B-it-Q4_K_M.gguf), você deve ir na aba **"AI Chat"** ou **"Local Server"** e clicar em **"Start Server"**.
* **Porta:** O script está configurado para buscar o endereço `http://127.0.0.1:1234`. Certifique-se de que o LM Studio está rodando nessa porta.

### 2. Ambiente Python

* **Python 3.8 ou superior:** Recomendado para garantir compatibilidade com as bibliotecas modernas.
* **PIP:** O gerenciador de pacotes do Python (geralmente já vem instalado com o Python).

### 3. Bibliotecas Python (Pacotes)

Você precisará instalar a biblioteca oficial da OpenAI, que o script utiliza para se comunicar com a API local do LM Studio.

Abra o seu terminal ou prompt de comando e execute:

```bash
pip install openai

```
### 4. Resumo de Dependências Internas

O script utiliza algumas bibliotecas que já fazem parte da **Standard Library** do Python (você não precisa instalá-las manualmente):

* `time`: Para gerenciar os intervalos entre as requisições e evitar sobrecarga no servidor local.
* `os`: Para criar a pasta "Pronto" e gerenciar os caminhos dos arquivos.
* `re`: Para realizar a limpeza de nomes de arquivos e extração da lista de 20 itens via Regex.

---

### Check-list de Execução

1. [ ] **LM Studio** aberto e com o **Local Server** iniciado.
2. [ ] Um modelo de texto (LLM) carregado no LM Studio.
3. [ ] Biblioteca `openai` instalada via pip.
4. [ ] Script salvo como `.py` e executado via terminal (`python 20textos.py`).

---

## Resultados dos testes:

Realizei várias avaliações usando Gemini 3 Rápido e DeepSeek para saber a qualidades dos materiais produzidos.
- Foi utilizado o LLM gemma-3n-E4B-it-Q4_K_M.gguf que ocupa ~4GB. Foram mantidas as configurações padrão do aplicativo e modelo (menos Temperatura=0,7): Amostragem TOp-K=40, Penalidade de Repetição = 1,1, Amostragem Min-P = 0,05, etc.
- A nota mais baixa verificada nas avaliações foi de 6/10 e mais alta 10/10.
- Os textos produzidos estão nas pastas Testes1 e Teste2.
- Links para você mesmo ler as avaliações:
#### Teste 1:
DeepSeek: 
[https://chat.deepseek.com/share/306ibamg2ezt0y2n3p]
Gemini:
[https://gemini.google.com/share/4027d53dee0b] 
Backup dos links:
DeepSeek: [https://archive.is/CCHGe]
Gemini: [https://archive.ph/mshey]
#### Teste 2:
- DeepSeek: 
[https://chat.deepseek.com/share/306ibamg2ezt0y2n3p
](https://chat.deepseek.com/share/dfvbkoxsv7x0lmdo4l)
- Gemini:
[https://gemini.google.com/share/4027d53dee0b](https://gemini.google.com/share/fa67cef32f5a)
Backup dos links:
DeepSeek: [https://archive.is/isC1R](https://archive.is/isC1R) 
Gemini: [https://archive.ph/mshey](https://archive.ph/Uho15)

Script criado com Gemini 3 Rápido em Janeiro de 2026.

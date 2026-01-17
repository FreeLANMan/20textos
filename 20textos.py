import time
import os
import re
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def limpar_modelo():
    try:
        client.chat.completions.create(model="local-model", messages=[], max_tokens=1)
    except:
        pass

def perguntar(system, mensagem):
    limpar_modelo()
    resp = client.chat.completions.create(
        model="local-model",
        temperature=0.7, # Aumentado levemente para maior criatividade na escrita
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": mensagem}
        ]
    )
    if not resp.choices:
        raise RuntimeError("Resposta inválida do LM Studio")
    return resp.choices[0].message.content

def salvar_resposta(tema_geral, item_nome, conteudo):
    os.makedirs("Pronto", exist_ok=True)
    # Limpa o nome do arquivo
    nome_limpo = re.sub(r"[^\w\-]", "_", item_nome[:40]).lower()
    caminho = os.path.join("Pronto", f"{nome_limpo}.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho

# ===============================
# Entrada do usuário
# ===============================
tema_geral = input("\n📝 Sobre o que você quer gerar 20 conteúdos? \n> ").strip()

if not tema_geral:
    print("Nenhum tema informado. Encerrando.")
    exit(1)

try:
    # --- IA1: GERADOR DE LISTA ---
    print(f"\n🟡 IA1 — Gerando lista de 20 itens para: {tema_geral}...")
    prompt_lista = (
        f"Com base no tema '{tema_geral}', crie uma lista numerada de 1 a 20 com títulos de "
        "textos, tutoriais ou códigos que devem ser escritos. Retorne APENAS a lista."
    )
    lista_bruta = perguntar("Você é um organizador de conteúdo. Gere apenas a lista.", prompt_lista)
    
    # Extrair itens da lista usando regex (pega o texto após o número)
    itens_pendentes = re.findall(r"\d+[\.\s]+(.+)", lista_bruta)
    print(lista_bruta)
    if len(itens_pendentes) < 1:
        print("Erro ao gerar lista. Verifique a resposta da IA1.")
        #print(lista_bruta)
        exit(1)

    print(f"✅ Lista criada com {len(itens_pendentes)} itens.")

    # --- LOOP DE PRODUÇÃO (IA2 e IA3) ---
    contador = 1
    while itens_pendentes:
        item_atual = itens_pendentes.pop(0) # Pega o primeiro e remove da lista
        
        print(f"\n--- Processando {contador}/20: {item_atual} ---")
        print(f"⏳ Itens restantes na fila: {len(itens_pendentes)}")

        # IA2: Cria o conteúdo
        print(f"🟢 IA2 — Escrevendo conteúdo...")
        instrucao_ia2 = f"Escreva um texto completo, tutorial ou código sobre o título fornecido."
        texto_bruto = perguntar(instrucao_ia2, f"Título: {item_atual}")

# Salva o resultado final
        #caminho = salvar_resposta(tema_geral, f"{contador}_{item_atual}", texto_bruto)
        caminho = salvar_resposta(tema_geral, f"{item_atual}", texto_bruto)
        print(f"💾 Salvo em: {caminho}")

        contador += 1

        time.sleep(2)

    print("\n\n✨ Missão cumprida! Todos os 20 itens foram gerados na pasta 'Pronto'.")

except KeyboardInterrupt:
    print("\n\nInterrompido pelo usuário. O progresso salvo está na pasta 'Pronto'.")

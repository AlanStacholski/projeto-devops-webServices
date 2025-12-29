import time
import random
import requests
from threading import Thread

# URL local onde o Docker expôs a API
URL = "http://localhost:8000"

def bot_usuario(id):
    print(f"Bot #{id} iniciado...")
    endpoints = ["/", "/transacao", "/transacao", "/cliente"]
    
    while True:
        try:
            target = random.choice(endpoints)
            requests.get(f"{URL}{target}")
            # Pausa aleatória entre requisições
            time.sleep(random.uniform(0.5, 2.0))
        except Exception as e:
            print(f"Erro no Bot {id}: {e}")
            time.sleep(5)

if __name__ == "__main__":
    print("Iniciando Teste de Carga Local...")
    print("Pressione CTRL+C para parar.")
    
    # Cria 10 bots simultâneos
    for i in range(10):
        t = Thread(target=bot_usuario, args=(i,))
        t.daemon = True # Mata as threads quando fechar o script
        t.start()
        
    while True:
        time.sleep(1)
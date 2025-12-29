import time
import random
from fastapi import FastAPI, Response
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Habilita as métricas do Prometheus
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"status": "Online", "service": "Flash Project"}

@app.get("/transacao")
def processar_transacao():
    # Simula tempo de processamento aleatório (Latência)
    time.sleep(random.uniform(0.1, 0.8))
    
    # Simula erro ocasional (10% de chance de erro 500)
    if random.random() < 0.1:
        return Response(status_code=500)
    
    return {"msg": "Transação aprovada", "valor": random.randint(10, 500)}

@app.get("/cliente")
def buscar_cliente():
    # Resposta rápida
    return {"id": 1, "nome": "Cliente Teste"}
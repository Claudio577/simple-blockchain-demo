import hashlib
import json
from datetime import datetime

# ===== Classe do Bloco =====
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        bloco = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(bloco.encode()).hexdigest()

# ===== Classe da Blockchain =====
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.now()), "Bloco Gênese", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.now()), data, prev_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            atual = self.chain[i]
            anterior = self.chain[i-1]

            if atual.hash != atual.calculate_hash():
                return False
            if atual.previous_hash != anterior.hash:
                return False
        return True

# ===== Teste do Sistema =====
bc = Blockchain()
bc.add_block("Fornecedor enviou o lote 001")
bc.add_block("Fabricante produziu o item com lote 001")
bc.add_block("Varejista recebeu o item e colocou à venda")

# Mostrar os blocos
for bloco in bc.chain:
    print(f"\nBloco {bloco.index}")
    print(f"Data: {bloco.timestamp}")
    print(f"Dados: {bloco.data}")
    print(f"Hash: {bloco.hash[:20]}...")
    print(f"Anterior: {bloco.previous_hash[:20]}...")

# Verificar se a cadeia é válida
print("\n✅ Blockchain válida?", bc.is_chain_valid())

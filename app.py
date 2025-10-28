import streamlit as st
import hashlib
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


# ===== INTERFACE STREAMLIT =====
st.set_page_config(page_title="Blockchain Demo", page_icon="🧱", layout="wide")
st.title("🧱 Simple Blockchain Demo")
st.markdown("Simulação visual de uma **blockchain realista** — com blocos encadeados e verificação de integridade.")

# Inicializa a blockchain na sessão
if "bc" not in st.session_state:
    st.session_state.bc = Blockchain()

# Entrada de dados
st.subheader("📦 Adicionar novo bloco")
novo_dado = st.text_input("Digite o conteúdo do novo bloco:")

if st.button("Adicionar bloco"):
    if novo_dado.strip():
        st.session_state.bc.add_block(novo_dado)
        st.success("✅ Bloco adicionado com sucesso!")
    else:
        st.warning("Digite algum dado antes de adicionar um bloco.")

# Mostrar os blocos existentes
st.subheader("🔗 Cadeia de Blocos")
for bloco in st.session_state.bc.chain:
    with st.expander(f"🧩 Bloco {bloco.index}"):
        st.write(f"**Data/Hora:** {bloco.timestamp}")
        st.write(f"**Dados:** {bloco.data}")
        st.code(f"Hash: {bloco.hash}")
        st.code(f"Anterior: {bloco.previous_hash}")

# Validar integridade
if st.session_state.bc.is_chain_valid():
    st.success("✅ Blockchain válida e íntegra!")
else:
    st.error("⚠️ Blockchain comprometida!")

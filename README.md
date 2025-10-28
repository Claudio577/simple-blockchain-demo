# 🧱 Simple Blockchain Demo

Este projeto demonstra, de forma simples e didática, o funcionamento de uma **blockchain realista**, com blocos encadeados, hashes únicos e validação de integridade.

## 🚀 Funcionalidades

- Criação de blocos com hash SHA-256
- Encadeamento entre blocos (`previous_hash`)
- Verificação automática de integridade (`is_chain_valid`)
- Exemplo prático da cadeia de suprimentos:
  - Fornecedor → Fabricante → Varejista

## 🧩 Estrutura de cada bloco

```json
{
  "index": 1,
  "timestamp": "2025-10-28 10:00:00",
  "data": "Fornecedor enviou o lote 001",
  "previous_hash": "abc123...",
  "hash": "def456..."
}



# 🛡️ Projeto: Honeypot Simples em Python

## 📌 Descrição

Este projeto é um **honeypot educacional** desenvolvido em Python. Ele simula serviços comuns como **FTP (porta 21)**, **SSH (22)** e **HTTP (80)**, com o objetivo de **registrar interações de atacantes** e demonstrar como técnicas básicas de monitoramento podem ser aplicadas em ambientes de **segurança ofensiva e defensiva**.

> ⚠️ **Aviso:** Este projeto é para fins **educacionais e laboratoriais**. Não deve ser usado em ambientes de produção ou conectado diretamente à internet sem proteção adequada.

---

## ⚙️ Funcionalidades

- 🎧 Escuta múltiplas portas (FTP, SSH, HTTP)
- 🧠 Responde com mensagens falsas (emulação simples de serviço)
- 📝 Registra:
  - IP e porta de origem
  - Data e hora da conexão
  - Mensagens enviadas pelo invasor
- 📂 Armazena tudo em um arquivo `honeypot_log.txt`

---

## 🧰 Tecnologias Utilizadas

- 🐍 Python 3.x
- 🔌 `socket` (biblioteca padrão)
- 🔄 `threading` para múltiplas conexões simultâneas
- 📆 `datetime` para marcação de tempo

---

## 🚀 Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

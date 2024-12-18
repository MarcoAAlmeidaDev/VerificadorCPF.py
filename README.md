# Validador de CPF em Python

Este projeto é uma ferramenta simples para **validação de CPF** desenvolvida em **Python**. O código recebe um CPF como entrada (com ou sem caracteres especiais) e valida se o número é correto, de acordo com os dois últimos dígitos verificadores.

---

## 🚀 Funcionalidades

- **Remoção de Caracteres Especiais**: O CPF pode ser inserido com ou sem pontos e traços, que são removidos automaticamente.
- **Validação Completa**: O código verifica se o CPF contém os dois últimos dígitos verificadores corretos, utilizando o algoritmo de cálculo oficial.
- **Checagem de CPF Inválido**: O sistema também detecta CPFs com todos os números iguais (ex.: 111.111.111-11), que são considerados inválidos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem utilizada para o desenvolvimento do código.
- **Expressões Regulares (Regex)**: Para tratar a entrada de dados, removendo caracteres especiais de forma eficaz.

---

## 📦 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

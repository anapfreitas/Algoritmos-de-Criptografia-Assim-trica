# 🔐 Criptografia Assimétrica com RSA em Python

Este projeto demonstra uma implementação prática do algoritmo **RSA (Rivest–Shamir–Adleman)**, uma das técnicas mais conhecidas de **criptografia assimétrica**, utilizando a linguagem Python.

O sistema realiza a cifragem (criptografia) e a decifragem (decriptação) de mensagens com segurança, garantindo que apenas o destinatário correto possa acessar o conteúdo original da informação.

---

## 🧠 O que é Criptografia Assimétrica?

A criptografia assimétrica é um método de segurança digital baseado em um **par de chaves**:

- 🔓 **Chave pública** – usada para **cifrar** (criptografar) mensagens.  
- 🔐 **Chave privada** – usada para **decifrar** (descriptografar) mensagens.

Esse modelo assegura que apenas quem possui a chave privada possa acessar a informação cifrada, mesmo que ela tenha sido transmitida por canais inseguros.

### 🔍 Aplicações reais:
- Proteção de dados em conexões seguras (HTTPS)
- Assinaturas digitais
- Sistemas de autenticação
- Blockchain e carteiras de criptomoedas

---

## 💻 Como funciona o programa?

O algoritmo RSA foi implementado com a biblioteca `cryptography` em Python. Ao executar o programa, o usuário digita a mensagem desejada diretamente no terminal.

Em seguida, o sistema realiza as seguintes etapas:

1. Geração do par de chaves (pública e privada)  
2. Cifração da mensagem com a chave pública  
3. Decifração da mensagem com a chave privada  
4. Exibição da mensagem original, cifrada (em bytes) e decifrada

---

## 📥 Entrada do Usuário

O programa solicita que o usuário digite uma mensagem.  
Essa mensagem será protegida via RSA e só poderá ser lida após o processo de decifragem com a chave correta.

---

## 📸 Print da Execução

![Execução do Programa](https://github.com/user-attachments/assets/d7371740-f3aa-4e7c-8a7e-cb209ae05bcb)

---

## 👩‍💻 Autora

**Ana Paula Santos de Freitas**  
Estudante de Análise e Desenvolvimento de Sistemas  
📍 Instituto Federal do Triângulo Mineiro (IFTM) – Campus Patrocínio




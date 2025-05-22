
# 🔐 Criptografia Assimétrica com RSA em Python

Este projeto apresenta uma implementação simples e funcional da **criptografia assimétrica** utilizando o algoritmo **RSA (Rivest–Shamir–Adleman)** em Python.  
A criptografia assimétrica é amplamente usada para garantir a **confidencialidade e integridade dos dados**, utilizando um par de chaves: uma **pública** e uma **privada**.

---

## 🧠 Sobre o funcionamento

O sistema implementa as operações básicas do algoritmo RSA:

- **Geração automática de chaves**: ao iniciar o programa, é gerado um par de chaves (pública e privada).
- **Ciframento de mensagens**: o usuário digita um texto, que é convertido para bytes e cifrado com a chave pública.
- **Decifragem de mensagens**: o sistema utiliza a chave privada para recuperar a mensagem original.

> As mensagens não são armazenadas em arquivos. Todo o processo ocorre em **memória** e é realizado diretamente pelo terminal.

---

## ⚙️ Funcionalidades

- Geração automática do par de chaves RSA ao iniciar o programa
- Ciframento de mensagens fornecidas pelo usuário
- Decifragem da última mensagem cifrada
- Menu interativo com opções claras e didáticas

---

## 📋 Estrutura do menu

Ao executar o programa, o usuário verá:

```
=== MENU - CRIPTOGRAFIA RSA ===
1 - Cifrar mensagem
2 - Decifrar mensagem
3 - Sair
```

- **Opção 1**: solicita que o usuário digite um texto, que será cifrado usando RSA.
- **Opção 2**: decifra a última mensagem cifrada.
- **Opção 3**: encerra o programa.

---

## 💻 Exemplo de uso

```
Par de chaves RSA gerado com sucesso.

=== MENU - CRIPTOGRAFIA RSA ===
1 - Cifrar mensagem
2 - Decifrar mensagem
3 - Sair
Escolha uma opção: 1
Digite a mensagem a ser cifrada: Teste de criptografia
Mensagem cifrada com sucesso.

=== MENU - CRIPTOGRAFIA RSA ===
Escolha uma opção: 2
Mensagem decifrada:
Teste de criptografia
```

---

## 👩‍💻 Autora

**Ana Paula Santos de Freitas**  
Estudante de Análise e Desenvolvimento de Sistemas  
📍 Instituto Federal do Triângulo Mineiro (IFTM) – Campus Patrocínio

---

Este projeto foi desenvolvido como parte da disciplina de **Segurança da Informação**, com o objetivo de demonstrar o funcionamento da criptografia assimétrica utilizando o algoritmo **RSA**.




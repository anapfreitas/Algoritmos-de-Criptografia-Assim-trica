from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class SistemaCriptografiaRSA:
    def __init__(self):
        self.chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.chave_publica = self.chave_privada.public_key()
        self.mensagem_cifrada = None
        print("Par de chaves RSA gerado com sucesso.")

    def cifrar_mensagem(self, texto):
        if not texto.strip():
            print("A mensagem não pode estar vazia.")
            return
        mensagem_em_bytes = texto.encode("utf-8")
        self.mensagem_cifrada = self.chave_publica.encrypt(
            mensagem_em_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Mensagem cifrada com sucesso.")

    def decifrar_mensagem(self):
        if not self.mensagem_cifrada:
            print("Nenhuma mensagem cifrada foi encontrada.")
            return
        mensagem_decifrada = self.chave_privada.decrypt(
            self.mensagem_cifrada,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Mensagem decifrada:")
        print(mensagem_decifrada.decode("utf-8"))

    def exibir_menu(self):
        while True:
            print("\n=== MENU - CRIPTOGRAFIA RSA ===")
            print("1 - Cifrar mensagem")
            print("2 - Decifrar mensagem")
            print("3 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                texto = input("Digite a mensagem a ser cifrada: ")
                self.cifrar_mensagem(texto)
            elif opcao == "2":
                self.decifrar_mensagem()
            elif opcao == "3":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaCriptografiaRSA()
    sistema.exibir_menu()

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def gerar_chaves():
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

def cifrar(mensagem: str, chave_publica):
    mensagem_bytes = mensagem.encode()
    mensagem_cifrada = chave_publica.encrypt(
        mensagem_bytes,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return mensagem_cifrada

def decifrar(mensagem_cifrada: bytes, chave_privada):
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return mensagem_decifrada.decode()

if __name__ == "__main__":
    priv, pub = gerar_chaves()
    mensagem = "Segredo da Ana Paula"
    cifrada = cifrar(mensagem, pub)
    decifrada = decifrar(cifrada, priv)

    print("Mensagem original:", mensagem)
    print("Mensagem cifrada (em bytes):", cifrada)
    print("Mensagem decifrada:", decifrada)

import hashlib


def gerar_hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

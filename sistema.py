from usuario import Usuario
import bcrypt

class Sistema:
    def __init__(self):
        self.usuarios = []
    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None
    
    def excluir_usuario(self, email):
        usuario = self.buscar_usuario(email)
        if usuario is not None:
            self.usuarios.remove(usuario)
            return True
        return False
    
    def atualizar_telefone(self, email, novo_telefone):
        usuario = self.buscar_usuario(email)
        if novo_telefone.strip() == "":
            return False
        if not novo_telefone.isdigit():
            return False
        if len(novo_telefone) != 11:
            return False
        if len(set(novo_telefone)) == 1:
            return False
        ddds_validos = [ "11", "12", "13", "14", "15", "16", "17", "18", "19","21", "22", "24", "27", "28","31", "32", "33", "34", "35", "37", "38","41", "42", "43", "44", "45", "46", "47", "48", "49","51", "53", "54", "55","61", "62", "63", "64", "65", "66", "67", "68", "69","71", "73", "74", "75", "77", "79","81", "82", "83", "84", "85", "86", "87", "88", "89","91", "92", "93", "94", "95", "96", "97", "98", "99"]
        ddd = novo_telefone[:2]
        if ddd not in ddds_validos:
            return False
        if usuario is None:
            return False
        if novo_telefone == usuario.telefone:
            return False
        for outro_usuario in self.usuarios:
            if outro_usuario is not usuario:
                if outro_usuario.telefone == novo_telefone:
                    return False
        usuario.telefone = novo_telefone
        return True

    def atualizar_nome(self, email, novo_nome):
        usuario = self.buscar_usuario(email)
        if usuario is None:
            return False
        if novo_nome.strip() == "":
            return False
        if novo_nome == usuario.nome:
            return False
        usuario.nome = novo_nome
        return True
        return False

    def atualizar_senha(self, email, senha_atual, nova_senha, confirma_senha):
        usuario = self.buscar_usuario(email)
        if usuario is None:
            return False
        if not bcrypt.checkpw(senha_atual.encode("utf-8"),usuario.senha.encode("utf-8")):
            return False
        if bcrypt.checkpw(nova_senha.encode("utf-8"),usuario.senha.encode("utf-8")):
            return False
        if nova_senha != confirma_senha:
            return False
        hash_nova_senha = bcrypt.hashpw(nova_senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        usuario.senha = hash_nova_senha
        return True

    def cadastrar_usuario(self, nome, email, telefone, senha):
        if email.count("@") != 1:
            return False
        usuario_email = email.split("@")[0]
        if ".." in usuario_email:
            return False
        if usuario_email.startswith("."):
            return False
        if usuario_email.endswith("."):
            return False
        dominio = email.split("@")[1]
        if "." not in dominio:
            return False
        if email.endswith("."):
            return False
        if dominio.startswith("."):
            return False
        if ".." in dominio:
            return False
        if " " in email:
            return False
        if email.startswith("@"):
            return False
        if email.endswith("@"):
            return False
        if "@" not in email:
            return False
        if senha.strip() == "":
            return False
        if len(senha) < 8:
            return False
        if not any(letra.isalpha() for letra in senha):
            return False
        if not any(caractere.isdigit() for caractere in senha ):
            return False
        if any(caractere.isspace() for caractere in senha):
            return False
        if not any(letra.isupper() for letra in senha):
            return False
        if not any(letra.islower() for letra in senha):
            return False
        if telefone.strip() == "":
            return False
        if email.strip() == "":
            return False
        if nome.strip() == "":
            return False
        if self.buscar_usuario(email) is not None:
            return False
        for usuario in self.usuarios:
            if usuario.telefone == telefone:
                return False
        if not telefone.isdigit():
            return False
        if len(telefone) != 11:
            return False
        ddds_validos = [ "11", "12", "13", "14", "15", "16", "17", "18", "19","21", "22", "24", "27", "28","31", "32", "33", "34", "35", "37", "38","41", "42", "43", "44", "45", "46", "47", "48", "49","51", "53", "54", "55","61", "62", "63", "64", "65", "66", "67", "68", "69","71", "73", "74", "75", "77", "79","81", "82", "83", "84", "85", "86", "87", "88", "89","91", "92", "93", "94", "95", "96", "97", "98", "99"]
        ddd = telefone[:2]
        if ddd not in ddds_validos:
         return False
        if telefone[2] != "9":
            return False
        hash_senha = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        novo_usuario = Usuario(nome, email, telefone, hash_senha)
        self.usuarios.append(novo_usuario)
        return novo_usuario 

    def fazer_login(self, email, senha):
        usuario = self.buscar_usuario(email)
        if usuario is None:
            return False
        if not bcrypt.checkpw(senha.encode("utf-8"),usuario.senha.encode("utf-8")):
            return False
        return True
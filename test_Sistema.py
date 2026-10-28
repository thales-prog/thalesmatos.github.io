import unittest
import bcrypt
from sistema import Sistema
class TestSistema(unittest.TestCase):
    def test_cadastro(self):
        sistema = Sistema()

        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

        self.assertEqual(len(sistema.usuarios), 1)

        self.assertEqual(sistema.usuarios[0].nome, "joão")

        self.assertEqual(sistema.usuarios[0].email, "joao@gmail.com")

    def test_dois_usuarios(self):
        sistema = Sistema()

        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

        sistema.cadastrar_usuario("maria", "maria@gmail.com", "11988888888", "Python456")

        self.assertEqual(len(sistema.usuarios), 2)

    def test_buscar_usuario(self):
            sistema = Sistema()

            sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
            
            sistema.cadastrar_usuario("maria", "maria@gmail.com", "11988888888", "Python456")

            usuario_encontrado = sistema.buscar_usuario("joao@gmail.com")
            self.assertIsNotNone(usuario_encontrado)
            self.assertEqual(usuario_encontrado.nome, "joão")

    def test_buscar_usuario_inexistente(self):
            sistema = Sistema()

            resultado = sistema.buscar_usuario("pedro@gmail.com")
            self.assertIsNone(resultado)

    def test_excluir_usuario(self):
              sistema = Sistema()
              sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
              sistema.cadastrar_usuario("maria", "maria@gmail.com", "11988888888", "Python456")

              resultado = sistema.excluir_usuario("joao@gmail.com")
              self.assertTrue(resultado)
              self.assertEqual(len(sistema.usuarios), 1)
              self.assertEqual(sistema.usuarios[0].nome, "maria")

    def test_excluir_usuario_inexistente(self):
                sistema = Sistema()
                sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
                resultado = sistema.excluir_usuario("pedro@gmail.com")

    def test_atualizar_telefone(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_telefone("joao@gmail.com", "11888888888")
        self.assertTrue(resultado)
        self.assertEqual(sistema.usuarios[0].telefone, "11888888888")

    def test_atualizar_telefone_inexistente(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_telefone("pedro@gmail.com", "11888888888")
        self.assertFalse(resultado)
        self.assertEqual(sistema.usuarios[0].telefone, "11999999999")

    def test_atualizar_nome(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_nome("joao@gmail.com", "pedro")
        self.assertTrue(resultado)
        self.assertEqual(sistema.usuarios[0].nome, "pedro")

    def test_atualizar_nome_inexistente(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_nome("pedro@gmail.com", "Pedro Costa")
        self.assertFalse(resultado)
        self.assertEqual(sistema.usuarios[0].nome, "joão")

    def test_atualizar_senha(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_senha("joao@gmail.com", "Python123", "Novasenha456", "Novasenha456")
        self.assertTrue(resultado)
        self.assertTrue(bcrypt.checkpw("Novasenha456".encode("utf-8"),sistema.usuarios[0].senha.encode("utf-8")))

    def test_senha_atual_incorreta(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_senha("joao@gmail.com", "Python", "Novasenha456", "Novasenha456")
        self.assertFalse(resultado)
        self.assertTrue(bcrypt.checkpw("Python123".encode("utf-8"),sistema.usuarios[0].senha.encode("utf-8")))

    def test_senha_igual_antiga(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_senha("joao@gmail.com", "Python123", "Python123", "Python123")
        self.assertFalse(resultado)
        self.assertTrue(bcrypt.checkpw("Python123".encode("utf-8"),sistema.usuarios[0].senha.encode("utf-8")))

    def test_confirmacao_senha_incorreta(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_senha("joao@gmail.com", "Python123", "Novasenha456", "Outranovasenha789")
        self.assertFalse(resultado)
        self.assertTrue(bcrypt.checkpw("Python123".encode("utf-8"),sistema.usuarios[0].senha.encode("utf-8")))

    def test_atualizar_senha_usuario_inexistente(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        resultado = sistema.atualizar_senha("pedro@gmail.com", "Python123", "Novasenha456", "Novasenha456")
        self.assertFalse(resultado)
        self.assertTrue(bcrypt.checkpw("Python123".encode("utf-8"),sistema.usuarios[0].senha.encode("utf-8")))

    def test_email_duplicado(self):
        sistema = Sistema()
        sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")
        sistema.cadastrar_usuario("pedro","joao@gmail.com", "11888888888", "Novasenha456")
        self.assertEqual(len(sistema.usuarios), 1)
        self.assertEqual(sistema.usuarios[0].nome, "joão")

    def test_cadastro_nome_vazio(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("", "joao@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_vazio(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_telefone_vazio(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_vazia(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_sem_arroba(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joaogmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_sem_dominio(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_sem_usuario(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_dois_arrobas(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_sem_ponto_dominio(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_dominio_termina_ponto(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_dominio_comeca_ponto(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_com_espacos(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao silva@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_dois_pontos(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail..com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_usuario_dois_pontos(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao..silva@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_usuario_comeca_ponto(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", ".joao@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_email_usuario_termina_ponto(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao.@gmail.com", "11999999999", "Python123")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_curta(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python1")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_sem_letras(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "12345678")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_sem_numeros(self):
        sistema = Sistema()
        resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "abcdefgh")
        self.assertFalse(resultado)
        self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_com_espaco(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joão@gmail.com", "11999999999", "python 123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_com_tabulacao(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "python\t123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_com_caractere_especial(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python@123")
         self.assertTrue(resultado)
         self.assertEqual(len(sistema.usuarios), 1)

    def test_cadastro_senha_sem_maiuscula(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_senha_sem_minuscula(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "PYTHON123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_telefone_com_letras(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "1199999abcd", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_telefone_com_10_digitos(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "1198765432", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_ddd_00(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "00987654321", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_ddd_01(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "01987654321", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_ddd_20(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "20987654321", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)


    def test_cadastro_celular_sem_nove(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11876543210", "Python123")
         self.assertFalse(resultado)
         self.assertEqual(len(sistema.usuarios), 0)

    def test_cadastro_telefone_duplicado(self):
          sistema = Sistema()
          resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

          resultado = sistema.cadastrar_usuario("maria", "maria@gmail.com", "11999999999", "Python456")
          self.assertFalse(resultado)
          self.assertEqual(len(sistema.usuarios), 1)

    def test_atualizar_telefone_duplicado(self):
         sistema = Sistema()
         resultado = sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

         resultado = sistema.cadastrar_usuario("maria", "maria@gmail.com", "11988888888", "Python456")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "11988888888")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11999999999")

    def test_atualizar_telefone_vazio(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11999999999")

    def test_atualizar_telefone_com_letras(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "119ABC45678")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11999999999")

    def test_atualizar_telefone_curto(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "1198765432")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com" ).telefone, "11999999999")

    def test_atualizar_telefone_ddd_invalidado(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11999999999", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "20987654321")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11999999999")

    def test_atualizar_telefone_digitos_iguais(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "11111111111")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11987654321")

    def test_atualizar_telefone_igual_atual(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.atualizar_telefone("joao@gmail.com", "11987654321",)
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").telefone, "11987654321")

    def test_atualizar_nome_vazio(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.atualizar_nome("joao@gmail.com", "    ")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").nome, "joão")

    def test_atualizar_nome_igual_atual(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.atualizar_nome("joao@gmail.com", "joão")
         self.assertFalse(resultado)
         self.assertEqual(sistema.buscar_usuario("joao@gmail.com").nome, "joão")

    def test_login_email_inexistente(self):
         sistema = Sistema()
         resultado = sistema.fazer_login("naoexiste@gmail.com", "Python123")
         self.assertFalse(resultado)

    def test_login_senha_incorreta(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.fazer_login("joao@gmail.com", "SenhaErrada456")
         self.assertFalse(resultado)

    def test_login_sucesso(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.fazer_login("joao@gmail.com", "Python123")
         self.assertTrue(resultado)

    def test_login_apos_atualizar_senha(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")
         sistema.atualizar_senha("joao@gmail.com", "Python123", "Novasenha456", "Novasenha456")
         login_antigo = sistema.fazer_login("joao@gmail.com", "Python123")
         login_novo = sistema.fazer_login("joao@gmail.com", "Novasenha456")

         self.assertFalse(login_antigo)
         self.assertTrue(login_novo)

    def test_login_usuario_excluido(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")
         sistema.excluir_usuario("joao@gmail.com")

         resultado = sistema.fazer_login("joao@gmail.com", "Python123")
         self.assertFalse(resultado)

    def test_login_senha_vazia(self):
         sistema = Sistema()
         sistema.cadastrar_usuario("joão", "joao@gmail.com", "11987654321", "Python123")

         resultado = sistema.fazer_login("joao@gmail.com", "")
         self.assertFalse(resultado)
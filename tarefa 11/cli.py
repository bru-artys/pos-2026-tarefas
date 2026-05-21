import users_wrapper as u
 
 
class UserMenu:
 
    def __init__(self):
        self.opcoes = {
            "1": self._listar,
            "2": self._detalhar,
            "3": self._criar,
            "4": self._atualizar,
            "5": self._deletar,
            "0": self._sair,
        }
        self._rodando = True
 
    def executar(self):
        while self._rodando:
            print("\n[1] Listar  [2] Detalhar  [3] Criar  [4] Atualizar  [5] Deletar  [0] Sair")
            acao = self.opcoes.get(input("Opção: ").strip())
            acao() if acao else print("Opção inválida!")
 
    def _listar(self):
        for user in u.list():
            print(f"{user['id']} - {user['name']}")
 
    def _detalhar(self):
        user = u.read(input("ID: "))
        print(user) if user else print("Não encontrado.")
 
    def _criar(self):
        print("Criado!" if u.create(self._coletar_dados()) else "Erro.")
 
    def _atualizar(self):
        user_id = input("ID: ")
        print("Atualizado!" if u.update(user_id, self._coletar_dados()) else "Erro.")
 
    def _deletar(self):
        print("Deletado!" if u.delete(input("ID: ")) else "Erro.")
 
    def _sair(self):
        self._rodando = False
 
    @staticmethod
    def _coletar_dados():
        return {
            "name":     input("Nome: "),
            "username": input("Username: "),
            "email":    input("Email: "),
            "phone":    input("Telefone: "),
            "website":  input("Website: "),
        }
 
 
UserMenu().executar()
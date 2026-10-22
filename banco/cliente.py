class cliente:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.contas = []

    def adicionarConta(self,conta):
        if conta not in self.contas:
            self.contas.append(conta)
            return True
        return False

def cadastrarCliente():
    while True:
        

        nome = input("informe seu nome completo: ").strip()
        cpf = input("informe o seu cpf")
        cpf = cpf.replace("-","")
        cpf = cpf.replace(".","")
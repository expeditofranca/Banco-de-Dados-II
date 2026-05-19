from pymongo import MongoClient


# =====================================
# CONEXÃO COM O MONGODB
# =====================================

client = MongoClient(
    "mongodb://usuario_proj:senha123@localhost:27017/AtividadesProj"
)

db = client["AtividadesProj"]

projetos = db["projetos"]
atividades = db["atividades"]


# =====================================
# CREATE
# Inserir nova atividade
# =====================================

def inserir_atividade():

    nova_atividade = {
        "projeto": "Sistema Financeiro",
        "descricao": "Implementar autenticação JWT",
        "responsavel": "Carlos Silva",
        "status": "Pendente"
    }

    atividades.insert_one(nova_atividade)

    print("Atividade inserida com sucesso!\n")


# =====================================
# READ
# Listar projetos e atividades
# =====================================

def listar_projetos_atividades():

    lista_projetos = projetos.find()

    for projeto in lista_projetos:

        print(f"\nProjeto: {projeto['nome']}")
        print(f"Líder: {projeto['lider']}")
        print(f"Status: {projeto['status']}")

        lista_atividades = atividades.find(
            {"projeto": projeto["nome"]}
        )

        print("Atividades:")

        for atividade in lista_atividades:
            print(
                f" - {atividade['descricao']} "
                f"({atividade['status']})"
            )


# =====================================
# UPDATE
# Atualizar líder do projeto
# =====================================

def atualizar_lider():

    projetos.update_one(
        {"nome": "Portal Web"},
        {
            "$set": {
                "lider": "Carlos Silva"
            }
        }
    )

    print("\nLíder atualizado com sucesso!\n")


# =====================================
# DELETE
# Remover atividade
# =====================================

def remover_atividade():

    atividades.delete_one(
        {"descricao": "Modelar banco de dados"}
    )

    print("Atividade removida com sucesso!\n")


# =====================================
# EXECUÇÃO
# =====================================

if __name__ == "__main__":

    inserir_atividade()

    listar_projetos_atividades()

    atualizar_lider()

    remover_atividade()
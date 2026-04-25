# --- Exercício 4 ---
usuarios = {"admin": "1234", "aluno_python": "py99"}
login = input("User: ")
if login in usuarios:
    senha = input("Senha: ")
    if senha == usuarios[login]:
        print("Acesso Permitido!")
    else:
        print("Senha Incorreta.")
else:
    print("Usuário não encontrado.")
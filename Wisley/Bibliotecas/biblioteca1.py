# from platform import python_version

# print("Versão: ", python_version())
import faker as fk

falso_dado = fk.Faker("pt_BR")
nome = falso_dado.name()
fk.Faker.seed()
for i in range(10):
    
    print(f"{falso_dado.name()} \nTelefone: {falso_dado.phone_number()}\nEmail: {falso_dado.email()}")

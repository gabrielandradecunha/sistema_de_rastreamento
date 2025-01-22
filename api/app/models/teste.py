from models.User import User

# criando tabela
#User.create()

# inserindo usuario de .longi
# User.createuser("Gabriel", "gandradecortez50@gmail.com", "teste",-15.593054444600057, -56.099054721903784)

# puxando usuario de teste
teste = User.getuser("gandradecortez50@gmail.com", "teste")

print(type(teste))
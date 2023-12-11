import shutil
import os

#adicionar o diretório
#tudo que estiver dentro do diretório será copiado para o destino
path = "/workspaces/api-bolsa/data/moeda/"
dest = "/workspaces/api-bolsa/database/archiving/"

lista = os.listdir(path)

for file in lista:
    caminho_completo_origem = os.path.join(path, file)
    caminho_completo_destino = os.path.join(dest, file)
    shutil.copyfile(caminho_completo_origem, caminho_completo_destino)
    print(f"{file} copiado para {dest}")







# path = "/workspaces/api-bolsa/data/acoes/"
# dest = "/workspaces/api-bolsa/database/archiving/"

# lista = os.listdir(path)

# for file in lista:
#     cop_path = shutil.copyfile(file, dest)
#     print(cop_path)
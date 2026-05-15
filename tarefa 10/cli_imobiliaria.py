import json
 
with open("biblioteca.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
 
livros = dados["biblioteca"]["livros"]
 
for i, livro in enumerate(livros, start=1):
    print(f"{i} - {livro['descricao']}")
 
id_lido = int(input("\ndigite o ID do livro para ver mais detalhes: "))
livro = livros[id_lido - 1]
 
print("\n- detalhes do livro\n")
print("descrição:", livro["descricao"])
print("preço: R$", livro["preco"])
 
loc = livro["localizacao"]
print("\nlocalização:")
print(" corredor:", loc["corredor"])
print(" prateleira:", loc["prateleira"])
print(" seção:", loc["secao"])
print(" andar:", loc["andar"])
 
aut = livro["autor"]
print("\nautor:")
print(" nome:", aut["nome"])
print(" email:", aut["email"])
print(" telefones:")
for tel in aut["telefones"]:
    print("  -", tel)
 
det = livro["detalhes"]
print("\ndetalhes:")
print(" páginas:", det["paginas"])
print(" edição:", det["numEdicao"])
print(" exemplares disponíveis:", det["numExemplares"])
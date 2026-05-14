from xml.dom.minidom import parse

dom = parse("cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

id_prato = 0
for prato in pratos:
    id_prato += 1
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f'{id_prato} - {nome}')

id_lido = int(input("Digite o id do prato para saber mais: "))

if 0 < id_lido <= len(pratos):
    prato = pratos[id_lido-1]

    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    
    ingredientes_tags = prato.getElementsByTagName('ingrediente')
    lista_ingredientes = [ing.firstChild.nodeValue for ing in ingredientes_tags]

    print("nome:", nome)
    print("descrição:", descricao)
    print("ingredientes:", ", ".join(lista_ingredientes))
    print("preço:", preco)
    print("calorias:", calorias)

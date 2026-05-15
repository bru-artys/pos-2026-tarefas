from xml.dom.minidom import parse
import json
 
def get_text(parent, tag):
    elems = parent.getElementsByTagName(tag)
    if elems and elems[0].firstChild:
        return elems[0].firstChild.nodeValue.strip()
    return None
 
dom = parse('biblioteca.xml')
biblioteca = dom.documentElement
livros = biblioteca.getElementsByTagName('livro')
 
lista = []
 
for livro in livros:
    descricao = get_text(livro, "descricao")
 
    localizacao_tag = livro.getElementsByTagName("localizacao")[0]
    corredor = get_text(localizacao_tag, "corredor")
    prateleira = get_text(localizacao_tag, "prateleira")
    secao = get_text(localizacao_tag, "secao")
    andar = get_text(localizacao_tag, "andar")
 
    autor_tag = livro.getElementsByTagName("autor")[0]
    nome = get_text(autor_tag, "nome")
    email = get_text(autor_tag, "email")
    telefones_tags = autor_tag.getElementsByTagName("telefone")
    telefones = []
    for tel in telefones_tags:
        if tel.firstChild:
            telefones.append(tel.firstChild.nodeValue.strip())
 
    detalhes_tag = livro.getElementsByTagName("detalhes")[0]
    paginas = get_text(detalhes_tag, "paginas")
    numEdicao = get_text(detalhes_tag, "numEdicao")
    numExemplares = get_text(detalhes_tag, "numExemplares")
 
    preco = get_text(livro, "preco")
 
    lista.append({
        "descricao": descricao,
        "localizacao": {
            "corredor": corredor,
            "prateleira": prateleira,
            "secao": secao,
            "andar": andar
        },
        "autor": {
            "nome": nome,
            "email": email,
            "telefones": telefones
        },
        "detalhes": {
            "paginas": paginas,
            "numEdicao": numEdicao,
            "numExemplares": numExemplares
        },
        "preco": preco
    })
 
dados = {
    "biblioteca": {
        "livros": lista
    }
}
 
with open('biblioteca.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f)
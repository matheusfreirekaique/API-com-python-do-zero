# Api - é um lugar para disponibilizar recursos e/ou funcionalidades 
# 1. objetivo - ciar um api que disponibiliza a consulta, criação, edição, e exclusão 
# 2. URL Base 
# 3. Endpoint-
          # - localhost/livros (GET)
          # - localhost/livros/id (GET)
          # - localhost/livros/id (PUT)
          # - localhost/livros/id (DELETE)
# 4. Quais recursos 

from flask import Flask, jsonify, request

app = Flask(__name__)

livros =[
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - ASociedade do anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra filosofal',
        'autor': 'J.K Howling'  
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábotos Atômicos'
    }
]

# consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)

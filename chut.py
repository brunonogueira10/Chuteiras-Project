from flask import Flask, jsonify, request

app = Flask(__name__)

Chuteiras = [
    {
        'id': 1,
        'chuteira': 'Nike Mercurial Vapor',
        'fabricante': 'Nike'
    },
    {
        'id': 2,
        'chuteira': 'Adidas Predator',
        'fabricante': 'Adidas'
    },
    {
        'id': 3,
        'chuteira': 'Puma KING',
        'fabricante': 'Puma'
    },
    {
        'id': 4,
        'chuteira': 'Puma Evospeed',
        'fabricante':'Puma'
    }
]


# Consultar(todos)

@app.route('/Chuteiras',methods=['GET'])
def obter_chuteiras():
    return jsonify(Chuteiras)


# Consultar(id)

@app.route('/Chuteiras/<int:id>',methods=['GET'])
def obter_chuteira_por_id(id):
    for chuteira in Chuteiras:
        if chuteira.get('id') == id:
            return jsonify(chuteira)

#  Editar

@app.route('/Chuteiras<int:id>',methods=['PUT'])
def editar_chuteira_por_id(id):
   chuteira_alterado = request.get_json()
   for indice,chuteira in enumerate(Chuteiras):
       if chuteira.get('id') == id:
           Chuteiras[indice].update(chuteira_alterado)
           return jsonify(Chuteiras[indice])

# Criar

@app.route('/Chuteiras',methods=['POST'])
def incluir_novo_chuteira():         
    novo_chuteira = request.get_json()
    Chuteiras.append(novo_chuteira)

    return jsonify(Chuteiras)

# Excluir

@app.route('/Chuteiras/<int:id>',methods=['DELETE'])
def excluir_chuteira(id):
    for indice, chuteira in enumerate(Chuteiras):
        if chuteira.get('id') == id:
            del Chuteiras[indice]
    
    return jsonify(Chuteiras)    
   
app.run(port=5000, host='localhost', debug=True)
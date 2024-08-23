from flask import Flask, jsonify, make_response, request

#database
from bd import Cidades

#modulo flask
app = Flask("Cidades")

#Método GET = Visualizar Cidades
@app.route("/Cidades", methods = ['GET'])
def Visualizar_cidades():
    return Cidades

#Método POST = Criar Cidade
@app.route("/Cidades", methods = ['POST'])
def Criar_cidades():
    nova_cidade = request.json
    Cidades.append(nova_cidade)
    return make_response(
        jsonify("Cidade criada com sucesso.")
    )

#Método PUT = Editar dados da Cidade
@app.route("/Cidades/<int:id>", methods = ['PUT'])
def Editar_cidades(id):
    cidade_editada = request.get_json()
    
    for indice, cidade in enumerate(Cidades):
        if cidade.get("id") == id:
            Cidades[indice].update(cidade_editada)
            return make_response(
                jsonify("Cidade atualizada com sucesso.", Cidades[indice])
            )
        
#Método DELETE = Excluir Cidades
@app.route("/Cidades/<int:id>", methods = ['DELETE'])
def Excluir_cidades(id):
    for indice, cidade in enumerate(Cidades):
        if cidade.get("id") == id:
            del Cidades[indice]
            return jsonify({"Mensagem":"Cidade excluída com sucesso."})
        
#Execução do programa
app.run(port= 5000, host='localhost')
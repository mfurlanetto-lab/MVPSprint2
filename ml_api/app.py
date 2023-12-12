from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib

from schemas import *

from model.empregado import Empregado

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)          # modo de depuração

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
empregado_tag = Tag(
    name="Empregado", description="Predição se empregado deixará ou não o emprego")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de previsão por machine learning
@app.post('/prever', tags=[empregado_tag],
          responses={"200": ResultadoSchema, "400": ErrorSchema, "404": ErrorSchema, "500": ErrorSchema})
def prever(form: EmpregadoSchema):
    """Dadas as informações fornecidas pelo RH sobre um empregado, o sistema prevê se o empregado deixará o emprego conforme o modelo ML treinado
    Retorna uma previsão se o empregado deixará o emprego ou não.

    Entrada:
            education: Grau acadêmico - (1) Bacharelado; (2) Mestrado; (3) PhD
            joiningYear: Ano de admissão - Formato AAAA
            paymentTier: Nível salarial - 1,  2 ou 3
            age: Idade
            gender: Gênero - (1) Masculino; (2) Feminino
            everBenched: Já esteve sem alocação no trabalho - (1) Sim; (0) Não
            experienceInCurrentDomain: Experiência na função atual - 0, 1, 2, 3, 4, 5, 6 ou 7

    Saída:
            leaveOrNot: Se deixará o emprego - (1) Sim; (0) Não
    """

    try:
        # Obtém os dados do formulário
        empregado = Empregado(int(request.form.get('education')),
                              int(request.form.get('joiningYear')),
                              int(request.form.get('paymentTier')),
                              int(request.form.get('age')),
                              int(request.form.get('gender')),
                              int(request.form.get('everBenched')),
                              int(request.form.get('experienceInCurrentDomain')))

        # Valida dados do formulário
        try:
            empregado.validar_dados()

        except ValueError as e:
            print(f"Erro: {e}")
            erro_msg = str(e)
            return {"message": erro_msg}, 400

        print('Carregando o modelo treinado...')
        # Carrega o modelo treinado
        nome_arquivo = 'ml_modelo\modelo_treinadoSVM.joblib'
        modelo_carregado = joblib.load(nome_arquivo)

        print('Fazendo a predição...')
        dados_predicao = [[
            form.education,
            form.joiningYear,
            form.paymentTier,
            form.age,
            form.gender,
            form.everBenched,
            form.experienceInCurrentDomain
        ]]

        # Faz a predição usando o modelo carregado
        resultado = modelo_carregado.predict(dados_predicao).item()
        print('Resultado: ', resultado)
        return {"resultado": resultado}, 200

    except FileNotFoundError:
        print('FileNotFoundError')
        erro_msg = 'Predição não realizada! Arquivo do modelo não encontrado. '
        return {"message": erro_msg}, 404

    except Exception as e:
        print('Exception', str(e))
        erro_msg = 'Predição não realizada! Descrição: ' + str(e)
        return {"message": erro_msg}, 500


if __name__ == '__main__':
    app.run(debug=True)

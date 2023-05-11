import os
import json
from banner import banner_project
try:
    from flask import Flask, jsonify, request

except ModuleNotFoundError:
    os.system('pip install flask')
    os.system('python.exe -m pip install --upgrade pip')

try:
    from flask_cors import CORS, cross_origin

except ModuleNotFoundError:
    os.system('pip install -U flask-cors')

finally:
    app = Flask(__name__)
    
    CORS(app, resources={r"http://localhost:5000/api/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    # PEGANDO INGREDIENTES DO DOCUMENTO JSON
    data = json.load(open('../db/db.json', encoding="utf-8"))

    # http://localhost:5000/api//ingredientes
    @app.route('/api/ingredientes', methods=['GET'])
    def get_ingredientes():
        """
            FUNÇÃO PARA CHAMAR A API.

            ...

            RETURN
            ----------
            status : str
            data : dic{}
        """

        response = jsonify(
            {
                'status': "200_OK",
                'data': data
            }
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # http://localhost:5000/api/burgers
    @app.route('/api/burgers', methods=['POST'])
    @cross_origin(allow_headers=['Content-Type'])
    def create_burger():
        """
            CRIAR UM NOVO PEDIDO PARA HAMBURGUER.

            ...

            VARIABLES
            ----------
            novo_pedido : dic{}
                    o novo pedido do cliente em json.

            RETURN
            ----------
            status : str
            data : dic{}
        """

        novo_pedido = request.get_json()

        data['burgers'].append(novo_pedido)

        response = jsonify(
            {
                'status': "200_OK",
                'data': novo_pedido
            }
        )

        return response

    if __name__ == '__main__':
        banner_project()
        app.run(port=5000, host='localhost', debug=True)
import os
import json
from banner import banner_project
try:
    from flask import Flask, jsonify, request

except ModuleNotFoundError:
    os.system('pip install flask')
    os.system('python.exe -m pip install --upgrade pip')

try:
    from flask_cors import CORS

except ModuleNotFoundError:
    os.system('pip install -U flask-cors')

finally:
    app = Flask(__name__)
    
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # PEGANDO INGREDIENTES DO DOCUMENTO JSON
    data = json.load(open('../db/db.json'))

    # http://localhost:5000
    @app.route('/ingredientes', methods=['GET'])
    def get_ingredientes():
        """
            FUNÇÃO PARA CHAMAR A API.

            ...

            RETURN
            ----------
            message : str
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

    if __name__ == '__main__':
        banner_project()
        app.run(port=5000, host='localhost', debug=True)
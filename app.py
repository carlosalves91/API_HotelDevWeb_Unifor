from flask import Flask

app = Flask(__name__)

# GET > método para captura dos dados
@app.route('/API_HotelDevWeb_Unifor', methods=['GET']) 
def get():
    
    return "Reserva do seu quarto confirmada!"

# POST > Inserção de dados pela API
@app.route('/API_HotelDevWeb_Unifor', methods=['POST']) 
def post():
    return "Reserva efetuada com sucesso!"

# PUT > Método de edição de dados
@app.route('/API_HotelDevWeb_Unifor', methods=['PUT']) 
def put():
    return "As alterações da sua reserva foram efetuadas."

# DELETE > Deletando dados
@app.route('/API_HotelDevWeb_Unifor', methods=['DELETE']) 
def delete():
    return "O cancelamento da sua reserva foi efetuadocom sucesso."

app.run()
from flask import Flask, jsonify
from teste_condoconta.controller.contaController import ContaController

app = Flask(__name__)

contaController = ContaController()

@app.route("/saldo/<conta>")
def consultar_saldo(conta):
    return jsonify(contaController.consultar_saldo(conta))

@app.route("/extrato/<conta>")
def consultar_extrato(conta):
    return jsonify(contaController.consultar_extrato(conta))

@app.route("/transferencia", methods=["POST"])
def realizar_transferencia():
    return jsonify(contaController.realizar_transferencia())

if __name__ == "__main__":
    app.run()

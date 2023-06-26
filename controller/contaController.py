from service.contaService import ContaService
from flask import Flask, jsonify
from datetime import date
import requests, json

class ContaController:

    def __init__(self):
        self.contaService = ContaService()

    def consultar_saldo(self, conta):
        try:
            saldo = self.contaService.consultar_saldo(conta)
            return {"saldo": saldo}
        except ValueError as e:
            return {"error": str(e)}, 400

    def consultar_extrato(self, tipo_conta):
        data_atual = date.today()
        try:
            extrato = self.contaService.consultar_extrato(tipo_conta, data_atual)
            return {"extrato": extrato}
        except ValueError as e:
            return {"error": str(e)}, 400

    def realizar_transferencia(self, conta_origem, conta_destino, valor):
        data_atual = date.today()
        if (conta_origem == "corrente"):
            if (conta_destino == "poupanca"):
                try:
                    self.contaService.realizar_transferencia(conta_origem, conta_destino, valor, data_atual)
                    return {"success": True}
                except ValueError as e:
                    return {"error": str(e)}, 400
            else:                 
                return 'A conta de destino está errada, ou está tentando transferência para a mesma conta'
       
        elif (conta_origem == "poupanca"):
            if (conta_destino == "corrente"):
                try:
                    self.contaService.realizar_transferencia(conta_origem, conta_destino, valor, data_atual)
                    return {"success": True}
                except ValueError as e:
                    return {"error": str(e)}, 400
            else:                 
                return 'A conta de destino está errada, ou está tentando transferência para a mesma conta'
        else:
            return 'A conta de origem só pode estar nas opçôes "corrente" ou "poupanca"'

            
        

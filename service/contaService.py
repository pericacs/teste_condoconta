from datetime import date

class ContaService:

    data_atual = date.today()

    def __init__(self, data_atual):
        self.saldo_conta_corrente = 1000.00
        self.saldo_conta_poupanca = 1.00
        self.valores_extrato_corrente = [data_atual, 'Saldo Inicial Conta Corrente', 0, 1000.00]
        self.extrato_corrente.append(self.valores_extrato_corrente) 
        self.valores_extrato_poupanca = [data_atual, 'Saldo Inicial Conta Poupança', 0, 1.00]
        self.extrato_poupanca.append(self.valores_extrato_poupanca) 

    def consultar_saldo(self, conta):
        if conta == "corrente":
            return self.extrato_corrente[3]
        if conta == "poupanca":
            return self.extrato_poupanca[3]
    
  
    def consultar_extrato(self, tipo_conta, data_atual):
        if tipo_conta == "corrente":
            for extrato in self.extrato_corrente:
                print(extrato)
        if tipo_conta == "poupanca":
            for extrato in self.extrato_poupanca:
                print(extrato)

        
        
    def realizar_transferencia(self, conta_origem, conta_destino, valor, data_atual):
        if (conta_origem == "corrente"):
            valores_extrato_corrente = [self.extrato_corrente[-1]]
            if valores_extrato_corrente[3] >= valor:
                saldo_atual = valores_extrato_corrente[3] - valor
                valores_extrato_corrente = [data_atual, 'Transferência para conta poupança', valor, saldo_atual]
                self.extrato_corrente.append(valores_extrato_corrente)                                            
            else:
                return 'Saldo Insuficiente !'
                       
        if (conta_origem == "poupanca"):
            valores_extrato_poupanca = [self.extrato_poupanca[-1]]
            if valores_extrato_poupanca[3] >= valor:
                saldo_atual = valores_extrato_poupanca[3] - valor
                valores_extrato_poupanca = [data_atual, 'Transferência para conta poupança', valor, saldo_atual]
                self.extrato_poupanca.append(valores_extrato_poupanca)                
            else:
                return 'Saldo Insuficiente !'        
            
        if (conta_destino == "corrente"):
            valores_extrato_corrente = [self.extrato_corrente[-1]]
            saldo_atual = valores_extrato_corrente[3] + valor
            valores_extrato_corrente = [data_atual, 'Recebimento da Conta Poupança', valor, saldo_atual]
            self.extrato_corrente.append(valores_extrato_corrente)              

        if (conta_destino == "poupanca"):
            valores_extrato_poupanca = [self.extrato_poupanca[-1]]            
            saldo_atual = valores_extrato_poupanca[3] + valor
            valores_extrato_poupanca = [data_atual, 'Transferência para conta poupança', valor, saldo_atual]
            self.extrato_poupanca.append(valores_extrato_poupanca)                
    

        return 'Transferência Realizada com Sucesso !'      
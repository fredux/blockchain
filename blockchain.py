#Ememplo simples de como funciona um blockchain

import hashlib
import json
current_transactions = []
blockchain = []
#adiciona um novo bloco
def adicionaBloco(novoBloco):
    global blockchain
    blockchain.append(novoBloco)

#cria hash do bloco atual usando como base o bloco anterior
def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


#bloco genesis - primeiro bloco da cadeia
current_transactions.append({
            'remetente': 'Miguel2',
            'destinatario': 'Julio',
            'mensagem': '5 BTC'
        })
current_transactions.append({
            'remetente': 'Pedro',
            'destinatario': 'Miguel',
            'mensagem': '6 BTC'
        })
current_transactions.append({
            'remetente': 'Jose',
            'destinatario': 'Maria',
            'mensagem': '10 BTC'
        })

block1 = {
            'transacoes': len(blockchain) + 1,
            'transactions': current_transactions,
            'previous_hash': '1'
        }
#adiciona o bloco 1
adicionaBloco(block1)
current_transactions = []

#bloco 2
current_transactions.append({
            'remetente': 'teste2',
            'destinatario': 'Fulano',
            'mensagem': '4 BTC'
        })
current_transactions.append({
            'remetente': 'igor',
            'destinatario': 'jose',
            'mensagem': '4 BTC'
        })

block2 = {
            'transacoes': len(blockchain) + 1,
            'transactions': current_transactions,
            'previous_hash': hash(blockchain[-1])            
        }

adicionaBloco(block2)
current_transactions = []

#bloco 3
current_transactions.append({
            'remetente': 'pipa4',
            'destinatario': 'pica-pau',
            'mensagem': '6 BTC'
        })
current_transactions.append({
            'remetente': 'pato donald',
            'destinatario': 'gastão',
            'mensagem': '2 BTC'
        })

block3 = {
            'transacoes': len(blockchain) + 1,
            'transactions': current_transactions,
            'previous_hash': hash(blockchain[-1])            
        }

adicionaBloco(block3)
current_transactions = []

#imprime os valores
for block in blockchain:
    print('Hash:' + block['previous_hash'])
    for transacao in block['transactions']:
        print('Remetente: ' + transacao['remetente'] + ' - Destinatario: '+ transacao['destinatario'] + '  - Mensagem: '+ transacao['mensagem'])
    print('-'*80)






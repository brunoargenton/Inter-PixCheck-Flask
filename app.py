# Importando as bibliotecas necessárias do Flask e outras dependências
from flask import Flask, render_template
from flask import request
import datetime
import requests
import time

# Inicializando a aplicação Flask
app = Flask(__name__)

# Lista de nomes de destinatários a serem excluídos do cálculo total
exclusoes = ('John Doe', 'Ifood Com Agencia De Restaurantes Online Sa')

# Configurando o fuso horário para o horário de Brasília (GMT-3)
fuso_horario = datetime.timezone(datetime.timedelta(hours=-3))

# Obtendo a data atual no fuso horário configurado para o início e fim do intervalo
inicio = datetime.datetime.now(fuso_horario).strftime("%Y-%m-%d")
fim = datetime.datetime.now(fuso_horario).strftime("%Y-%m-%d")

# Teste com um dia específico que teve transações
# inicio = "2023-12-13"
# fim = "2023-12-13"

# Inicializando variáveis para o token, URL do saldo e total das transações
token = ''
urlSaldo = "https://cdpj.partners.bancointer.com.br/banking/v2/extrato"
total = 0

# Parâmetros para a requisição à API do Banco Inter
params = {
    "dataInicio": inicio,
    "dataFim": fim,
}

# Corpo da requisição para obter o token de autenticação, insira aqui o client_id e client_secret obtidos na plataforma de desenvolvimento do Banco Inter
request_body = "client_id=XXXXX-XXXX-XXXX-XXXXX-XXXXXXX&client_secret=XXXXX-XXXX-XXXX-XXXXX-XXXXXXX&scope=extrato.read&grant_type=client_credentials"

# Caminhos para os arquivos de certificado.crt e chave.key
cert_paths = (
    '/home/rasp01/pixcheck_flask/certificado.crt',
    '/home/rasp01/pixcheck_flask/chave.key'
)

# Rota principal que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Função para renovar o token de autenticação
def renew_token():
    global token

    # Verificando se o token já está presente
    if token:
        return

    # Realizando a requisição para obter o token de autenticação
    response = requests.post(
        "https://cdpj.partners.bancointer.com.br/oauth/v2/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=request_body,
        cert=cert_paths
    )
    response.raise_for_status()

    # Armazenando o token obtido
    token = response.json()['access_token']

# Função para obter o extrato das transações Pix
def get_extrato():
    global data, token
    total = 0

    # Realizando a requisição para obter o extrato
    response = requests.get(urlSaldo,
                            params=params,
                            headers={"Authorization": "Bearer " + token},
                            cert=cert_paths
                            )
    if response.status_code == 200:
        data = response.json()

# Rota para atualizar a tabela de transações
@app.route('/update_table')
def update_table():
    global data, total

    # Renovando o token de autenticação e obtendo o extrato das transações
    renew_token()
    get_extrato()

    # Calculando o total das transações Pix recebidas, excluindo destinatários específicos
    for transacao in data['transacoes']:
        if transacao['titulo'] == 'Pix recebido':
            if transacao['descricao'] not in exclusoes:
                total += float(transacao['valor'])

    # Formatando o total em formato de moeda
    total_text = "R$ " + format(total, '.2f')

    # Renderizando a tabela HTML com os dados das transações e o total calculado
    return render_template('table.html', data=data['transacoes'], total_text=total_text)

# Iniciando a aplicação Flask se este script for executado diretamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

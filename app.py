from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import dados
import porcentagem
import psycopg2

connection=psycopg2.connect(database='investimento_fii',
                         host='localhost',
                         user='postgres',
                         password='SUA SENHA',
                         port='5432'
                         )

connection.info
connection_status_sql = connection.status # se for 1, está perfeito # se for 1, está perfeito
if connection_status_sql == 1:
    print('\033[32mConexão feita com sucesso !\n')
else:
    print(f'Error : {connection_status_sql}')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SUASENHA@localhost:5432/investimento_fii'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Investimento(db.Model):
    __tablename__='invest'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_total = db.Column(db.Float, nullable=False)

# with app.app_context():       #Como criei o banco de dados SQL a parte no próprio SGBD, não precisa desse comando
#     db.create_all()

@app.route('/', methods=['GET'])
def inicio():
    dados_fiss = dados.obter_dados()
    investimentos = Investimento.query.all()
    valor_total = db.session.query(db.func.sum(Investimento.preco_total)).scalar() or 0
    return render_template('index.html', dados_fiss=dados_fiss, investimentos=investimentos, valor_total=valor_total)

@app.route('/investir', methods=['GET', 'POST'])
def investir():
    dados_fiss = dados.obter_dados()
    calculo_porcentagem = []
    valor_total = 0  # Inicializa a variável valor_total
    if request.method == 'POST':
        valor_investir = float(request.form.get('valor_investir'))
        calculo_porcentagem = porcentagem.dividir_investimento(valor_investir)
        # Calcula o valor total somando todos os totais calculados
        valor_total = sum(item[2] for item in calculo_porcentagem)
    return render_template('investir.html', dados_fiss=dados_fiss, calculo_porcentagem=calculo_porcentagem, valor_total=valor_total)

@app.route('/aplicar', methods=['POST'])
def aplicar():
    tickers = request.form.getlist('ticker')
    quantidades = request.form.getlist('quantidade')
    totais = request.form.getlist('total')

    for ticker, quantidade, total in zip(tickers, quantidades, totais):
        quantidade = int(float(quantidade))
        total = float(total)
        if quantidade > 0:
            investimento = Investimento.query.filter_by(ticker=ticker).first()
            if investimento:
                investimento.quantidade += quantidade
                investimento.preco_total += total
            else:
                novo_investimento = Investimento(ticker=ticker, quantidade=quantidade, preco_total=total)
                db.session.add(novo_investimento)
            db.session.commit()
            print('-'*20,'Comitado','-'*20)

    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

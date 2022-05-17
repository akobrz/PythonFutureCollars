import flask
from accountant import manager

config = {
    "DEBUG": True
}

app = flask.Flask(__name__)
app.config.from_mapping(config)

file_name = "in.txt"

@app.route('/', methods=['GET', 'POST'])
def main():
    w = ""
    if flask.request.method == 'POST':
        f = flask.request.form
        if 'buy_name' in f and len(f['buy_name']) > 0 and len(f['buy_cost']) > 0 and len(f['buy_amount']) > 0:
            t = [f['buy_name'], f['buy_cost'], f['buy_amount']]
            o = manager.execute("dodaj_kupno", manager.execute("odczytaj", file_name), t)
            manager.execute("zapisz", o, file_name)
        elif 'buy_name' in f and (len(f['buy_name']) == 0 or len(f['buy_cost']) == 0 or len(f['buy_amount']) == 0):
            w = "WARNING, incomplete buying operation data"
        if 'sell_name' in f and len(f['sell_name']) > 0 and len(f['sell_cost']) > 0 and len(f['sell_amount']) > 0:
            t = [f['sell_name'], f['sell_cost'], f['sell_amount']]
            o = manager.execute("dodaj_sprzedaz", manager.execute("odczytaj", file_name), t)
            manager.execute("zapisz", o, file_name)
        elif 'sell_name' in f and (len(f['sell_name']) == 0 or len(f['sell_cost']) == 0 or len(f['sell_amount']) == 0):
            w = "WARNING, incomplete selling operation data"
        if 'cash_info' in f and len(f['cash_info']) > 0 and len(f['cash_amount']) > 0:
            t = [f['cash_amount'], f['cash_info']]
            o = manager.execute("dodaj_saldo", manager.execute("odczytaj", file_name), t)
            manager.execute("zapisz", o, file_name)
        elif 'cash_info' in f and (len(f['cash_info']) == 0 or len(f['cash_amount']) == 0):
            w = "WARNING, incomplete cash operation data"
    s, m = manager.execute("magazynuj", manager.execute("odczytaj", file_name))
    return flask.render_template("view_price.html", store=m, saldo=s, invalid_data=w)

@app.route('/history', methods=['GET'])
@app.route('/history/', methods=['GET'])
def full_history():
    operations = manager.execute("odczytaj", file_name)
    return flask.render_template("history.html", operations=operations)

@app.route('/history/<line_from>/<line_to>', methods=['GET'])
@app.route('/history/<line_from>/<line_to>/', methods=['GET'])
def short_history(line_from, line_to):
    operations = manager.execute("odczytaj", file_name)
    return flask.render_template("history.html", operations=operations[int(line_from):int(line_to)])

if __name__ == "__main__":
    app.run()


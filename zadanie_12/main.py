import flask
from aplikacja import app
from accountant import manager


@app.route('/', methods=['GET', 'POST'])
def main():
    warning = ""

    def buy_validator(f):
        return len(f['buy_name']) > 0 and len(f['buy_cost']) > 0 and len(f['buy_amount']) > 0

    def sell_validator(f):
        return 'sell_name' in f and len(f['sell_name']) > 0 and len(f['sell_cost']) > 0 and len(f['sell_amount']) > 0

    def saldo_validator(f):
        return 'cash_info' in f and len(f['cash_info']) > 0 and len(f['cash_amount']) > 0

    if flask.request.method == 'POST':
        f = flask.request.form
        if 'buy_name' in f:
            if buy_validator(f):
                t = [f['buy_name'], f['buy_cost'], f['buy_amount']]
                o = manager.execute("dodaj_kupno", manager.execute("odczytaj"), t)
                manager.execute("zapisz", o)
            else:
                warning = "WARNING, incomplete buying operation data"
        if 'sell_name' in f:
            if sell_validator(f):
                t = [f['sell_name'], f['sell_cost'], f['sell_amount']]
                o = manager.execute("dodaj_sprzedaz", manager.execute("odczytaj"), t)
                manager.execute("zapisz", o)
            else:
                warning = "WARNING, incomplete selling operation data"
        if 'cash_info' in f:
            if saldo_validator(f):
                t = [f['cash_amount'], f['cash_info']]
                o = manager.execute("dodaj_saldo", manager.execute("odczytaj"), t)
                manager.execute("zapisz", o)
            else:
                warning = "WARNING, incomplete cash operation data"
    s, m = manager.execute("magazynuj", manager.execute("odczytaj"))
    return flask.render_template("view_price.html", store=m, saldo=s, invalid_data=warning)


@app.route('/history', methods=['GET'])
@app.route('/history/', methods=['GET'])
def full_history():
    operations = manager.execute("odczytaj")
    return flask.render_template("history.html", operations=operations)


@app.route('/history/<line_from>/<line_to>', methods=['GET'])
@app.route('/history/<line_from>/<line_to>/', methods=['GET'])
def short_history(line_from, line_to):
    operations = manager.execute("odczytaj")
    return flask.render_template("history.html", operations=operations[int(line_from):int(line_to)])


if __name__ == "__main__":
    app.run()


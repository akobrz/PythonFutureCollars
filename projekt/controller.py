import flask


def menu():
    # if flask.request.method == 'POST':
    #     f = flask.request.form
    return flask.render_template("menu.html", store="m", saldo="s", invalid_data="warning")


# @app.route('/history', methods=['GET'])
# @app.route('/history/', methods=['GET'])
# def full_history():
#     return flask.render_template("history.html", operations=[])
#
#
# @app.route('/history/<line_from>/<line_to>', methods=['GET'])
# @app.route('/history/<line_from>/<line_to>/', methods=['GET'])
# def short_history(line_from, line_to):
#     return flask.render_template("history.html", operations=[])


if __name__ == "__main__":
    pass

from projekt.portals import portal_olx, portal_otodom
from projekt.models import offer, offer_dto
from projekt.services.services import Services
from projekt import application
import operator
import flask

def refresh_data():
    # portal_olx.Portal_Olx().load_page(1)
    # portal_olx.Portal_Olx().load_page(2)
    portal_otodom.Portal_otodom().load_page(1)
    # portal_otodom.Portal_otodom().load_page(2)
    # portal_otodom.Portal_otodom().load_page(3)

@application.app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        f = flask.request.form
        print("/", f)
        if 'refresh' in f.values():
            # refresh_data()
            # return flask.redirect(flask.request.path)
            return flask.redirect("/refresh")
        elif 'view' in f.keys():
            if 'price' in f.values():
                return flask.render_template("view.html", houses=Services().get_active_order_by_price())
            elif 'read' in f.values():
                return flask.render_template("view.html", houses=Services().get_active_order_by_read())
        elif 'edit' in f.keys():
            print('edit')
        elif 'settings' in f.keys():
            print('settings')
    return flask.render_template("menu.html")

@application.app.route('/refresh', methods=['GET', 'POST'])
def refreshing():
    f = flask.request.form
    print("refresh", f)
    flask.render_template("refresh.html")
    refresh_data()
    return flask.redirect("/")



def start_app():
    application.app.run()

if __name__ == "__main__":
    start_app()

from projekt.portals import portal_olx
from projekt.models import offer, offer_dto
from projekt import application
import operator
import flask


@application.app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        f = flask.request.form
        if 'view' in f.keys():
            houses = [offer_dto.OfferDTO().transfer_from_offer(h) for h in offer.Offer().load_all()]
            return flask.render_template("view.html", houses=sorted(houses, key=operator.attrgetter('price')))
        if 'edit' in f.keys():
            print('edit')
        if 'settings' in f.keys():
            print('settings')
    return flask.render_template("menu.html")

def refresh_data():
    portal_olx.Portal_Olx().load_page(1)
    portal_olx.Portal_Olx().load_page(2)

def start_app():
    application.app.run()

if __name__ == "__main__":
    # refresh_data()
    start_app()

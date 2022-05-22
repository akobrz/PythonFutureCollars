from projekt.portals import portal_olx, portal_otodom
from projekt.models import offer, criteria
from projekt.services import variables
from projekt.services.services import Services
from projekt import application
import flask



def refresh_data():

    # portal_olx.Portal_Olx().load_page(1)
    # portal_olx.Portal_Olx().load_page(2)
    portal_otodom.Portal_otodom().load(variables.TARGET_HOUSE)
    portal_otodom.Portal_otodom().load(variables.TARGET_FLAT)


@application.app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        f = flask.request.form
        if 'refresh' in f.values():
            refresh_data()
            return flask.redirect(flask.request.path)
        elif 'view' in f.keys():
            if 'priority' in f.values():
                return flask.redirect("/view/priority")
            elif 'price' in f.values():
                return flask.redirect("/view/price")
            elif 'read' in f.values():
                return flask.redirect("/view/date")
            elif 'disabled' in f.values():
                return flask.redirect("/view/disabled")
    return flask.render_template("menu.html")

@application.app.route('/view/priority', methods=['GET', 'POST'])
def view_priority():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'menu' in f.values():
            return flask.redirect("/")
    return flask.render_template("view_priority.html", houses=Services().get_priority_order_by_read())

@application.app.route('/view/date', methods=['GET', 'POST'])
def view_date():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'menu' in f.values():
            return flask.redirect("/")
    return flask.render_template("view_date.html", houses=Services().get_active_order_by_read())

@application.app.route('/view/price', methods=['GET', 'POST'])
def view_price():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'menu' in f.values():
            return flask.redirect("/")
    return flask.render_template("view_price.html", houses=Services().get_active_order_by_price())

@application.app.route('/view/disabled', methods=['GET', 'POST'])
def view_disabled():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'menu' in f.values():
            return flask.redirect("/")
    return flask.render_template("view_disabled.html", houses=Services().get_disabled_order_by_last())

@application.app.route('/refresh', methods=['GET', 'POST'])
def refreshing():
    refresh_data()
    return flask.redirect("/")

@application.app.route('/disable/date/<id>', methods=['GET', 'POST'])
def disable_date(id):
    offer.Offer().disable_by_id(id)
    return flask.redirect("/view/date")

@application.app.route('/disable/price/<id>', methods=['GET', 'POST'])
def disable_price(id):
    offer.Offer().disable_by_id(id)
    return flask.redirect("/view/price")

@application.app.route('/priority/date/<id>', methods=['GET', 'POST'])
def priority_date(id):
    offer.Offer().priority_by_id(id)
    return flask.redirect("/view/date")

@application.app.route('/priority/price/<id>', methods=['GET', 'POST'])
def priority_price(id):
    offer.Offer().priority_by_id(id)
    return flask.redirect("/view/price")

@application.app.route('/enable/<id>', methods=['GET', 'POST'])
def enable(id):
    offer.Offer().enable_by_id(id)
    return flask.redirect("/view/price")

@application.app.route('/edit/priority/<id>', methods=['GET', 'POST'])
def edit_priority(id):
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'save' in f.keys():
            Services().update_offer_after_save(f)
        return flask.redirect("/view/priority")
    h = offer.Offer().load_by_id(id)
    return flask.render_template("edit.html", house=h)

@application.app.route('/edit/date/<id>', methods=['GET', 'POST'])
def edit_date(id):
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'save' in f.keys():
            Services().update_offer_after_save(f)
        return flask.redirect("/view/date")
    h = offer.Offer().load_by_id(id)
    return flask.render_template("edit.html", house=h)

@application.app.route('/edit/price/<id>', methods=['GET', 'POST'])
def edit_price(id):
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'save' in f.keys():
            Services().update_offer_after_save(f)
        return flask.redirect("/view/price")
    h = offer.Offer().load_by_id(id)
    return flask.render_template("edit.html", house=h)

@application.app.route('/criteria/house', methods=['GET', 'POST'])
def criteria_house():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'save' in f.keys():
            Services().update_criteria_after_save(f, variables.TARGET_HOUSE)
        return flask.redirect("/")
    crit = criteria.Criteria().load(variables.TARGET_HOUSE)
    return flask.render_template("criteria.html", crit=crit)

@application.app.route('/criteria/flat', methods=['GET', 'POST'])
def criteria_flat():
    f = flask.request.form
    if flask.request.method == 'POST':
        if 'save' in f.keys():
            Services().update_criteria_after_save(f, variables.TARGET_FLAT)
        return flask.redirect("/")
    crit = criteria.Criteria().load(variables.TARGET_FLAT)
    return flask.render_template("criteria.html", crit=crit)

def start_app():
    application.app.run()

if __name__ == "__main__":
    start_app()

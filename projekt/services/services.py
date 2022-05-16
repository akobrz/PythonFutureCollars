from projekt.models.offer import Offer
from projekt.models.offer_dto import OfferDTO
import operator

class Services:

    def get_active_order_by_price(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_active_all()]
        return sorted(houses, key=operator.attrgetter('price'))

    def get_active_order_by_first(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_active_all()]

        h = sorted(houses, key=operator.attrgetter('first'))
        print([x.first for x in h])
        return sorted(houses, key=operator.attrgetter('first'))

    def get_active_order_by_last(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_active_all()]
        return sorted(houses, key=operator.attrgetter('last'))

    def get_active_order_by_read(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_active_all()]
        return sorted(houses, key=operator.attrgetter('read'))
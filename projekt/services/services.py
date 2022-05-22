from projekt.models.offer import Offer
from projekt.models.criteria import Criteria
from projekt.models.offer_dto import OfferDTO
from projekt.services import variables
import operator

class Services:

    def get_priority_order_by_read(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_priority_all()]
        return sorted(houses, key=operator.attrgetter('read'))

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

    def get_disabled_order_by_last(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_disabled_all()]
        return sorted(houses, key=operator.attrgetter('last'))

    def get_active_order_by_read(self):
        houses = [OfferDTO().from_offer(h) for h in Offer().load_active_all()]
        return sorted(houses, key=operator.attrgetter('read'))

    def update_offer_after_save(self, f):
        o = Offer()
        o.id = int(f.get('save'))
        o.price = f.get('input-price', '')
        o.area = f.get('input-area', 0)
        o.city = f.get('input-city', '')
        o.district = f.get('input-district', '')
        o.street = f.get('input-street', '')
        o.info = str(f.get('input-info', ''))
        o.update_after_edit()

    def update_criteria_after_save(self, f, target):
        criteria = Criteria()
        criteria.price_min = f.get('input-price-min', 0)
        criteria.price_max = f.get('input-price-max', 0)
        criteria.area = f.get('input-area', 0)
        criteria.update_after_edit(target)


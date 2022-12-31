from store.models import Product
from decimal import Decimal

class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        '''
        adding and updating the users basket session data
        '''
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.save()

    def __iter__(self):
        '''
        collect the produtc_id in the session data to query the database and return products
        '''
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()



        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        '''
        get the basket data and count the quantity of items
        '''
        return sum(item['qty'] for item in self.basket.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        product_id = str(product)
        print(type(product_id))

        if product_id in self.basket:
            del self.basket[product_id]
        self.save()


    def save(self):
        self.session.modified = True
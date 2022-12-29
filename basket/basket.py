from store.models import Product

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
        self.session.modified = True

    def __len__(self):
        '''
        get the basket data and count the quantity of items
        '''
        return sum(item['qty'] for item in self.basket.values())

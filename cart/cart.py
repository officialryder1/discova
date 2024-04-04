from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if exists
        cart = self.session.get('session_key')

        # if the user is new, no session key: create  one;
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all page
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] ={'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    # get tthe number of item in cart
    def __len__(self):
        return len(self.cart)
    
    def get_probs(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    # def delete(self, product):
    #     product_id = product.id
    #     product.delete()

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def cart_total(self):
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in=product_id)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total




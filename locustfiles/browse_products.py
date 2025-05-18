from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    # Set the host for your API - replace with your actual API URL
    host = "http://localhost:8000"  # Update this to your API server address
    wait_time = between(1, 5)  # Wait time between tasks

    @task(2)
    def view_products(self):
        print('view product')
        collection_id = randint(2, 6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name='/store/products')

    @task(4)
    def view_product(self):
        print('view product details')
        product_id = randint(1, 1000)
        self.client.get(f'/store/products/{product_id}', name='/store/products/:id')

    @task(1)
    def add_to_cart(self):
        print('add to cart')
        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/', name='/store/carts/items', json={'product_id': product_id, 'quantity': 1})

    def on_start(self):  # This method is called when a simulated user starts (lifecycle hook)
        response = self.client.post('/store/carts/')
        self.cart_id = response.json()["id"]

    def view_hello(self):
        print('view hello')
        self.client.get('/playground/hello/', name='/playground/hello')
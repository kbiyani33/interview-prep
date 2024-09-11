from typing import Dict, List, Optional
from datetime import datetime

class OnlineShoppingSystem:
    def __init__(self) -> None:
        self.users: Dict[int, User] = {}
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}

    def add_user(self, user: 'User') -> None:
        self.users[user.user_id] = user

    def remove_user(self, user_id: int) -> None:
        if user_id in self.users:
            del self.users[user_id]

    def add_product(self, product: 'Product') -> None:
        self.products[product.product_id] = product

    def remove_product(self, product_id: int) -> None:
        if product_id in self.products:
            del self.products[product_id]

    def add_order(self, order: 'Order') -> None:
        self.orders[order.order_id] = order

    def remove_order(self, order_id: int) -> None:
        if order_id in self.orders:
            del self.orders[order_id]

class User:
    def __init__(self, user_id: int, name: str, email: str, password: str) -> None:
        self.user_id: int = user_id
        self.name: str = name
        self.email: str = email
        self.password: str = password
        self.logged_in: bool = False
        self.orders: Dict[int, Order] = {}
        self.payment_methods: Dict[int, PaymentMethod] = {}
        self.cart: ShoppingCart = ShoppingCart()

    def login_user(self) -> bool:
        self.logged_in = True
        return self.logged_in

    def logout_user(self) -> None:
        self.logged_in = False

    def add_new_order(self, order: 'Order') -> None:
        self.orders[order.order_id] = order

    def cancel_order(self, order_id: int) -> None:
        if order_id in self.orders and self.orders[order_id].status == "IN_PROCESS":
            self.orders[order_id].update_status("CANCELLED")
            del self.orders[order_id]

    def update_cart_with_product(self, product: 'Product', quantity: int) -> None:
        if product.stock >= quantity:
            self.cart.add_product(product, quantity)
            product.stock -= quantity

    def add_payment_method(self, payment_method: 'PaymentMethod') -> None:
        self.payment_methods[payment_method.method_id] = payment_method

class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float, stock: int) -> None:
        self.product_id: int = product_id
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.stock: int = stock

class Order:
    def __init__(self, order_id: int, user: 'User', products: Dict['Product', int]) -> None:
        self.order_id: int = order_id
        self.user: User = user
        self.products: Dict[Product, int] = products
        self.order_date: datetime = datetime.now()
        self.status: str = "IN_PROCESS"
        self.payment_information: Optional[Payment] = None

    def update_status(self, status: str) -> None:
        self.status = status

    def cancel_order(self) -> None:
        self.update_status("CANCELLED")

class ShoppingCart:
    def __init__(self) -> None:
        self.products: Dict[int, int] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if product.product_id in self.products:
            self.products[product.product_id] += quantity
        else:
            self.products[product.product_id] = quantity

    def remove_product(self, product_id: int) -> None:
        if product_id in self.products:
            del self.products[product_id]

    def view_cart(self) -> List[Dict[int, int]]:
        return list(self.products.items())

    def get_total_price(self, product_catalog: Dict[int, Product]) -> float:
        return sum(product_catalog[product_id].price * quantity for product_id, quantity in self.products.items())

class PaymentMethod:
    def __init__(self, method_id: int, method_type: str, details: str) -> None:
        self.method_id: int = method_id
        self.method_type: str = method_type
        self.details: str = details

class Payment:
    def __init__(self, payment_id: int, amount: float, payment_date: datetime, payment_method: 'PaymentMethod') -> None:
        self.payment_id: int = payment_id
        self.amount: float = amount
        self.payment_date: datetime = payment_date
        self.payment_method: PaymentMethod = payment_method
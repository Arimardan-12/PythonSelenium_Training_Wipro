import pytest
import time
import json
from datetime import datetime


# REQUIREMENT 1: Functional / End-to-End Application Logic
class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name, email):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = {
            "name": name,
            "email": email,
            "created_at": datetime.now().isoformat()
        }
        return self.users[user_id]

    def get_user(self, user_id):
        if user_id not in self.users:
            raise KeyError("User not found")
        return self.users[user_id]

    def update_user(self, user_id, name=None, email=None):
        if user_id not in self.users:
            raise KeyError("User not found")
        if name:
            self.users[user_id]["name"] = name
        if email:
            self.users[user_id]["email"] = email
        return self.users[user_id]

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise KeyError("User not found")
        del self.users[user_id]
        return True


class OrderService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.orders = {}
        self.counter = 0

    def create_order(self, user_id, items, total):
        # Ensures order creation depends on valid user (functional behavior)
        self.user_service.get_user(user_id)
        self.counter += 1
        order_id = f"ORD-{self.counter}"
        self.orders[order_id] = {
            "user_id": user_id,
            "items": items,
            "total": total,
            "status": "pending",
            "created_at": datetime.now().isoformat()
        }
        return order_id, self.orders[order_id]

    def update_order_status(self, order_id, status):
        if order_id not in self.orders:
            raise KeyError("Order not found")
        valid_status = ["pending", "confirmed", "shipped", "delivered", "cancelled"]
        if status not in valid_status:
            raise ValueError("Invalid status")
        self.orders[order_id]["status"] = status
        return self.orders[order_id]

    def get_order(self, order_id):
        if order_id not in self.orders:
            raise KeyError("Order not found")
        return self.orders[order_id]


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, pid, name, price, qty=1):
        for item in self.items:
            if item["product_id"] == pid:
                item["quantity"] += qty
                return self.items
        self.items.append({
            "product_id": pid,
            "name": name,
            "price": price,
            "quantity": qty
        })
        return self.items

    def get_total(self):
        return sum(i["price"] * i["quantity"] for i in self.items)

    def clear(self):
        self.items = []



# REQUIREMENT 5 (Part): Pytest Fixtures for Scalable Test Automation


@pytest.fixture
def user_service():
    return UserService()

@pytest.fixture
def order_service(user_service):
    return OrderService(user_service)

@pytest.fixture
def shopping_cart():
    return ShoppingCart()

@pytest.fixture
def history_file(tmp_path):
    return tmp_path / "execution_history.json"


# REQUIREMENT 1:Functional / End-to-End Test Cases

class TestUserFunctional:
    def test_user_lifecycle(self, user_service):
        # Create user
        user = user_service.create_user("u1", "Alice", "a@test.com")
        assert user["name"] == "Alice"

        # Read user
        fetched = user_service.get_user("u1")
        assert fetched["email"] == "a@test.com"

        # Update user
        updated = user_service.update_user("u1", name="Alice Smith")
        assert updated["name"] == "Alice Smith"

        # Delete user
        assert user_service.delete_user("u1") is True

        # Validate deletion
        with pytest.raises(KeyError):
            user_service.get_user("u1")


class TestOrderFunctional:
    def test_order_workflow(self, user_service, order_service):
        user_service.create_user("buyer", "Buyer", "b@test.com")

        # Create order
        oid, order = order_service.create_order(
            "buyer",
            [{"item": "Laptop"}],
            1000
        )
        assert order["status"] == "pending"

        # Update order status (end-to-end flow)
        order_service.update_order_status(oid, "confirmed")
        order_service.update_order_status(oid, "shipped")
        order_service.update_order_status(oid, "delivered")

        # Verify final state
        assert order_service.get_order(oid)["status"] == "delivered"


class TestShoppingCartFunctional:
    def test_cart_flow(self, shopping_cart):
        shopping_cart.add_item("P1", "Keyboard", 100, 1)
        shopping_cart.add_item("P2", "Mouse", 50, 2)

        # Validate total calculation
        assert shopping_cart.get_total() == 200

        # Clear cart
        shopping_cart.clear()
        assert shopping_cart.get_total() == 0


class TestEndToEnd:
    def test_complete_ecommerce_flow(self, user_service, order_service, shopping_cart):
        # User creation
        user_service.create_user("cust1", "Customer", "c@test.com")

        # Cart operations
        shopping_cart.add_item("P1", "Laptop", 900, 1)
        shopping_cart.add_item("P2", "Bag", 100, 1)

        total = shopping_cart.get_total()

        # Order creation from cart
        oid, _ = order_service.create_order("cust1", shopping_cart.items, total)

        # Complete order lifecycle
        order_service.update_order_status(oid, "confirmed")
        order_service.update_order_status(oid, "delivered")

        assert order_service.get_order(oid)["status"] == "delivered"



# REQUIREMENT 2: Parallel Execution using pytest-xdist

class TestParallelExecution:
    @pytest.mark.parametrize("i", range(1, 11))
    def test_parallel_users(self, user_service, i):
        # Each parameter runs in parallel safely
        user = user_service.create_user(f"user{i}", f"User{i}", f"u{i}@test.com")
        assert user["name"] == f"User{i}"
        time.sleep(0.1)


# REQUIREMENT 4:Test Execution History Tracking


class TestHistoryTracking:
    def test_history_logging(self, history_file):
        # Record test execution data
        record = {
            "test": "test_history_logging",
            "status": "passed",
            "timestamp": datetime.now().isoformat()
        }

        history = []
        if history_file.exists():
            history = json.loads(history_file.read_text())

        history.append(record)
        history_file.write_text(json.dumps(history, indent=2))

        loaded = json.loads(history_file.read_text())
        assert len(loaded) >= 1



# REQUIREMENT 5:Explanation: Pytest Scalability Support


"""
Pytest supports scalable test automation by:
1. Fixtures for reusable setup and teardown
2. pytest-xdist for parallel execution
3. Parameterization for data-driven testing
4. HTML and JUnit reporting for CI/CD integration
5. Plugin-based architecture for extensibility
6. Simple syntax that scales to large test suites
"""

# =====================================================
# REQUIREMENT 3:
# Reporting (HTML & JUnit XML)
# =====================================================
# Commands to run:
#
# HTML Report:
# pytest test_functional_pytest.py --html=report.html --self-contained-html
#
# JUnit XML Report:
# pytest test_functional_pytest.py --junitxml=results.xml
#
# Parallel + Reports:
# pytest test_functional_pytest.py -n auto --html=report.html --junitxml=results.xml -v

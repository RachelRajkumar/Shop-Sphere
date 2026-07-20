# 🛒 Shop-Sphere

A modern E-Commerce web application built using **Django**, **Bootstrap**, and **SQLite**.

---

## ✨ Features

- **User Accounts**: Registration, Login, Secure Authentication, and Delete Account.
- **Product Management**: Product Listing, Product Search, and Category Filtering.
- **Shopping Experience**: Wishlist, Shopping Cart, Buy Now functionality, and Order Placement.
- **UI/UX**: Fully Responsive Design using Bootstrap 5.
- **Admin**: Comprehensive Django Admin Panel for store management.

---

## 🏗️ Backend Architecture

This project is structured for scalability and maintainability using custom backend modules. While standard Django handles the core, we have extended the architecture:

- **Services Layer** (`services.py`): Abstracts database queries and complex business logic (e.g., `ProductService` for fetching active products).
- **Validators** (`validators.py`): Reusable field-level validations (e.g., `validate_positive_price` and `validate_product_stock`).
- **Serializers** (`serializers.py`): Custom Python classes for converting Django model instances into JSON-serializable dictionaries.
- **Utilities** (`utils.py`): Independent helper functions (e.g., price formatting and discount calculation).
- **Middleware** (`shopsphere/middleware.py`): Includes custom middleware like `RequestTimingMiddleware` to log request processing performance.
- **Custom Management Commands**: Built-in Django command for automated tasks. Run `python manage.py export_products` to dump product data.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (Default)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RachelRajkumar/Shop-Sphere.git
   cd Shop-Sphere
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🧪 Testing

The project includes an extended suite of unit tests covering utilities, validators, services, and serializers. To run the tests:

```bash
python manage.py test
```

---

## 📦 Custom Commands

You can export all products to a JSON file using the custom management command:

```bash
python manage.py export_products --output products_export.json
```

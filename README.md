# Django E-commerce Storefront

A feature-rich backend built and cover all of Django and Django REST Framework uses.

## Features

- Authentication using JWT tokens with Djoser
- Product catalog with categories and collections
- Shopping cart functionality
- Order management system
- Redis caching for improved performance
- Celery for asynchronous tasks
- Email notifications
- User management
- Product reviews and ratings
- Comprehensive test suite
- API documentation

## Tech Stack

- Django 5.2.2
- Django REST Framework 3.16.0
- MySQL Database
- Redis for caching and Celery broker
- Celery for async tasks
- JWT Authentication
- CORS support

## Prerequisites

- Python 3.x
- MySQL
- Redis Server

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd storefront-django
```

2. Install dependencies using Pipenv:
```
pipenv install
```
3. For Development run 
```
pipenv shell
```

4. Set up the MySQL database:
```
mysql -u root -p
CREATE DATABASE storefront;
```
5. Populates the database with seed.sql
```
python manage.py seed_db
```

6. Configure environment variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_LOG_LEVEL=INFO
```

7. Database Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

8. Create a superuser:
```
python manage.py createsuperuser
```

## Development Server

Run the development server:
```
python manage.py runserver
```

Start Celery worker:
```
celery -A storefront worker --loglevel=info
```

Start Celery beat:
```
celery -A storefront beat --loglevel=info
```

## Project Structure

- `core/` - User management and base functionality
- `store/` - Main e-commerce functionality
- `playground/` - Testing and development endpoints
- `likes/` - Product rating system
- `tags/` - Product tagging system
- `storefront/` - Project settings and configuration

## API Endpoints

### Authentication
- `POST /auth/jwt/create/` - Get JWT token
- `POST /auth/jwt/refresh/` - Refresh JWT token
- `POST /auth/users/` - Register new user
- `GET /auth/users/me/` - Get current user details

### Products
- `GET /store/products/` - List all products
- `POST /store/products/` - Create a product
- `GET /store/products/{id}/` - Get product details
- `PUT /store/products/{id}/` - Update product
- `DELETE /store/products/{id}/` - Delete product
- `GET /store/products/{id}/reviews/` - Get product reviews

### Collections
- `GET /store/collections/` - List all collections
- `POST /store/collections/` - Create collection
- `GET /store/collections/{id}/` - Get collection details
- `PUT /store/collections/{id}/` - Update collection
- `DELETE /store/collections/{id}/` - Delete collection

### Cart
- `POST /store/carts/` - Create cart
- `GET /store/carts/{id}/` - Get cart details
- `POST /store/carts/{id}/items/` - Add item to cart
- `DELETE /store/carts/{id}/` - Delete cart
- `PATCH /store/carts/{id}/items/{id}/` - Update cart item
- `DELETE /store/carts/{id}/items/{id}/` - Remove cart item

### Orders
- `GET /store/orders/` - List user orders
- `POST /store/orders/` - Create order
- `GET /store/orders/{id}/` - Get order details
- `PATCH /store/orders/{id}/` - Update order

### Customers
- `GET /store/customers/` - List customers
- `GET /store/customers/me/` - Get current customer
- `PUT /store/customers/me/` - Update customer profile

### Reviews
- `GET /store/products/{id}/reviews/` - List product reviews
- `POST /store/products/{id}/reviews/` - Create review
- `DELETE /store/products/{id}/reviews/{id}/` - Delete review

## Testing

Run tests using pytest:
```
pytest
```

For development with auto-reloading:
```
ptw
```

## Performance Testing

Load testing with Locust:
```
locust -f locustfiles/browse_products.py
```

## Caching

The project uses Redis for caching with the following configuration:
- Cache timeout: 10 minutes
- Cache backend: django-redis

## Email Configuration

SMTP settings for development:
- Host: localhost
- Port: 2525
- Default sender: from@asib.com

## 🐛 Debugging

1. Django Debug Toolbar
2. Logging Configuration
3. Error Tracking

## 🔧 Maintenance

1. Database backups
2. Cache invalidation
3. Session cleanup
4. Media files management

## 📊 Monitoring Tools

1. Celery Flower
2. Redis Commander
3. MySQL Workbench

## Deployment

1. Set DEBUG=False in production
2. Configure proper ALLOWED_HOSTS
3. Use proper SECRET_KEY
4. Set up proper database credentials
5. Configure proper email settings
6. Set up static files with WhiteNoise

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
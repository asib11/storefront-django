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

3. Set up the MySQL database:
```
mysql -u root -p
CREATE DATABASE storefront;
```

4. Configure environment variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_LOG_LEVEL=INFO
```

5. Run migrations:
```
python manage.py migrate
```

6. Create a superuser:
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

- Authentication: `/auth/`
- Store API: `/store/`
- Product management: `/store/products/`
- Cart operations: `/store/carts/`
- Order management: `/store/orders/`

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

## Deployment

1. Set DEBUG=False in production
2. Configure proper ALLOWED_HOSTS
3. Use proper SECRET_KEY
4. Set up proper database credentials
5. Configure proper email settings
6. Set up static files with WhiteNoise

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
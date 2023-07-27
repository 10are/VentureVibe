# VentureVibe

VentureVibe is a Django-based web application that allows users to rate and review organizations based on various criteria. The platform aims to provide a space for users to share their experiences with organizations and help others make informed decisions.

## Installation

### Local Setup (Virtual Environment)

To run the project locally, follow these steps:

1. Clone the repository:

git clone <https://github.com/10are/VentureVibe.git>

cd venturevibe

2. Create and activate a virtual environment:

python3 -m venv env

source env/bin/activate # On Windows: env\Scripts\activate

3. Install project dependencies:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver


### Docker Setup

To run the project using Docker, make sure you have Docker installed on your system.

1. Clone the repository:

git clone <https://github.com/10are/VentureVibe.git>

cd venturevibe

2. Build the Docker image:

docker compose build

3. Run the Docker container:

docker compose up

## Important Packages Used

The following packages have been used in the project:

- **Django 3.2.9**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework 3.12.4**: A powerful and flexible toolkit for building Web APIs.
- **dj-rest-auth 2.1.10**: A Django app providing authentication features (JWT, social authentication) for Django REST framework.
- **django-allauth 0.45.0**: Integrated set of Django applications addressing authentication, registration, account management, and more.
- **django-cors-headers 3.8.0**: A Django app that adds Cross-Origin Resource Sharing (CORS) headers to responses.
- **django-countries 7.0**: A Django app that provides country choices for use with forms, flag icons, and more.
- **psycopg2 2.9.1**: PostgreSQL adapter for Python.

## Additional Notes

- The application allows users to register and authenticate using their email.
- Users can rate organizations as "like" or "dislike," which affects the overall rating of the organization.
- Organizations can be filtered based on country, business type, and other criteria.
- Users need to be authenticated to rate organizations.




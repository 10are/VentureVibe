VentureVibe

VentureVibe is a Django-based web application that allows users to rate and review organizations based on various criteria.

Project Overview
VentureVibe aims to provide a platform where users can rate and review organizations to share their experiences. It helps others make informed decisions about organizations they are interested in. The application allows users to like or dislike an organization and provides an overall rating based on user feedback.

Prerequisites
Python 3.9 or higher installed
Virtual environment (for local setup)
Setting Up the Development Environment
Local Setup (Virtual Environment)
# Clone the repository:
git clone <repository_url>
cd venturevibe

# Create and activate a virtual environment:
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install project dependencies:
pip install -r requirements.txt

# Apply migrations:
python manage.py migrate

# Run the development server:
python manage.py runserver


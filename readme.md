# AWS Cognito Backend

This Django project integrates AWS Cognito User Pool API with a backend server.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Before you start, make sure you have the following installed:
- Python >= 3.x
- pip package manager

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Aadilkhan2001/cognito_backend.git
    ```

2. Navigate to the project directory:
    ```sh
    cd cognito_backend
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

Before running the project, configure the necessary settings:

1. Set up environment variables:
    ```sh
    export AWS_COGNITO_CLIENT_ID='your_client_id'
    export AWS_COGNITO_CLIENT_SECRET='your_client_secret'
    export AWS_COGNITO_USER_POOL_ID='your_user_pool_id'
    export AWS_REGION='your_aws_region'
    ```

2. Update Django settings in `settings.py`, including database configuration, static files, etc.

### Database Setup

If your project requires a database:

1. Make migrations:
    ```sh
    python manage.py makemigrations
    ```

2. Apply migrations:
    ```sh
    python manage.py migrate
    ```

### Running the Server

Start the development server by running:
```sh
python manage.py runserver
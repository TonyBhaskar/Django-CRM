# Django CRM (Customer Relationship Management)

# Django CRM Project

This is a Customer Relationship Management (CRM) system built using Django, designed to manage customer details with robust authentication features. The application allows users to securely log in and access customer information, ensuring data privacy and integrity.

## Features

- **User Authentication**: Secure login and registration system to control access to customer data.
- **Customer Management**: Comprehensive management of customer details including name, address, city, state, zip code, date created, and ID.
- **Data Privacy**: Restricts access to customer information based on user authentication, ensuring that only authorized users can view and manage customer data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TonyBhaskar/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser for accessing the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Manage users and customer data through the Django admin panel at `http://127.0.0.1:8000/admin/`.
- **Login**: Securely log in to access and manage customer details.

## Contributing

We welcome contributions to enhance the functionality of this CRM system. To contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

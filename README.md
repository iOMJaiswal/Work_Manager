# Employee Management System

This project is an Employee Management System (EMS) built using Django and Cassandra as a database. It performs CRUD (Create, Read, Update, Delete) operations and an additional Fetch operation. The system allows the user to add, view, update, and delete employee records. Additionally, the system also allows users to fetch employees based on their designation.

The system is deployed on AWS.
## Prerequisites

* Python 3.7 or later installed on the system
* Django 3.0 or later installed on the system
* Cassandra 4.0 or later installed on the system
* AWS account for deployment

## Installation

1. Clone the repository

```bash
git clone https://github.com/iOMJaiswal/Work_Manager.git
```

2. Create a virtual environment and activate it.

```bash
python -m venv myenv
source myenv/bin/activate
```

3. Install the requirements.

```bash
pip install -r requirements.txt
```
4. Update the settings.py file with your Cassandra database details.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': 'employee_database',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'replication': {
                'strategy_class': 'SimpleStrategy',
                'replication_factor': 1
            }
        }
    }
}
```
5. Run the server.

```bash
python manage.py runserver
```

6. Navigate to http://localhost:8000/

## Usage

Once the system is set up, you can use it to perform CRUD operations on employee records. The system also allows you to fetch employees based on their designation.

To use the system, navigate to http://localhost:8000/ to access the homepage. From there, you can add, view, update, and delete employee records. To fetch employees based on their designation, navigate to http://localhost:8000/fetch_emp.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT]

# Creating Models in Django

In Django, models define the structure of our database tables. Each model is a Python class that subclasses `django.db.models.Model`. Django provides an ORM (Object-Relational Mapping) that allows us to interact with the database using Python code instead of raw SQL.

## Defining a Model

A basic model in Django consists of:
- A class that inherits from `models.Model`
- Fields to define attributes of the model (we will cover fields separately)
- A `Meta` class for additional configurations
- An overridden `__str__` method to provide a readable string representation of the model instance

### Example:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
```

### Explanation:
- **`name` and `email`**: These are character fields (we will discuss field types in another lecture).
- **`Meta` class**: It customizes the model's behavior. In this case, it defines singular and plural names.
- **`__str__` method**: It returns the `name` attribute when printing the model instance.

## Registering the Model

To make Django recognize our model, we need to register it in the `admin.py` file:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Now, Django's admin panel will display the `Student` model.

## Applying Migrations

After defining the model, we must create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the necessary database table for the `Student` model.

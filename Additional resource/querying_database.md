# Querying the Database with Django ORM

Django’s ORM (Object-Relational Mapping) provides a powerful way to interact with the database using Python code instead of SQL.

## 1. Retrieving All Objects

To fetch all records from a model:

```python
students = Student.objects.all()
```
- Returns a `QuerySet` containing all `Student` records.

---

## 2. Filtering Records

Retrieve records that match specific conditions:

```python
students = Student.objects.filter(name="John Doe")
```
- Equivalent to: `SELECT * FROM student WHERE name = 'John Doe'`

Retrieve students with a name starting with "J":

```python
students = Student.objects.filter(name__startswith="J")
```

Retrieve students whose email contains "gmail":

```python
students = Student.objects.filter(email__icontains="gmail")
```

---

## 3. Retrieving a Single Object

Get a single record using `.get()`:

```python
student = Student.objects.get(id=1)
```
- Raises an error if no record or multiple records match.

Use `.first()` or `.last()` to avoid errors:

```python
student = Student.objects.filter(name="John Doe").first()
```

---

## 4. Excluding Records

Retrieve all students except "John Doe":

```python
students = Student.objects.exclude(name="John Doe")
```

---

## 5. Ordering Query Results

Sort students by name (ascending):

```python
students = Student.objects.order_by("name")
```

Sort by name (descending):

```python
students = Student.objects.order_by("-name")
```

---

## 6. Selecting Specific Fields

Retrieve only names and emails:

```python
students = Student.objects.values("name", "email")
```

Retrieve as dictionaries:

```python
students = Student.objects.values_list("name", "email", flat=True)
```

---

## 7. Counting Records

Get the total number of students:

```python
count = Student.objects.count()
```

---

## 8. Limiting Query Results

Retrieve the first 5 students:

```python
students = Student.objects.all()[:5]
```

---

## 9. Checking Record Existence

Check if a student exists:

```python
exists = Student.objects.filter(email="john@example.com").exists()
```

---

## 10. Aggregation Queries

Find the total number of students:

```python
from django.db.models import Count

count = Student.objects.aggregate(total=Count("id"))
```

Find the average age of students:

```python
from django.db.models import Avg

average_age = Student.objects.aggregate(Avg("age"))
```

---

## 11. Raw SQL Queries

Django allows executing raw SQL:

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
```

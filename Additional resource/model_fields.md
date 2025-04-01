# Django Model Fields

Django provides different types of fields to define the structure and behavior of our database models. Each field corresponds to a column in the database.

## Commonly Used Field Types

### 1. `CharField`
Used for storing short text values such as names or titles.

```python
name = models.CharField(max_length=255)
```
- **`max_length`**: Defines the maximum length of the text.

---

### 2. `TextField`
Used for storing large text values such as descriptions.

```python
description = models.TextField()
```
- No `max_length` is required.

---

### 3. `IntegerField`
Stores integer values.

```python
age = models.IntegerField()
```
- Accepts positive and negative integers.

---

### 4. `FloatField`
Stores floating-point numbers.

```python
price = models.FloatField()
```
- Used for values with decimal points.

---

### 5. `DecimalField`
Stores decimal numbers with fixed precision.

```python
salary = models.DecimalField(max_digits=10, decimal_places=2)
```
- **`max_digits`**: Total number of digits.
- **`decimal_places`**: Digits after the decimal point.

---

### 6. `BooleanField`
Stores `True` or `False`.

```python
is_active = models.BooleanField(default=True)
```
- **`default`**: Sets a default value.

---

### 7. `DateField`
Stores dates.

```python
birth_date = models.DateField()
```
- Optionally, use `auto_now=True` to update it automatically.

---

### 8. `DateTimeField`
Stores date and time.

```python
created_at = models.DateTimeField(auto_now_add=True)
```
- **`auto_now_add=True`**: Sets the date/time when the object is created.
- **`auto_now=True`**: Updates the date/time when the object is modified.

---

### 9. `EmailField`
Validates and stores email addresses.

```python
email = models.EmailField(unique=True)
```
- **`unique=True`**: Ensures uniqueness in the database.

---

### 10. `URLField`
Stores URLs.

```python
website = models.URLField()
```

---

### 11. `SlugField`
Stores short labels typically used in URLs.

```python
slug = models.SlugField(unique=True)
```
- Often used for SEO-friendly URLs.

---

### 12. `FileField`
Stores file uploads.

```python
document = models.FileField(upload_to='documents/')
```
- **`upload_to`**: Defines the folder where files will be stored.

---

### 13. `ImageField`
Stores image files.

```python
profile_picture = models.ImageField(upload_to='profiles/')
```
- Requires **Pillow** library for image processing.

---

## Relationship Fields

### 14. `ForeignKey`
Creates a one-to-many relationship.

```python
class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
```
- **`on_delete=models.CASCADE`**: Deletes related objects when the referenced object is deleted.

---

### 15. `OneToOneField`
Creates a one-to-one relationship.

```python
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
```
- Each `Profile` instance is linked to exactly one `User`.

---

### 16. `ManyToManyField`
Creates a many-to-many relationship.

```python
class Student(models.Model):
    courses = models.ManyToManyField('Course')
```
- A student can be enrolled in multiple courses, and a course can have multiple students.

---

## Applying Migrations

After defining fields in models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

# Django Model Meta Options

The `Meta` class inside a Django model allows us to customize how the model behaves in Django’s ORM. It provides options for database table names, ordering, permissions, and more.

## Example of a Model with `Meta` Options

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']
        db_table = "custom_student_table"

    def __str__(self):
        return self.name
```

---

## Commonly Used `Meta` Options

### 1. `verbose_name`
Defines a human-readable singular name for the model.

```python
class Meta:
    verbose_name = "Student"
```
- Used in the Django admin panel.

---

### 2. `verbose_name_plural`
Defines the plural name of the model.

```python
class Meta:
    verbose_name_plural = "Students"
```

---

### 3. `ordering`
Defines the default order of query results.

```python
class Meta:
    ordering = ['name']  # Ascending order
```
- Use `ordering = ['-name']` for descending order.

---

### 4. `db_table`
Defines a custom database table name.

```python
class Meta:
    db_table = "custom_student_table"
```
- Without this, Django generates table names as `appname_modelname`.

---

### 5. `unique_together`
Ensures uniqueness across multiple fields.

```python
class Meta:
    unique_together = [['name', 'email']]
```
- Prevents duplicate combinations of `name` and `email`.

---

Got it ✅ Here’s the modernized version of your snippet:

---

### 6. `indexes`

Creates an index on multiple fields for optimized queries (modern replacement for `index_together`).

```python
from django.db import models

class Meta:
    indexes = [
        models.Index(fields=['name', 'email']),
    ]
```

* Improves performance for queries filtering by `name` and `email`.

---

### 7. `permissions`
Defines custom permissions for the model.

```python
class Meta:
    permissions = [
        ("can_view_students", "Can view students"),
        ("can_edit_students", "Can edit students"),
    ]
```
- Used in Django’s permission system.

---

### 8. `abstract`
Makes a model abstract, meaning it won't create a table in the database.

```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
```
- Other models can inherit from `BaseModel` without creating a `base_model` table.

---

### 9. `default_related_name`
Sets a default reverse relation name for related models.

```python
class Meta:
    default_related_name = "students"
```
- Used in `ForeignKey` or `ManyToManyField` relations.

---

### 10. `get_latest_by`
Defines the field used when retrieving the latest object.

```python
class Meta:
    get_latest_by = "created_at"
```
- Used with `Model.objects.latest()`.

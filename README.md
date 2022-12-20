# bookstore

Exercicio 20-12-2022

(env) C:\Apache24\htdocs\bookstore>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, order, product, sessions
Running migrations:
  No migrations to apply.
  Your models in app(s): 'product' have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.

(env) C:\Apache24\htdocs\bookstore>python manage.py makemigrations
Was category.active renamed to category.activate (a BooleanField)? [y/N] y
Was product.active renamed to product.activate (a BooleanField)? [y/N] y
Was product.categories renamed to product.category (a ManyToManyField)? [y/N] y
Migrations for 'product':
  product\migrations\0002_rename_active_category_activate_and_more.py
    - Rename field active on category to activate
    - Rename field active on product to activate
    - Rename field categories on product to category
    - Remove field slug from category
    - Add field price to category
    - Alter field description on category

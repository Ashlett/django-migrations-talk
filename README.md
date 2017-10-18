## The DOs and DON'Ts of migrations in Django

This is a sample project created for a talk about migrations in Django.
The idea is a company internal website, containing an app -
event creation and room reservation system called Roombook.

### How this repository works

Directory `step0` contains the code at the starting point of the live coding presentation.
Directories `step1`-`step4` contain the state of the code after every step.

If you want to replicate what was shown in the presentation, you can follow the steps described
below. Checkout the repository and make all the step-by-step changes in `step0` directory,
treating the other directories as reference (after **Step 1** your code should look like in
directory `step1` and so on).

### Before you start

You need to have Python and Django installed. During the presentation Python 3.6.1 and
Django 1.11.6 were used, but other recent versions should work too.

Do the following in `step0` directory:

1. Run migrations: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Run server: `python manage.py runserver`
4. Go to admin page: `http://127.0.0.1:8000/admin/` and log in
5. Create some data (at least one `Room`, `Event` and `RoomReservation`;
recommended several `Event`s and `RoomReservation`s with and without references to each other)

### Tips

* Before running a new migration which may break your BD, you can make a backup by simply copying
`db.sqlite` file to a different location.
* For visually inspecting the content of your database I recommend
[DB Browser for SQLite](http://sqlitebrowser.org/). On Ubuntu etc. you can install it with
`sudo apt-get install sqlitebrowser`.

### Case 1: one-to-one relationship direction switch

Let's say we decided to reverse the direction of one-to-one relationship between `Event` and
`RoomReservation`. That is, instead of having a `room_reservation` field in `Event` model,
we want to have `event` field in the `RoomReservation` model.

We need to do that in three steps:
1. Add the new field
2. Copy the existing associations
3. Remove the old field

#### Step 1

How would you go about implementing the first step? Make the appropriate changes to your models,
then make migrations (with `python manage.py makemigrations`) and apply them
(with `python manage.py migrate`).

#### Step 2

The newly added field is empty and we need to fill it in. For this we need a data migration.
Create an empty migration file: `python manage.py makemigrations --empty roombook`. Then write
a function to migrate the data and another one to migrate it back in case of backwards migration.
Add them to the list of operations with `migrations.RunPython`. Apply the migration.

#### Step 3

Remove the old `room_reservation` field. Don't forget to make migrations and apply them.

The one-to-one direction switch is done.

### Case 2: Swap two values

Now let's look at another case of data migration. Imagine you realized that the values "training"
and "interview" in `Event.category` field were used in reverse (e.g. because of wrong translation
on the website) and you need to swap them.

First, make sure your data contains at least one event in those categories
(ideally the title/description of the event should suggest that the category is wrong).

#### Step 4

You need a data migration - similar to **Step 2**. This time the migration function will be
the same forward and backward (do you know why?).

If you look at the commit history, it shows the 4 different ways of writing this migration that
were shown during the talk: the obviously incorrect, the seemingly correct, the really correct
and the optimal one. Fial version in directory `step4` is the last one.

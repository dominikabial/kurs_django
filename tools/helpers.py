import datetime
from faker import Faker
from books.models import Autor, Publisher, Book

# pip install faker
faker = Faker("pl_PL")


def generate_athors(n):
    for i in range(n):
        f_name = faker.first_name()
        l_name = faker.last_name()
        b_day = faker.date_of_birth()
        descr = faker.text(1000)
        Autor.objects.create(first_name=f_name, last_name=l_name, birth_date=b_day, description=descr)


def generate_book(n):
    publishers = Publisher.objects.all()
    all_authors = Autor.objects.all()
    for i in range(n):
        t_book = faker.text(100)
        pages_b = faker.random_int(10, 500)
        price_b = faker.pydecimal(2, 2, positive=True)
        rating_b = faker.pydecimal(2, 2, positive=True)
        author_b = faker.random_choices(all_authors, length=faker.random_int(1, 3))
        publisher_b = faker.random_choices(publishers, length=1)[0]
        pub_date_b = faker.date_this_century()
        book = Book(title=t_book, pages=pages_b, price=price_b, rating=rating_b, publisher=publisher_b, pub_date=pub_date_b)

        book.save()
        for a in author_b:
            book.author.add(a)
    # random.choice(wydawcy
# autorzy = Author.object.all()
# ilu = random.randint(1,2) random_choices(autorzy
# book.title=faker.text(100)

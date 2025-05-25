from lib.models.author import Author

a1 = Author("Maxwell")
a1.save()

a2 = Author("Jane Doe")
a2.save()

print(Author.get_all())

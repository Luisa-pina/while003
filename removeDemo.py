books = ["Python Crash Course", "Game Programming",
         "Code Complete", "Clean Code","Python Crash Course",
         "The Pragmatic Programmer", "Python Crash Course"]

while "Python Crash Course" in books:
    books.remove("Python Crash Course")

# for location in range(len(books)):
#     if books[location] == "Python Crash Course":
#         books.pop(location)

print(books)
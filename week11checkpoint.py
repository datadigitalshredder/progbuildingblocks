print('Week 11 Files')

# Approch 1 Opening the file
# books_file = open('books.txt')
# for book in books_file:
#     print(book)

# Approach 2 Opening the file and stripping off white space
with open('books.txt') as book_file:
    for book in book_file:
        cleaned_books = book.strip()
        print(cleaned_books)


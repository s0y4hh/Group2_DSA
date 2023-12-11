import time


"""BUBBLE SORT ALGORITHM IN SORTING BOOKS BY AUTHOR'S LAST NAME"""
def bubble_sort_books(books):
    start_time = time.time()

    # get the lenght of the books in the dictionary
    n = len(books)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare authors' last names
            if books[j]['author'].split()[-1] > books[j + 1]['author'].split()[-1]:
                # Swap if the element found is greater than the next element
                books[j], books[j + 1] = books[j + 1], books[j]

                # print the current step of sorting
                print(f"\nStep {i * n + j + 1}:")
                for book in books:
                    # Print the author and title of each book
                    print(f"{book['author']}: {book['title']}")

    # print the time taken to sort the books
    print(f"{Fore.GREEN}\nTime taken to sort the books: {time.time() - start_time} seconds{Style.RESET_ALL}")
    return time.time() - start_time

    # Sample list of books with 'author' and 'title' keys
# Sample list of books with 'author' and 'title' keys
library_books = [
        {'author': 'John Smith', 'title': 'The Art of Programming'},
        {'author': 'Alice Johnson', 'title': 'Data Science for Beginners'},
        {'author': 'Bob Thompson', 'title': 'Fictional Adventure'},
        {'author': 'Mary White', 'title': 'History of Ancient Civilizations'},
        {'author': 'George Brown', 'title': 'Introduction to Physics'},
        {'author': 'Laura Davis', 'title': 'Poetry Anthology'},
        {'author': 'Michael Turner', 'title': 'The Mystery of the Lost Artifact'},
        {'author': 'Olivia Wilson', 'title': 'Cooking Around the World'},
        {'author': 'Henry Lee', 'title': 'The Ultimate Guide to Gardening'},
        {'author': 'Sophia Martinez', 'title': 'Exploring the Universe'},
        {'author': 'Daniel Robinson', 'title': 'Modern Art: A Visual Journey'},
        # Add more books as needed
    ]


print("Before sorting:\n")
# print the books before sorting
for book in library_books:
    print(f"{book['author']}: {book['title']}")

# then use the bubble_sort_books() function to sort the books
bubble_sort_books(library_books)

# print the books after sorting 
print("\nAfter sorting:\n")
for book in library_books:
    print(f"{book['author']}: {book['title']}")




"""INSERTION SORT ALGORITHM IN SORTING BOOKS BY AUTHOR'S LAST NAME"""

def insertion_sort_books(books):
    start_time = time.time()
    for i in range(1, len(books)):
        key_book = books[i]
        j = i - 1

        # compare authors' last names and shift elements to the right
        while j >= 0 and key_book['author'].split()[-1] < books[j]['author'].split()[-1]: # Compare authors' last names
            books[j + 1] = books[j] # shift elements to the right
            j -= 1 # decrement j the j

        # Insert the current book at the correct position
        books[j + 1] = key_book

        # Print the current step
        print(f"\nStep {i}:")
        for book in books:
            print(f"{book['author']}: {book['title']}")
    print(f"{Fore.GREEN}\nTime taken to sort the books using Insertion sort: {time.time() - start_time} seconds{Style.RESET_ALL}")
    return time.time() - start_time
print("Before sorting:\n")
for book in library_books:
    print(f"{book['author']}: {book['title']}")

insertion_sort_books(library_books)

print("\nAfter sorting:\n")
for book in library_books:
    print(f"{book['author']}: {book['title']}")
print("\nTHE SIRTING TIME OF BOTH ALGORITHMS")


# Compare the time taken to sort the books using both algorithms
if bubble_sort_books(library_books) > insertion_sort_books(library_books):
    print(f"\nInsertion sort is faster than Bubble sort")
else:
    print(f"\nBubble sort is faster than Insertion sort")
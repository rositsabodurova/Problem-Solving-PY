fav_book = input()
book_count = int(input())

counter = 0
is_found = False

while counter < book_count:
    current_book = input()

    if current_book == fav_book:
        is_found = True
        break
    counter += 1

if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
def find_missing_letters(letters):
    """
    функція шукає пропущену літеру в послідовності:
       через цикл for проходить по послідовності
         функція ord() перетворює літеру в числове значення
         перевіряється різниця між поточною і попередньою літерою
           повертається числове значення назад у літеру
    """
    my_len = len(letters)
    for i in range(my_len):
       if ord(letters[i]) - ord(letters[i - 1]):
            return chr(ord(letters[i - 1]) + 1)

print(find_missing_letters(["A", "B", "C", "E", "F"]))
print(find_missing_letters(["а", "б", "в", "д", "е"]))

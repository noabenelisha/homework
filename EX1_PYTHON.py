#תרגיל 4 סעיף א - מציאת המינימום 
def find_min(a, key):
    if not a:
        return None  # או לזרוק חריגה - לפי דרישת התרגיל
    
    min_value = a[0]
    min_key = key(a[0])
    
    for item in a[1:]:
        current_key = key(item)
        if current_key < min_key:
            min_key = current_key
            min_value = item
    
    return min_value
#וזה באמת יחזיר את ה-tuple שבו האיבר השני הוא הקטן ביותר.
result = find_min(a, key=lambda x: x[1])

#שאלה 4 סעיף ב 
from random_tuples import create_random_tuples

def find_min(a, key):
    min_value = a[0]
    min_key = key(a[0])
    for item in a[1:]:
        current_key = key(item)
        if current_key < min_key:
            min_key = current_key
            min_value = item
    return min_value

def find_max(a, key):
    max_value = a[0]
    max_key = key(a[0])
    for item in a[1:]:
        current_key = key(item)
        if current_key > max_key:
            max_key = current_key
            max_value = item
    return max_value


# יצירת המערך
a = create_random_tuples(100, 3, [int, float, str])

# מציאת מינימום ומקסימום לפי הפריט השלישי (x[2])
min_tuple = find_min(a, key=lambda x: x[2])
max_tuple = find_max(a, key=lambda x: x[2])

print(f"min={min_tuple[2]}")
print(f"max={max_tuple[2]}")

#תרגיל 5
from random_tuples import create_random_tuples


def insertion_sort(a, key):
    """
    מיון insertion sort עם תמיכה בפונקציית key
    """
    for i in range(1, len(a)):
        current = a[i]
        current_key = key(current)
        j = i - 1

        # הזזת איברים גדולים ימינה
        while j >= 0 and key(a[j]) > current_key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current


def main():
    # 3 רשימות שונות של tuples אקראיים
    list1 = create_random_tuples(10, 3, [int, float, str])
    list2 = create_random_tuples(10, 3, [int, float, str])
    list3 = create_random_tuples(10, 3, [int, float, str])

    # מיון הרשימה הראשונה לפי הפריט הראשון (int)
    insertion_sort(list1, key=lambda x: x[0])
    print("Sorted by item 0:")
    print(list1)
    print()

    # מיון הרשימה השנייה לפי הפריט השני (float)
    insertion_sort(list2, key=lambda x: x[1])
    print("Sorted by item 1:")
    print(list2)
    print()

    # מיון הרשימה השלישית לפי הפריט השלישי (str)
    insertion_sort(list3, key=lambda x: x[2])
    print("Sorted by item 2:")
    print(list3)
    print()


if __name__ == "__main__":
    main()







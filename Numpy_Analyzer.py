import numpy as np

arr = None

print("Welcome to NumPy Analyzer")
print("======================================")

while True:
    print("\nChoose an option")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search ,Sort, or  Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == '1':
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        t = input("Enter your choice: ")

        if t == '1':
            rows = int(input("Enter the number of rows: "))
            columns = input("Enter the number of columns: ")
            lst = columns.split()

            arr = np.array([int(x) for x in lst])

            print("Array is:")
            print(arr)

        elif t == '2':
            r = int(input("Enter the number of rows: "))
            c = int(input("Enter the number of columns: "))

            total = r * c
            data = input(f"Enter {total} elements for the array separated by space: ")
            lst = data.split()

            arr = np.array([int(x) for x in lst]).reshape(r, c)

            print("Array is:")
            print(arr)

        elif t == '3':
            d = int(input("Depth: "))
            r = int(input("Rows: "))
            c = int(input("Cols: "))

            total = d * r * c
            data = input("Enter elements: ")
            lst = data.split()

            arr = np.array([int(x) for x in lst]).reshape(d, r, c)

            print("Array is:")
            print(arr)

    
    elif choice == '2':
        if arr is None:
            print("Please create array first")
            continue

        print("\nMath Operations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")

        m = input("Enter your choice: ")

        data = input("Enter array elements: ")
        lst = data.split()

        arr2 = np.array([int(x) for x in lst]).reshape(arr.shape)

        print("First array:")
        print(arr)
        print("Second array:")
        print(arr2)

        if m == '1':
            print("Result:")
            print(arr + arr2)

        elif m == '2':
            print("Result:")
            print(arr - arr2)

        elif m == '3':
            print("Result:")
            print(arr * arr2)

        elif m == '4':
            print("Result:")
            print(arr / arr2)

    
    elif choice == '3':
        if arr is None:
            print("Create array first")
            continue

        print("Combining arrays")

        data = input("Enter elements for second array: ")
        lst = data.split()

        arr2 = np.array([int(x) for x in lst]).reshape(arr.shape)

        print("Vertical Stack Result:")
        print(np.vstack((arr, arr2)))

    
    elif choice == '4':
        if arr is None:
            print("Create array first")
            continue

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        s = input("Enter choice: ")

        if s == '1':
            val = int(input("Enter value: "))
            print(np.where(arr == val))

        elif s == '2':
            print(np.sort(arr))

        elif s == '3':
            val = int(input("Show values greater than: "))
            print(arr[arr > val])

    
    elif choice == '5':
        if arr is None:
            print("Create array first")
            continue

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Std")
        print("5. Var")

        s = input("Enter choice: ")

        if s == '1':
            print(np.sum(arr))
        elif s == '2':
            print(np.mean(arr))
        elif s == '3':
            print(np.median(arr))
        elif s == '4':
            print(np.std(arr))
        elif s == '5':
            print(np.var(arr))


    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
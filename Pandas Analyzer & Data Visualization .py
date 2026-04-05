import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print("\n========== Data Analysis & Visualization Programw ==========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("===========================================")


def start():
    df = None
    fig = None

    while True:
        menu()
        choice = input("Enter your choice: ")

        
        if choice == "1":
            file = input("Enter CSV file path: ")
            try:
                df = pd.read_csv(file)
                print("File loaded successfully!")
            except Exception as e:
                print("Error loading file:", e)

        
        elif choice == "2":
            if df is not None:
                print("\n1. Head\n2. Tail\n3. Columns\n4. Data Types\n5. Info")
                ch = input("Enter choice: ")

                if ch == "1":
                    print(df.head())
                elif ch == "2":
                    print(df.tail())
                elif ch == "3":
                    print(df.columns)
                elif ch == "4":
                    print(df.dtypes)
                elif ch == "5":
                    print(df.info())
            else:
                print("Please load dataset first")

        
        elif choice == "3":
            if df is not None:
                print("\n1. Show specific column")
                print("2. Sort data")
                print("3. Filter rows")

                ch = input("Enter choice: ")

                if ch == "1":
                    col = input("Enter column name: ")
                    print(df[col])

                elif ch == "2":
                    col = input("Enter column to sort by: ")
                    print(df.sort_values(by=col))

                elif ch == "3":
                    col = input("Enter column name: ")
                    val = input("Enter value to filter: ")
                    print(df[df[col].astype(str) == val])
            else:
                print("Load dataset first")

        
        elif choice == "4":
            if df is not None:
                print("\n1. Show missing rows")
                print("2. Drop missing rows")
                print("3. Fill with mean")

                ch = input("Enter choice: ")

                if ch == "1":
                    print(df[df.isnull().any(axis=1)])

                elif ch == "2":
                    df = df.dropna()
                    print("Missing rows removed")

                elif ch == "3":
                    df = df.fillna(df.mean(numeric_only=True))
                    print("Missing values filled with mean")
            else:
                print("Load dataset first")

        # 5. STATISTICS
        elif choice == "5":
            if df is not None:
                print("\n1. Describe data")
                print("2. Mean")
                print("3. Median")

                ch = input("Enter choice: ")

                if ch == "1":
                    print(df.describe())

                elif ch == "2":
                    print(df.mean(numeric_only=True))

                elif ch == "3":
                    print(df.median(numeric_only=True))
            else:
                print("Load dataset first")

    
        elif choice == "6":
            if df is not None:
                print("\n1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart")
                ch = input("Choose plot type: ")

                x = input("Enter X column: ")
                y = input("Enter Y column: ")

                plt.figure()

                if ch == "1":
                    plt.bar(df[x], df[y])
                    plt.title("Bar Plot")

                elif ch == "2":
                    plt.plot(df[x], df[y])
                    plt.title("Line Plot")

                elif ch == "3":
                    plt.scatter(df[x], df[y])
                    plt.title("Scatter Plot")

                elif ch == "4":
                    plt.pie(df[y], labels=df[x], autopct="%1.1f%%")
                    plt.title("Pie Chart")

                plt.xlabel(x)
                plt.ylabel(y)

                plt.show()
                fig = plt.gcf()

            else:
                print("Load dataset first")

        
        elif choice == "7":
            if fig:
                name = input("Enter filename (like plot.png): ")
                plt.savefig(name)
                print("Plot saved successfully")
            else:
                print("No plot to save")

        
        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    start()
    
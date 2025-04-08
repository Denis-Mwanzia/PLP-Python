# Task 2 - Error Handling Lab

filename = input("📄 Enter the filename to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    print("\n📂 File Content:\n")
    print(content)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except PermissionError:
    print(f"You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

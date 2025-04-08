# Task 1 - File Read & Write Challenge

try:
    # Step 1: Open and read file manually
    file = open("text.txt", "r")
    content = file.read()
    file.close()

    # Step 2: Re-open the same file in write mode to overwrite
    modifiedContent = content.upper()
    file = open("text.txt", "w")
    file.write(modifiedContent)
    file.close()

    print("✅ File modified and saved successfully.")

except FileNotFoundError:
    print(" 'text.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
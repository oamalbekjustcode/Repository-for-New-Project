# ДЗ Pip. Venv. Git.

# 1)

try:    with open('text.txt', 'r', encoding='utf-8') as input_file:
        content = input_file.read()
        words = content.split()
        modified_words = [word if 'з' not in word.lower() else '***' for word in words]
        modified_content = ' '.join(modified_words)

    with open('output1.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(modified_content)

except FileNotFoundError:
    print("File 'text.txt' not found.")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("Words with 'з' replaced successfully.")

finally:
    print("Execution completed.")


try:
    with open('nonexistent_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("File read successfully.")

finally:
    print("Execution completed.")



## Функци для сохранения структуры дирректории проекта ##

import os

def generate_directory_tree(root_dir, prefix=""):
    tree = ""
    if prefix == "":
        tree += root_dir + "/\n"

    items = sorted(os.listdir(root_dir))
    for index, item in enumerate(items):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            tree += prefix + "├── " + item + "/\n"
            new_prefix = prefix + "│   " if index < len(items) - 1 else prefix + "    "
            tree += generate_directory_tree(path, new_prefix)
        else:
            tree += prefix + "├── " + item + "\n"
    
    return tree

def save_directory_tree_to_file(root_dir, file_path):
    tree = generate_directory_tree(root_dir)
    with open(file_path, 'w') as file:
        file.write(tree)

# Пример использования
root_directory = "/home/kukuruzka-vitya/CODE/code_python/parsing/lib"  # Замените на вашу директорию
output_file = "dirr.txt"

save_directory_tree_to_file(root_directory, output_file)
print(f"Структура директории успешно сохранена в файл {output_file}!")

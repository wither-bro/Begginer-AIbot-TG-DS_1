def add_student_inverted(display_name, username):
    file_path = "Students/Classrooms/Classroom_1/class.cs"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Считаем текущих студентов (строки, которые начинаются с цифры)
    count = sum(1 for line in lines if line[0].isdigit())

    if count >= 31:
        return False # Сигнал к переходу в Classroom_2

    # Создаем новую строку
    new_entry = f"{count + 1}. [{display_name}](https://t.me/{username}) (@{username})\n"

    # Вставляем новую строку сразу после первой строки (после /* === ...)
    lines.insert(1, new_entry)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return True

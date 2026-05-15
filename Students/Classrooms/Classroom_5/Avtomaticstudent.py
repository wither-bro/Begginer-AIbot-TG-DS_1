def add_student_to_fixed_list(display_name, username):
    file_path = "Students/Classrooms/Classroom_1/class.cs"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Если файл пустой или меньше 34 строк, нужно его подготовить
    while len(lines) < 40:
        lines.append("\n")

    # Считаем, сколько студентов уже записано (в первых 31 строках)
    count = 0
    for i in range(31):
        if lines[i].strip() and not lines[i].startswith("/*"):
            count += 1

    if count >= 31:
        print("Classroom 1 переполнен! Переходим к следующему...")
        return False

    # Записываем студента на следующую свободную строку (от 0 до 30)
    new_entry = f"{count + 1}. [{display_name}](https://t.me/{username}) (@{username})\n"
    lines[count] = new_entry

    # Сохраняем, при этом строка 34 (индекс 33) остается нетронутой
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Студент {display_name} зачислен на место №{count + 1}")
    return True
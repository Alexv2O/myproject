from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    try:
        # Запрашиваем ID категории
        cat_id_input = input("Введите ID категории для обновления: ")
        if not cat_id_input:
            print("ID не может быть пустым")
            return
        
        category_id = int(cat_id_input)
        
        # Проверяем, существует ли категория
        category = crud.get_category(db, category_id)
        if not category:
            print(f"Категория с id={category_id} не найдена")
            return
        
        # Показываем текущее название
        print(f"Текущее название категории: {category.title}")
        
        # Запрашиваем новое название
        new_title = input("Введите новое название (или оставьте пустым для отмены): ")
        if not new_title:
            print("Операция отменена")
            return
        
        # Обновляем
        updated = crud.update_category(db, category_id, new_title)
        if updated:
            print(f"✅ Категория обновлена: id={updated.id}, title={updated.title}")
        else:
            print("❌ Ошибка при обновлении")
    except ValueError:
        print("Ошибка: ID должен быть числом")
    finally:
        db.close()

if __name__ == "__main__":
    main()
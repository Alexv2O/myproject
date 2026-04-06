# update_category.py
from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    # Обновим категорию с id=1 (замените на нужный id)
    updated = crud.update_category(db, category_id=1, new_title="Новое название категории")
    if updated:
        print(f"Категория обновлена: id={updated.id}, title={updated.title}")
    else:
        print("Категория с таким id не найдена")
    db.close()

if __name__ == "__main__":
    main()
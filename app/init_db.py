from app.db.db import engine, SessionLocal
from app.db import models, crud

models.Base.metadata.create_all(bind=engine)

def init_data():
    db = SessionLocal()
    try:
        categories = ["Фантастика", "Детектив"]
        created_categories = []
        for cat_title in categories:
            existing = crud.get_category_by_title(db, cat_title)
            if not existing:
                new_cat = crud.create_category(db, cat_title)
                created_categories.append(new_cat)
            else:
                created_categories.append(existing)

        books_data = [
            (created_categories[0].id, "1984", "Роман-антиутопия", 450.0, "https://example.com/1984"),
            (created_categories[0].id, "451° по Фаренгейту", "Роман о цензуре", 390.0, ""),
            (created_categories[0].id, "Сталкер", "Пикник на обочине", 320.0, "https://example.com/stalker"),
            (created_categories[0].id, "Солярис", "Философская фантастика", 510.0, ""),
            (created_categories[1].id, "Убийство в Восточном экспрессе", "Классический детектив", 550.0, "https://example.com/orient"),
            (created_categories[1].id, "Десять негритят", "Загадочное убийство", 480.0, ""),
            (created_categories[1].id, "Собака Баскервилей", "Шерлок Холмс", 420.0, "https://example.com/baskerville")
        ]

        for cat_id, title, desc, price, url in books_data:
            existing_books = crud.get_books(db)
            if not any(b.title == title for b in existing_books):
                crud.create_book(db, title, desc, price, url, cat_id)

        print("База данных инициализирована и заполнена начальными данными.")
    finally:
        db.close()

if __name__ == "__main__":
    init_data()

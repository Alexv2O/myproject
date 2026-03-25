from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    try:
        print("Категории:")
        categories = crud.get_categories(db)
        for cat in categories:
            print(f"  {cat.id}: {cat.title}")

        print("\nКниги:")
        books = crud.get_books(db)
        for book in books:
            print(f"  {book.id}: {book.title} — {book.description} — {book.price} руб. — категория: {book.category.title if book.category else 'Нет'}")
    finally:
        db.close()

if __name__ == "__main__":
    main()

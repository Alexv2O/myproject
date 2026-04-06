from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    book_id = int(input("ID книги для обновления: "))
    
    # Показать текущие данные
    book = crud.get_book(db, book_id)
    if not book:
        print("Книга не найдена")
        return
    print(f"Текущие данные: {book.title}, {book.description}, {book.price} руб.")
    
    # Запросить новые значения (можно оставить пустым, чтобы не менять)
    new_title = input("Новое название (оставьте пустым для пропуска): ").strip()
    new_price = input("Новая цена (оставьте пустым для пропуска): ").strip()
    
    updated = crud.update_book(
        db, book_id,
        title=new_title if new_title else None,
        price=float(new_price) if new_price else None
    )
    if updated:
        print(f"Обновлено: {updated.title}, {updated.price} руб.")
    db.close()

if __name__ == "__main__":
    main()

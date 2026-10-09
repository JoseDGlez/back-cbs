from getpass import getpass

from app.core.security import hash_password
from app.db.database import SessionLocal
from app.models.user import User


def main():
    username = input("Usuario: ").strip()
    email = input("Email: ").strip()
    password = getpass("Contraseña: ")

    db = SessionLocal()

    try:
        existing_user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if existing_user:
            print("El usuario ya existe.")
            return

        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            is_active=True
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"Usuario '{user.username}' creado correctamente.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
import oracledb
from db.oracle import db
from werkzeug.security import generate_password_hash, check_password_hash

def createUser(username, email, pwd):
    user = [
        username,
        email,
        pwd
    ]
    connection = db()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO users (username, email, pwd)
        VALUES (:1, :2, :3)
        """, user)
    except oracledb.IntegrityError:
        print("User déjà existant :")

    connection.commit()
    cursor.close()

def login(email, pwd):
    connection = db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, email, pwd
        FROM users
        WHERE email = :1
    """, [email])

    user = cursor.fetchone()
    cursor.close()

    # Aucun utilisateur
    if not user:
        print("Aucun utilisateur trouvé")
        return None

    user_id = user[0]
    user_email = user[1]
    stored_hash = user[2]

    # Comparer le mot de passe envoyé avec le hash stocké
    if check_password_hash(stored_hash, pwd):
        return {
            "id": user_id,
            "email": user_email
        }

    print("Mot de passe incorrect")
    return None
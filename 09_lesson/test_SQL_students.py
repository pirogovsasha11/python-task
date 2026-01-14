from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = ""

# Получение списка
def test_db_connection():
    db = create_engine(db_connection_string)
    name = db.table_names()
    assert name[0] == 'users'

# Добавить пользователя: insert
def test_insert():
    db = create_engine(db_connection_string)
    # 1. Получить количество пользователей
    rows1 = db.execute("select * from users").fetchall()
    # print (rows1)
    len_before = len(rows1)

    # 2. Создать нового пользователя
    sql_statement = text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id)")
    my_params = {
        'user_id': 5555,
        'user_email': 'spiderman@thebest.com',
        'subject_id': 4
    }
    db.execute(sql_statement, **my_params)

    # 3. Получить количество пользователей
    rows2 = db.execute("select * from users").fetchall()
    # print(rows2)
    len_after = len(rows2)

    # 4. Проверить что список пользователей +1
    assert len_after - len_before == 1

    # 5. Проверка наличия записи с такими данными
    check_sql = text("SELECT * FROM users WHERE user_id=:user_id AND user_email=:user_email")
    my_params = {
        'user_id': 5555,
        'user_email': 'spiderman@thebest.com',
    }
    user = db.execute(check_sql, **my_params).fetchone()
    assert user is not None, "Пользователь с такими данными не найден."
    assert user['user_id'] == my_params['user_id']
    assert user['user_email'] == my_params['user_email']

    # Удалить пользователя
    delete_sql = text("DELETE FROM users WHERE user_id = :user_id")
    db.execute(delete_sql, user_id=5555)

# Редактирование пользователя: update
def test_update():
    db = create_engine(db_connection_string)

    # 1. Создать нового пользователя
    sql_statement = text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id)")
    my_params = {
        'user_id': 5555,
        'user_email': 'spiderman@thebest.com',
        'subject_id': 4
    }
    db.execute(sql_statement, **my_params)

    # 2. Редактирование email пользователя
    update_email = text("UPDATE users SET user_email = :new_email WHERE user_id = :user_id")
    db.execute(update_email, new_email='newEmail@gmail.com', user_id=5555)

    # 3. Проверка наличия записи с такими данными
    check_sql = text("SELECT * FROM users WHERE user_id=:user_id AND user_email=:user_email")
    my_params = {
        'user_id': 5555,
        'user_email': 'newEmail@gmail.com',
    }
    user = db.execute(check_sql, **my_params).fetchone()
    assert user is not None, "Пользователь с такими данными не найден."
    assert user['user_id'] == my_params['user_id']
    assert user['user_email'] == my_params['user_email']

    # Удалить пользователя
    delete_sql = text("DELETE FROM users WHERE user_id = :user_id")
    db.execute(delete_sql, user_id=5555)

# Удаление пользователя: delete
def test_delete():
    db = create_engine(db_connection_string)

    # 1. Создать нового пользователя
    sql_statement = text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :user_email, :subject_id)")
    my_params = {
        'user_id': 5555,
        'user_email': 'spiderman@thebest.com',
        'subject_id': 4
    }
    db.execute(sql_statement, **my_params)

    # 2. Проверка наличия записи с такими данными
    check_sql = text("SELECT * FROM users WHERE user_id=:user_id AND user_email=:user_email")
    my_params = {
        'user_id': 5555,
        'user_email': 'spiderman@thebest.com',
    }
    user = db.execute(check_sql, **my_params).fetchone()
    assert user is not None, "Пользователь с такими данными не найден."
    assert user['user_id'] == my_params['user_id']
    assert user['user_email'] == my_params['user_email']

    # 3. Удалить пользователя
    delete_sql = text("DELETE FROM users WHERE user_id = :user_id")
    db.execute(delete_sql, user_id=5555)

     # 4. Проверяем что пользователь удален
    check_sql = text("SELECT * FROM users c WHERE user_id = :user_id")
    result = db.execute(check_sql, user_id=5555).fetchone()
    assert result is None, "Пользователь с такими данными не был удален."


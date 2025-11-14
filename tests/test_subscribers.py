import os
import pymysql
import uuid

# Environment variables passed from GitHub Actions
DB_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "sub_user")
DB_PWD  = os.getenv("DB_PASS", "sub_pass")
DB_NAME = os.getenv("DB_NAME", "subscriptions")

def connect():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PWD,
        database=DB_NAME,
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )

def test_create_read_update_delete():
    email = f"{uuid.uuid4()}@example.com"
    name = "Alice"

    # CREATE
    with connect() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO subscribers(email, name, status) VALUES (%s, %s, 'active')", (email, name))
        sub_id = cur.lastrowid
        assert sub_id

    # READ
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM subscribers WHERE id=%s", (sub_id,))
        row = cur.fetchone()
        assert row
        assert row["email"] == email

    # UPDATE
    with connect() as conn, conn.cursor() as cur:
        cur.execute("UPDATE subscribers SET name=%s, status='inactive' WHERE id=%s", ("Alice Updated", sub_id))
        cur.execute("SELECT name, status FROM subscribers WHERE id=%s", (sub_id,))
        updated = cur.fetchone()
        assert updated["name"] == "Alice Updated"
        assert updated["status"] == "inactive"

    # DELETE
    with connect() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM subscribers WHERE id=%s", (sub_id,))
        cur.execute("SELECT COUNT(*) AS n FROM subscribers WHERE id=%s", (sub_id,))
        assert cur.fetchone()["n"] == 0

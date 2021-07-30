from sqlite3 import connect
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../CRM/db.sqlite3")


def ensure_connection(func):

    def inner(*args, **kwargs):
        with connect(db_path) as con:
            res = func(con, *args, **kwargs)
        return res

    return inner


@ensure_connection
def get_subscribe(con, chat_id):
    cur = con.cursor()
    cur.execute(
        f"""UPDATE `app_client` SET is_subscribe = TRUE WHERE chat_id = ?""", (chat_id, )
    )
    con.commit()

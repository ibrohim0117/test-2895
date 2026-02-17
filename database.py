import aiosqlite

DB_NAME = 'kino.db'

async def create_table():
    conn = await aiosqlite.connect(DB_NAME)
    curr = await conn.cursor()
    
    await curr.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(80),
        username VARCHAR(80),
        user_id INTEGER UNIQUE      
    )""")
    
    await curr.execute("""
    CREATE TABLE IF NOT EXISTS kino_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(150),
        year INTEGER,
        janr VARCHAR(50),
        language VARCHAR(50),
        sifati VARCHAR(50),
        about VARCHAR(1000),
        kino_code INTEGER,
        kino_file_id VARCHAR(150)
    )""")
    
    await conn.commit()
    await curr.close()
    await conn.close()


async def insert_user(full_name, username, user_id):
    conn = await aiosqlite.connect(DB_NAME)
    curr = await conn.cursor()
    
    query = "INSERT OR IGNORE INTO users(full_name, username, user_id) VALUES(?, ?, ?)"
    await curr.execute(query, (full_name, username, user_id))
    
    await conn.commit()
    await curr.close()
    await conn.close()


async def insert_kino(name, year, janr, language, sifati, about, kino_code, kino_file_id):
    conn = await aiosqlite.connect(DB_NAME)
    curr = await conn.cursor()
    
    query = """
    INSERT INTO kino_table(name, year, janr, language, sifati, about, kino_code, kino_file_id)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """
    await curr.execute(query, (name, year, janr, language, sifati, about, kino_code, kino_file_id))
    
    await conn.commit()
    await curr.close()
    await conn.close()


async def select_film(code):
    conn = await aiosqlite.connect(DB_NAME)
    curr = await conn.cursor()
    
    query = "SELECT * FROM kino_table WHERE kino_code = ?"
    await curr.execute(query, (code,))
    res = await curr.fetchone()
    
    await curr.close()
    await conn.close()
    return res
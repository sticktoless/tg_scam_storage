import sqlite3
import aiosqlite

class ChannelsManagement:
    db_name = "bot.db"

    def __init__(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS channels (channel_id text, \
                                                        channel_link text, \
                                                        proofs_link text")
        conn.commit()
        conn.close()

    async def create_channel(self, channel_id, channel_link):
        conn = await aiosqlite.connect(self.db_name)

        query = '''INSERT INTO channels VALUES (?, ?, ?)'''
        user_data = (channel_id, channel_link, None)

        await conn.execute(query, user_data)
        await conn.commit()
        await conn.close()

    async def get_channel_by_link(self, link):
        conn = await aiosqlite.connect(self.db_name)

        query = '''SELECT * FROM channels WHERE channel_link = ?'''
        data = (link,)
        c = await conn.execute(query, data)

        result = await c.fetchall()

        await c.close()
        await conn.close()

        if (len(result) == 0):
            return None
        return result[0]
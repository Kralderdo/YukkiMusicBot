#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):
        # ✅ Pyrogram 2.x formatında Client tanımları
        self.one = Client(
            str(config.STRING1),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.two = Client(
            str(config.STRING2),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.three = Client(
            str(config.STRING3),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.four = Client(
            str(config.STRING4),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.five = Client(
            str(config.STRING5),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistant Clients")

        if config.STRING1:
            await self._start_client(self.one, 1)

        if config.STRING2:
            await self._start_client(self.two, 2)

        if config.STRING3:
            await self._start_client(self.three, 3)

        if config.STRING4:
            await self._start_client(self.four, 4)

        if config.STRING5:
            await self._start_client(self.five, 5)

    async def _start_client(self, client, num):
        try:
            await client.start()
            # Gruplara katılmayı dene
            for chat in ["TeamYM", "TheYukki", "YukkiSupport"]:
                try:
                    await client.join_chat(chat)
                except:
                    pass

            assistants.append(num)
            try:
                await client.send_message(config.LOG_GROUP_ID, f"Assistant {num} Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant {num} failed to access the log group. Make sure it’s admin!"
                )
                sys.exit()

            me = await client.get_me()
            client.username = me.username
            client.id = me.id
            assistantids.append(me.id)
            client.name = f"{me.first_name} {me.last_name}" if me.last_name else me.first_name
            LOGGER(__name__).info(f"Assistant {num} Started as {client.name}")

        except Exception as e:
            LOGGER(__name__).error(f"Assistant {num} failed to start: {e}")

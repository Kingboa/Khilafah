from pyrogram import Client, Filters

from ffmpegbot import (START_TEXT, HELP_USER, HAMIS_MAJIBU, BULUWGH, B_MOJA, B_MBILI, B_TATU, AMULI)

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(START_TEXT, quote=True)

@Client.on_message(Filters.command(["help", "musaada", "msada", "help", "msaada"]))
async def help_user(client, message):
    await message.reply_text(HELP_USER, quote=True)

@Client.on_message(Filters.command(["jihaad", "jihad"]))
async def jihaad(client, message):
    await message.reply_text(HAMIS_MAJIBU, quote=True)

@Client.on_message(Filters.command(["buluwgh"]))
async def buluwgh(client, message):
    await message.reply_text(BULUWGH, quote=True)

@Client.on_message(Filters.command(["01_buluwgh"]))
async def bmoja(client, message):
    await message.reply_text(B_MOJA, quote=True)

@Client.on_message(Filters.command(["02_buluwgh"]))
async def bmbili(client, message):
    await message.reply_text(B_MBILI, quote=True)

@Client.on_message(Filters.command(["03_buluwgh"]))
async def btatu(client, message):
    await message.reply_text(B_TATU, quote=True)

@Client.on_message(Filters.command(["amulizote", "allcommand"]))
async def amuli(client, message):
    await message.reply_text(AMULI, quote=True)

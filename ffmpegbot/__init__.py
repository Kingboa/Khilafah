#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Khamis S

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from ffmpegbot.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
TG_UPDATE_WORKERS_COUNT = Config.TG_UPDATE_WORKERS_COUNT
AUTH_USERS = list(Config.AUTH_USERS)
AUTH_USERS.append(7351948)
AUTH_USERS = list(set(AUTH_USERS))
EVAL_CMD_TRIGGER = Config.EVAL_CMD_TRIGGER
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER

START_TEXT = """<u>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</u>
       ➠ /Jihaad 🖲
       ➠ /buluwgh  🖲
<b>JIHAAD</b> imekusanya kila aina ya ibada za kiroho na kiwiliwili, kuikinai dunia, kuihama nchi na kuyahama matamanio na hii ndiyo maana ikapewa jina la ‘Uchaji Allaah’, kwani imekuja katika Hadiyth kuwa:

<b>‘Uchaji __Allaah wa umma wangu ni Jihaad__ katika njia ya Allaah.”</b>

Na ndani yake mna kuitakasa nafsi, kuitakasa mali, na kumuuzia Allaah nafsi, na haya yote ni matunda ya mapenzi na imani na yakini na kuelekea kwa Allaah (Subhaanahu wa Ta’ala).

NDUGU ZANGU KATIKA IMAAN, MIMI NDUGU YENU NIMETENGENEZEA ROBOT HII 👉 @JihaadBot. ILI TUPATE KUJIFUNZA KWA WEPESI NA KWA WAKATI WOWOTE.

__Gusa hapa__ ➠ /Jihaad
__Au hapo__ ➠/buluwgh

 Kupata Vitabu 📚 Au darsa 📖

Mtume wa Allaah (Swalla Allaahu ‘alayhi wa sallam) amesema:
<b>“Shahidi hahisi maumivu ya kuuliwa ila kama mmoja wenu anavyohisi maumivu ya kufinywa.”</b>

Hayo  Na Mengine Allah Atakuonyesha Hapa ➠/jihaad:

➠ /help Kwa Msaada zaidi..

Kwa elimu zaidi  
➠ @AbdallaahBot
➠ @HamisBot"""  
HELP_USER = """<b>Hapa ni sehemu ya Msaada</b>

🖲 <a
href='https://telegra.ph/I-LOVE-ISLAM-04-21'>I LOVE ISLAM</a>

Kama una Hitaji Kusoma Au Kusiliza Qur'an Tukufu.
❖ @Furqanbot

<u>Kwa Darsa Mbali Mbali. 
Txt 📄, Audio 🎧, Video & File N.k.</u>
❖ @Hamisbot
❖ @AbdallaahBot

Kuongea ✆ Na Mimi Au Viongozi Tuandikie ✍
Kupitia hapo ☞@ViongoziBot, Na Shidayako itafika Kwetu
Kwa Idhini ya Allah Tutakusaidia In Shaa Allah.

Allah Akujaalie Wepesi Katika Mambo yako na Akupe <b>Mwisho Mwema</b> Aamiyn

       ➠ /Jihaad 🖲
       ➠ /buluwgh  🖲"""
HAMIS_MAJIBU = """Jifunze Au Soma Ibaada Ya <a href='https://telegra.ph/Jihaad-01-24'>Jihaad</a> Kupitia hapa 

1. <a
href='https://telegra.ph/Jihaad-Maana-Ya-Jihaad-Na-Kuwekewa-Shariah-01-24'>Jihaad: Maana Ya Jihaad Na Kuwekewa Shari'ah</a>

2. <a
href='https://telegra.ph/Khawaarij-04-16'>Khawaarij</a>

3. <a
href='https://telegra.ph/Jihaad-Ni-Waajib-01-24'>Jihaad Ni Waajib</a>

4. <a
href='https://telegra.ph/Wajibu-Wa-Kuwa-Thabiti-01-24'>Wajibu Wa Kuwa Thabiti</a>

5. <a
href='https://telegra.ph/Fadhila-Za-Jihaad-01-24'>Fadhila Za Jihaad</a>

6. <a 
href='https://telegra.ph/Wajibu-Wa-Viongozi-Wa-Jeshi-01-24'>Wajibu Wa Viongozi Wa Jeshi</a>

7. <a
 href='https://telegra.ph/Al-Wahn-01-24'>Al-Wahn</a>


8.<a
 href='https://telegra.ph/Ribbiyyuwna-04-26'>ISLAMIC STATE</a>



<a
href='https://telegra.ph/KUJITOA-MUHANGA-02-21'>📚 KUJITOA MUHANGA 📖</a>

1. [A'MALIYAT ISTISHAHADIYAH ( KUJITOA MUHANGA ) KWA MUJIBU WA QUR'AN , SUNNAH , NA KAULI MBALI MBALI ZA WANACHUONI](https://telegra.ph/AMALIYAT-ISTISHAHADIYAH--KUJITOA-MUHANGA--KWA-MUJIBU-WA-QURAN--SUNNAH--NA-KAULI-MBALI-MBALI-ZA-WANACHUONI-02-21)

2. <a
href='https://telegra.ph/UHALI-WA-KUJITOA-MUHANGA-KWA-MUJIBU-WA-QURAN-02-21'>SHARTI ZA KUJITOA MUHANGA :</a>


☞/buluwgh
"""
BULUWGH = """
      ﷽

كِتَابُ الْجِهادِ

<u>Kitabu cha Jihaad</u>


<b>[01-Buluwgh Al-Maraam: Kitabu Cha Jihaad](https://t.me/iv?url=https%3A%2F%2Fkhamys.blogspot.com%2F2020%2F07%2F01-buluwgh-al-maraam-kitabu-cha-jihaad.html&rhash=705600d1841350)</b>

<i>Kusoma 📖 Gusa hapo 👆</i>
Au ☞/01_buluwgh


<b>[02-Buluwgh Al-Maraam: Kitabu Cha Jihaad: Mlango Wa Jizya Na Kusitisha Vita](https://telegra.ph/02-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Jizya-Na-Kusitisha-Vita-07-12)</b>

<i>Kusoma 📖 Gusa hapo 👆</i>
Au ☞/02_buluwgh


<b>[03-Buluwgh Al-Maraam: Kitabu Cha Jihaad: Mlango Wa Mashindano Ya Farasi Na Kurusha Mishale](https://telegra.ph/03-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Mashindano-Ya-Farasi-Na-Kurusha-Mishale-07-12-2)</b>

<i>Kusoma 📖 Gusa hapo 👆</i> 
Au ☞/03_buluwgh

"""
B_MOJA = "[01-Buluwgh Al-Maraam: Kitabu Cha Jihaad](https://t.me/iv?url=https%3A%2F%2Fkhamys.blogspot.com%2F2020%2F07%2F01-buluwgh-al-maraam-kitabu-cha-jihaad.html&rhash=705600d1841350) \n\n **Next ➠** /02_buluwgh  "
B_MBILI = "[02-Buluwgh Al-Maraam: Kitabu Cha Jihaad: Mlango Wa Jizya Na Kusitisha Vita](https://telegra.ph/02-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Jizya-Na-Kusitisha-Vita-07-12) \n\n **Next ➠** /03_buluwgh "
B_TATU = "[03-Buluwgh Al-Maraam: Kitabu Cha Jihaad: Mlango Wa Mashindano Ya Farasi Na Kurusha Mishale](https://telegra.ph/03-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Mashindano-Ya-Farasi-Na-Kurusha-Mishale-07-12-2)"
AMULI = """Command Zangu Zoote Zenye Elimu Za Jihaad

All Commands
    ☟☟☟

**1.** /buluwgh

**2.** /Jihaad

**3.** /01_buluwgh

**4.** /02_buluwgh

**5.** /03_buluwgh
"""

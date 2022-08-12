import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID","13810920"))
API_HASH = getenv("API_HASH","6b9fd1fdcc93ac3b40f5847752cbd337")
BOT_USERNAME = getenv("BOT_USERNAME","ultra_vc_music_bot")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN","5419397769:AAEoAO147i8pT3Y2XEdAlKARSSPI-bVLeaU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT","7200"))
SESSION_NAME = getenv("SESSION_NAME", "BQCyZuA97FKOuvJkhTRpf_Elp56mx95KfYAu6GRJlOtCZcSznu-kS2ECgYyOd7h5Ve5_nDESiUEoKotrhVEWvnKrewiYXYmxUyQ81xrZ5vAbncKniMQM3Fh91IaHlRvqDVd0V771oql-O3wPToxSEoKpxhXI40RSKfxpvZkjmN2aj27Nrp94SgRMlPK69EdMpdHz5vgIFikEsmH8g14VbMi-FOvZ1WWIq1el3_s1H_wFpnDmq6zjddTgRfIEyp8kyCmcZU8SlwoX57MxYz3V-BjhaAt1GIo-2BBP1gLQVLxndRx6jUb5i6OmvSMCT4y_0WOzq-zY_7gqZgCtYPwcANy9bniEMgA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1853391922").split()))
aiohttpsession = aiohttp.ClientSession()

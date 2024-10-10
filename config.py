import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "9671629"))
API_HASH = getenv("API_HASH", "be5c84e9dc1ca0e2b53d54b71e575124")

EVAL = list(map(int, getenv("EVAL", "7291869416").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("7632141884:AAHvcEtis4_yca_zFEXCNGn9__i1Tk54wx4")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","BDB0B")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Oscbbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "SOMUXD")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "MissYumikoo")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anubarlo:Anubarlo@cluster0.ioiefbq.mongodb.net/?retryWrites=true&w=majority")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002059513294))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7291869416))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/tutorialwindoxIk/SOMU_V2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/O_P_G")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/QU_QUU")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BAGi8fAAKi11JuYBCZ3d0o_evYzCihyZA-Xi-nVA3hh3UyK1keI8FG2qS5t8ysryBVTkHewmqz1UYghYUuBCA2VTkU7VHBq2x8kx3B83aT6RYSctw4-gkRGNoKgAU3SVDHGI_I7GTNgREgnHM4DJsxuGnlag998q_MNCv6OxV_GawDWK8eRTxhFl884dA5-Fjetjr8wj0e0oHa4YAq6GzkQjCLUy4ONcOub10Y6nVfHuu4ZUGyFQ67g74y8LWKqwlHW9MrrJkhkRYZx4NvxGx60h_zt6K9GxyeYCCMx-JQQfHTmMTVbORBvoY0m7Skmt9X7CWIXilD2-aOzJtQuEDqcZn0CIWAAAAAEvAALVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg"
STATS_IMG_URL = "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/462ea653de0a313f8302a.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/462ea653de0a313f8302a.jpg"
STREAM_IMG_URL = "https://graph.org/file/462ea653de0a313f8302a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/4d303296e4fac9a40ea07.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/IER.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

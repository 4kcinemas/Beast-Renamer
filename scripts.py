class Scripted(object):    


    PROGRESS_DIS = """\n
โญโโโ[**๐Progress Bar๐**]โโโโ
โ
โ<b>๐ : {1} | {2}</b>
โ
โ<b>๐ : {0}%</b>
โ
โ<b>โก : {3}/s</b>
โ
โ<b>โฑ๏ธ : {4}</b>
โฐโโโโโโโโโโโโโโโโโโ"""

    HELP_TEXT = """
<i>๐๐๐ง๐ ๐ ๐ฉ๐ก๐จ๐ญ๐จ ๐ญ๐จ ๐ฆ๐๐ค๐ ๐ข๐ญ ๐๐ฌ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ (optional)</i>\n
<i>๐๐๐ง๐ ๐ฆ๐ ๐๐ง๐ฒ ๐๐ข๐ฅ๐ (or) ๐๐๐๐ข๐ ๐๐ซ๐จ๐ฆ ๐ญ๐๐ฅ๐๐ ๐ซ๐๐ฆ</i>\n
<i>๐๐จ๐ง๐ฏ๐๐ซ๐ญ ๐๐ข๐ฅ๐๐ฌ ๐ข๐ง๐ญ๐จ ๐ฏ๐ข๐๐๐จ ๐ฎ๐ฌ๐ /convert ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฉ๐ฅ๐ฒ ๐ญ๐จ ๐ญ๐ก๐๐ญ ๐๐ข๐ฅ๐ ๐ฐ๐ข๐ญ๐ก /rename ๐ง๐๐ฐ ๐ง๐๐ฆ๐.ext</i>\n
<i>๐๐ข๐๐ฐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /sthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฅ๐๐ญ๐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /dthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>"""


    ABOUT_TEXT = """
โญโโโโ[๐Beast Renamer Bot๐]โโโโ
โ
โ<b>๐ค Bot Name : <a href='https://t.me/beastautofilterbot'>Beast Renamer</a></b>
โ
โ<b>๐ข Channel : <a href='https://t.me/ss_linkz'>SS Linkz</a></b>
โ
โ<b>๐ฅ Version : <a href='https://t.me/beastautofilterbot'>0.9.2 beta</a></b>
โ
โ<b>๐ข Source : It's Closed Project โ
โ
โ<b>๐ Server : <a href='https://heroku.com'>Heroku</a></b>
โ
โ<b>๐ Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
โ
โ<b>ใ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
โ
โ<b>๐จโ๐ป Developer : <a href='https://t.me/sarathi_admin'>@sarathi_admin</a></b>
โ
โ<b>๐ธ Powered By : <a href='https://t.me/NetflixMovies_sslinkz'>Netflix Movies</a></b>
โ
โฐโโโโโโ[Thanks ๐]โโโโ"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>ยฅou Are Banned ๐ซ</b>"
    BANNED_USER_TEXT = "<i>ยฅou are Banned ๐ซ</i>"
    TRYING_TO_UPLOAD = "<i>Trying to Upload.....</i>"
    CURRENT_THUMBNAIL = "<i>๐๐จ๐ฎ๐ซ ๐๐ฎ๐ซ๐ซ๐๐ง๐ญ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐ญ</i>"
    THUMBNAIL_SAVED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฏ๐๐ โ</i>"
    THUMBNAIL_DELETED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฅ๐๐ญ๐๐ โ</i>"
    NO_THUMBNAIL_FOUND = "<i>๐๐จ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ๐ฎ๐ง๐ (Konsi Goals Chahiye)๐</i>"
    TRYING_TO_DOWNLOAD = "<i>Trying to Download....</i>"
    UPLOAD_SUCCESS = "<u>Tสแดษดแดs Fแดส Usษชษดษข แดแดโค @SS_Linkz</u>"
    REPLY_TO_MEDIA = "<i>Reply to Media For Converting with Command /convert</i>"
    UPLOAD_START = "<i>๐ค Uploading Your File Please wait...</i>\n"
    DOWNLOAD_START = "<i>๐ฅ Downloading Your File Please wait...</i>\n"
    JOIN_NOW_TEXT = "<code>First Join My Updates Channel to Use Me</code>"
    REPLY_TO_FILE = "<i>Reply to that media with /rename new name .ext</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Wrong Contact in Support Group @SS_Linkz_Support ๐</i>"
    START_TEXT = "<i>This is a Fastest File Renamer and Converter Bot With Permanant Thumbnail Support๐ฏ</i>"
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/Sarathi_admim'>[ Click Here]</a></b>"

import telebot
import requests
import logging
from telebot.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telebot import apihelper


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
BALE_TOKEN = os.environ.get("BALE_TOKEN")
key = os.environ.get("API_KEY")

# برای ااتصال مجدد ربات به تلگرام از TOKEN اسفاده کنید
# و apihelper را پاک کنید
#apihelper.API_URL = "https://tapi.bale.ai/bot{0}/{1}"
#apihelper.FILE_URL = "https://tapi.bale.ai/file/bot{0}/{1}"

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Accept": "application/json, text/plain, */*",
}

base_url = "https://api.brsapi.ir/Market/"
Currency_url = f"{base_url}Gold_Currency.php?key={key}"
crypto_url = f"{base_url}Cryptocurrency.php?key={key}"
commodity_url = f"{base_url}Commodity.php?key={key}"

# button

start_button = InlineKeyboardButton("منوی اصلی 📲", callback_data="start")
currency_menu = InlineKeyboardButton("منوی ارز 💰", callback_data="currency")
crypto_menu_button = InlineKeyboardButton("منوی کریپتو ₿", callback_data="crypto")
gold_menu_button = InlineKeyboardButton("منوی طلا 🪙", callback_data="gold")
commodity_button = InlineKeyboardButton("منوی کامودیتی 🛢️")


usd_button = KeyboardButton("usd/دلار💵")
eur_button = KeyboardButton("eur/یورو💶")
gbp_button = KeyboardButton("gbp/پوند💷")
aed_button = KeyboardButton("aed/درهم امارات🇦🇪")
jpy_button = KeyboardButton("jpy/ین ژاپن💴")
cad_button = KeyboardButton("cad/دلار کانادا🇨🇦")
aud_button = KeyboardButton("aud/دلار استرالیا🇦🇺")
kwd_button = KeyboardButton("kwd/دینار کویت🇰🇼")
cny_button = KeyboardButton("cny/یوان چین🇨🇳")
sar_button = KeyboardButton("sar/ریال عربستان🇸🇦")
chf_button = KeyboardButton("chf/فرانک سوئیس🇨🇭")

btc_button = KeyboardButton("btc/بیتکوین")
eth_button = KeyboardButton("eth/اتریوم")
bnb_button = KeyboardButton("bnb/بایننس کوین")
sol_button = KeyboardButton("sol/سولانا")
xrp_button = KeyboardButton("xrp/ریپل")
ada_button = KeyboardButton("ada/کاردانو")
doge_button = KeyboardButton("doge/دوج کوین")
trx_button = KeyboardButton("trx/ترون")
ton_button = KeyboardButton("ton/تون کوین")
tether_button = KeyboardButton("usdt/تتر")
dot_button = KeyboardButton("dot/پولکادات")
link_button = KeyboardButton("link/چین لینک")
ltc_button = KeyboardButton("ltc/لایت کوین")
shib_button = KeyboardButton("shib/شیبا اینو")
atom_button = KeyboardButton("atom/کازموس")

gold_18k_button = KeyboardButton("طلای 18 عیار")
gold_24k_button = KeyboardButton("طلای 24 عیار")
gold_ounce_button = KeyboardButton("انس جهانی طلا")
quater_coin_button = KeyboardButton("ربع سکه")
half_coin_button = KeyboardButton("نیم سکه")
imami_coin_button = KeyboardButton("سکه امامی")
bahar_azadi_coin_button = KeyboardButton("سکه بهار آزادی")

gold_oz_button = KeyboardButton("XAUUSD/انس طلا 🥇")
silver_oz_button = KeyboardButton("XAGUSD/انس نقره 🥈")
platinum_oz_button = KeyboardButton("XPTUSD/انس پلاتین ⚪")
palladium_oz_button = KeyboardButton("XPDUSD/انس پالادیوم 🔘")

copper_button = KeyboardButton("Cu/مس 🟠")
aluminum_button = KeyboardButton("Al/آلومینیوم ⚙️")
zinc_button = KeyboardButton("Zn/روی 🔩")
lead_button = KeyboardButton("Pb/سرب ⚫")
# tin_button = KeyboardButton("Sn/قلع 🔧")
nickel_button = KeyboardButton("Ni/نیکل 🪙")

brent_button = KeyboardButton("BRENT/نفت برنت 🛢️")
wti_button = KeyboardButton("WTI/نفت سبک ⛽")
gas_button = KeyboardButton("GAS/گاز طبیعی 🔥")
gasoline_button = KeyboardButton("RBOB/بنزین 🚗")
gasoil_button = KeyboardButton("GASOIL/گازوییل 🚚")

chanle_link_button = InlineKeyboardButton("لینک کانال ما 📡", url="https://abantether.com")
link_markup = InlineKeyboardMarkup().add(chanle_link_button)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

Author = """
👋 About the Author

I'm Kamyar Shahroudi, a software developer and tech enthusiast. I create projects focused on programming, automation, and networking while continuously learning and experimenting with new technologies.

🔗 GitHub: https://github.com/kamyarshah-11
💬 Telegram: https://t.me/KamyJooon
📸 Instagram: https://instagram.com/kamyarr166
📧 Email: kshahroudi97@gmail.com

Thanks for using this bot! Your feedback and suggestions are always welcome.
"""




@bot.message_handler(commands=["Author"])
def Author_info(message):
    bot.send_message(message.chat.id, Author)
    return


@bot.message_handler(commands=["start"])
def start_menu(message):
    logger.info("start menu")
    markup = ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(currency_menu, gold_menu_button)
    markup.add(crypto_menu_button, commodity_button)
    markup.add(chanle_link_button)

    bot.send_message(
        message.chat.id,
        "منوی اصلی :\nیکی از گزینه های زیر را انتخاب کنید 👇",
        reply_markup=markup,
    )
    return


@bot.message_handler(func=lambda message: True)
def handeling_messages(message):
    logger.info("handeling message")

    text = message.text

    if text == "usd/دلار💵":
        bot.send_message(message.chat.id, price("USD"), reply_markup=link_markup)
        return

    elif text == "eur/یورو💶":
        bot.send_message(message.chat.id, price("EUR"), reply_markup=link_markup)
        return

    elif text == "gbp/پوند💷":
        bot.send_message(message.chat.id, price("GBP"), reply_markup=link_markup)
        return

    elif text == "aed/درهم امارات🇦🇪":
        bot.send_message(message.chat.id, price("AED"), reply_markup=link_markup)
        return

    elif text == "jpy/ین ژاپن💴":
        bot.send_message(message.chat.id, price("JPY"), reply_markup=link_markup)
        return

    elif text == "cad/دلار کانادا🇨🇦":
        bot.send_message(message.chat.id, price("CAD"), reply_markup=link_markup)
        return

    elif text == "aud/دلار استرالیا🇦🇺":
        bot.send_message(message.chat.id, price("AUD"), reply_markup=link_markup)
        return

    elif text == "kwd/دینار کویت🇰🇼":
        bot.send_message(message.chat.id, price("KWD"), reply_markup=link_markup)
        return

    elif text == "cny/یوان چین🇨🇳":
        bot.send_message(message.chat.id, price("CNY"), reply_markup=link_markup)
        return

    elif text == "sar/ریال عربستان🇸🇦":
        bot.send_message(message.chat.id, price("SAR"), reply_markup=link_markup)
        return

    elif text == "chf/فرانک سوئیس🇨🇭":
        bot.send_message(message.chat.id, price("CHF"), reply_markup=link_markup)
        return

    elif text == "btc/بیتکوین":
        bot.send_message(
            message.chat.id, crypto_price("Bitcoin"), reply_markup=link_markup
        )
        return

    elif text == "eth/اتریوم":
        bot.send_message(
            message.chat.id, crypto_price("Ethereum"), reply_markup=link_markup
        )
        return

    elif text == "bnb/بایننس کوین":
        bot.send_message(
            message.chat.id, crypto_price("Binance Coin"), reply_markup=link_markup
        )
        return

    elif text == "sol/سولانا":
        bot.send_message(
            message.chat.id, crypto_price("Solana"), reply_markup=link_markup
        )
        return

    elif text == "xrp/ریپل":
        bot.send_message(message.chat.id, crypto_price("XRP"), reply_markup=link_markup)
        return

    elif text == "ada/کاردانو":
        bot.send_message(
            message.chat.id, crypto_price("Cardano"), reply_markup=link_markup
        )
        return

    elif text == "doge/دوج کوین":
        bot.send_message(
            message.chat.id, crypto_price("Dogecoin"), reply_markup=link_markup
        )
        return

    elif text == "trx/ترون":
        bot.send_message(
            message.chat.id, crypto_price("TRON"), reply_markup=link_markup
        )
        return

    elif text == "ton/تون کوین":
        bot.send_message(
            message.chat.id, crypto_price("Toncoin"), reply_markup=link_markup
        )
        return

    elif text == "usdt/تتر":
        bot.send_message(
            message.chat.id, crypto_price("Tether"), reply_markup=link_markup
        )
        return

    elif text == "dot/پولکادات":
        bot.send_message(
            message.chat.id, crypto_price("Polkadot"), reply_markup=link_markup
        )
        return

    elif text == "link/چین لینک":
        bot.send_message(
            message.chat.id, crypto_price("Chainlink"), reply_markup=link_markup
        )
        return

    elif text == "ltc/لایت کوین":
        bot.send_message(
            message.chat.id, crypto_price("Litecoin"), reply_markup=link_markup
        )
        return

    elif text == "shib/شیبا اینو":
        bot.send_message(
            message.chat.id, crypto_price("SHIBA INU"), reply_markup=link_markup
        )
        return

    elif text == "atom/کازموس":
        bot.send_message(
            message.chat.id, crypto_price("Cosmos"), reply_markup=link_markup
        )
        return

    elif text == "طلای 18 عیار":
        bot.send_message(
            message.chat.id, gold_price("طلای 18 عیار"), reply_markup=link_markup
        )
        return

    elif text == "طلای 24 عیار":
        bot.send_message(message.chat.id, gold_price(text), reply_markup=link_markup)
        return

    elif text == "انس جهانی طلا":
        bot.send_message(
            message.chat.id, gold_price("انس طلا"), reply_markup=link_markup
        )
        return

    elif text == "ربع سکه":
        bot.send_message(message.chat.id, gold_price(text), reply_markup=link_markup)
        return

    elif text == "نیم سکه":
        bot.send_message(message.chat.id, gold_price(text), reply_markup=link_markup)
        return

    elif text == "سکه امامی":
        bot.send_message(message.chat.id, gold_price(text), reply_markup=link_markup)
        return

    elif text == "سکه بهار آزادی":
        bot.send_message(message.chat.id, gold_price(text), reply_markup=link_markup)
        return

    elif text == "XAUUSD/انس طلا 🥇":
        bot.send_message(
            message.chat.id, commodity_price("XAUUSD"), reply_markup=link_markup
        )
        return

    elif text == "XAGUSD/انس نقره 🥈":
        bot.send_message(
            message.chat.id, commodity_price("XAGUSD"), reply_markup=link_markup
        )
        return

    elif text == "XPTUSD/انس پلاتین ⚪":
        bot.send_message(
            message.chat.id, commodity_price("XPTUSD"), reply_markup=link_markup
        )
        return

    elif text == "XPDUSD/انس پالادیوم 🔘":
        bot.send_message(
            message.chat.id, commodity_price("XPDUSD"), reply_markup=link_markup
        )
        return

    elif text == "Cu/مس 🟠":
        bot.send_message(
            message.chat.id, commodity_price("Cu"), reply_markup=link_markup
        )
        return

    elif text == "Al/آلومینیوم ⚙️":
        bot.send_message(
            message.chat.id, commodity_price("Al"), reply_markup=link_markup
        )
        return

    elif text == "Zn/روی 🔩":
        bot.send_message(
            message.chat.id, commodity_price("Zn"), reply_markup=link_markup
        )
        return

    elif text == "Pb/سرب ⚫":
        bot.send_message(
            message.chat.id, commodity_price("Pb"), reply_markup=link_markup
        )
        return

    elif text == "Sn/قلع 🔧":
        bot.send_message(
            message.chat.id, commodity_price("Sn"), reply_markup=link_markup
        )
        return

    elif text == "Ni/نیکل 🪙":
        bot.send_message(
            message.chat.id, commodity_price("Ni"), reply_markup=link_markup
        )
        return

    elif text == "BRENT/نفت برنت 🛢️":
        bot.send_message(
            message.chat.id, commodity_price("BRENT"), reply_markup=link_markup
        )
        return

    elif text == "WTI/نفت سبک ⛽":
        bot.send_message(
            message.chat.id, commodity_price("WTI"), reply_markup=link_markup
        )
        return

    elif text == "GAS/گاز طبیعی 🔥":
        bot.send_message(
            message.chat.id, commodity_price("GAS"), reply_markup=link_markup
        )
        return

    elif text == "RBOB/بنزین 🚗":
        bot.send_message(
            message.chat.id, commodity_price("RBOB"), reply_markup=link_markup
        )
        return

    elif text == "GASOIL/گازوییل 🚚":
        bot.send_message(
            message.chat.id, commodity_price("GASOIL"), reply_markup=link_markup
        )
        return

    elif text == "منوی اصلی 📲":
        start_menu(message)
        return

    elif text == "منوی کریپتو ₿":
        crypto_menu(message)
        return

    elif text == "منوی ارز 💰":
        curr_menu(message)
        return

    elif text == "منوی طلا 🪙":
        gold_menu(message)
        return

    elif text == "منوی کامودیتی 🛢️":
        commodity_menu(message)
        return

    elif text == "لینک کانال ما":
        bot.send_message(message.chat.id,"لینک کانال ما :",reply_markup=InlineKeyboardMarkup.add(InlineKeyboardButton("قیمت چند؟|Gheymat chand?",url="https://t.me/Gheymat_Chand_team")))
        return
    else:
        bot.send_message(message.chat.id, "درخواست نادرست")
        return


def curr_menu(message):
    logger.info("currency menu")

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    markup.add(usd_button, eur_button)
    markup.add(gbp_button, jpy_button)
    markup.add(aed_button, cad_button)
    markup.add(aud_button, kwd_button)
    markup.add(cny_button, sar_button, chf_button)
    markup.add(start_button)

    bot.send_message(
        message.chat.id,
        "منوی ارز 💵\n\nاز گزینه های زیر یکی را انتخواب کنید",
        reply_markup=markup,
    )
    return


def crypto_menu(message):
    logger.info("crypto menu")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    markup.row(btc_button, eth_button)
    markup.row(bnb_button, sol_button)
    markup.row(xrp_button, ada_button)
    markup.row(doge_button, trx_button)
    markup.row(ton_button, tether_button)
    markup.row(dot_button, link_button)
    markup.row(ltc_button, shib_button)
    markup.row(atom_button)
    markup.add(start_button)

    bot.send_message(
        message.chat.id,
        "منوی کریپتو :\nاز گزینه های زیر یکی را انتخواب کنید",
        reply_markup=markup,
    )
    return


def gold_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(gold_18k_button, gold_24k_button)
    markup.add(gold_ounce_button)
    markup.add(quater_coin_button, half_coin_button)
    markup.add(imami_coin_button, bahar_azadi_coin_button)
    markup.add(start_button)

    bot.send_message(
        message.chat.id, "از بین گزینه های زیر یکی را انتخواب کنید", reply_markup=markup
    )
    return


def commodity_menu(message):
    logger.info("commodity menu")

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(gold_oz_button, silver_oz_button)
    markup.add(platinum_oz_button, palladium_oz_button)

    markup.add(copper_button, aluminum_button)
    markup.add(zinc_button, lead_button)
    markup.add(nickel_button)

    markup.add(brent_button, wti_button)
    markup.add(gas_button, gasoline_button)
    markup.add(gasoil_button)

    markup.add(start_button)

    bot.send_message(message.chat.id, "منوی کامودیتی 🛢️", reply_markup=markup)
    return


def price(symbol):
    r = requests.get(Currency_url, timeout=5, headers=headers)
    if r.status_code != 200:
        return "متاسفانه خطایی رخ داده است لطفا بعدا تلاش کنید❌"

    data = r.json()
    data = data["currency"]

    for curr in data:
        if curr["symbol"] == symbol:
            try:
                return f"{curr["name"]} : {int(curr["price"]):,} {curr["unit"]}\nدرصد تغییرات : {curr["change_percent"]} 💹\nآخرین آپدیت : {curr["date"]} {curr["time"]}"
            except:
                return "wrong name"


def crypto_price(name):
    r = requests.get(crypto_url, headers=headers, timeout=5)

    if r.status_code != 200:
        return "متاسفانه خطایی رخ داده است لطفا بعدا تلاش کنید❌"

    data = r.json()

    for curr in data:

        if curr["name_en"].upper() == name.upper():
            try:
                return f"🪙{curr["name"]} : {curr["price"]} $\n{int(curr["price_toman"]):,} تومان\nدرصد تغییرات : {curr["change_percent"]} 💹\nآخرین آپدیت : {curr["date"]} {curr["time"]}"
            except:
                return f"🪙{curr["name"]} : {curr["price"]} $\n{curr["price_toman"]} تومان\nدرصد تغییرات : {curr["change_percent"]} 💹\nآخرین آپدیت : {curr["date"]} {curr["time"]}"

    return "ارز مورد نظر پیدا نشد"


def gold_price(name):
    r = requests.get(Currency_url, headers=headers, timeout=10)

    if r.status_code != 200:
        return "متاسفانه خطایی رخ داده است لطفا بعدا تلاش کنید❌"

    data = r.json()
    data = data["gold"]

    for curr in data:
        if curr["name"] == name:
            return f"{curr["name"]} : {int(curr["price"]):,} {curr["unit"]}\nدرصد تغییرات : {curr["change_percent"]} 💹\nآخرین آپدیت : {curr["date"]} {curr["time"]}"


def commodity_price(name):
    r = requests.get(commodity_url, headers=headers, timeout=10)

    data = r.json()
    category = "metal_precious"

    for curr in data[category]:
        if curr["symbol"] == name:
            return f"{curr["name"]} : {curr["price"]} {curr["unit"]}\nمیزان تغییرات : {curr["change_percent"]}\nآخرین اپدیت : {curr["time"]} {curr["date"]}"

    category = "metal_base"
    for curr in data[category]:
        if curr["symbol"] == name:
            return f"{curr["name"]} : {curr["price"]} {curr["unit"]}\nمیزان تغییرات : {curr["change_percent"]}\nآخرین اپدیت : {curr["time"]} {curr["date"]}"

    category = "energy"
    for curr in data[category]:
        if curr["symbol"] == name:
            return f"{curr["name"]} : {curr["price"]} {curr["unit"]}\nمیزان تغییرات : {curr["change_percent"]}\nآخرین اپدیت : {curr["time"]} {curr["date"]}"

    return "نام اشتباه است"


bot.infinity_polling()

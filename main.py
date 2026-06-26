import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT = "@elegramSMS_Support27"

# --- القواميس ---
SERVICES = {
    "btn_tg": {"name": "✈️ تليجرام", "countries": {"البرازيل": ("0.50 USDT", "50 نجمة"), "كندا": ("0.30 USDT", "30 نجمة"), "أمريكا": ("0.40 USDT", "40 نجمة"), "إيران": ("0.50 USDT", "50 نجمة"), "سوريا": ("1.10 USDT", "110 نجمة"), "المغرب": ("0.50 USDT", "50 نجمة")}},
    "btn_fb": {"name": "🔵 فيسبوك", "countries": {"ألمانيا": ("0.20 USDT", "20 نجمة"), "السودان": ("0.20 USDT", "20 نجمة"), "الأردن": ("0.30 USDT", "30 نجمة")}},
    "btn_ig": {"name": "📸 انستقرام", "countries": {"غانا": ("0.25 USDT", "25 نجمة"), "الأردن": ("0.30 USDT", "30 نجمة")}},
    "btn_tt": {"name": "🎵 تيك توك", "countries": {"النرويج": ("0.30 USDT", "30 نجمة")}},
    "btn_apple": {"name": "🍎 أبل", "countries": {"السودان": ("0.30 USDT", "30 نجمة"), "زيمبابوي": ("0.25 USDT", "25 نجمة")}},
    "btn_paypal": {"name": "💰 باي بال", "countries": {"فنزويلا": ("0.30 USDT", "30 نجمة")}}
}

PAYMENT_METHODS = """💳 **طرق الدفع المعتمدة:**

🔹 **C-Wallet:** `61824874`

🔹 **FaucetPay:** `Telegramsms71@gmail.com`

🔹 **TON Network:** `UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7`

🔹 **USDT Polygon:** `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`

🔹 **USDT ERC-20:** `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`

🔹 **USDT TRC-20:** `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`"""

STARS_SHOP = """⭐️ **متجر النجوم:**

💎 النجمة الواحدة: `0.015$`

🐻 دب: `0.2$`

🌹 وردة: `0.29$`

🍰 كيكة: `0.55$`

💍 خاتم: `1.1$`"""

# --- الوظائف ---
def send_main_menu(m):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("✈️ تليجرام", callback_data="btn_tg"),
        types.InlineKeyboardButton("🔵 فيسبوك", callback_data="btn_fb"),
        types.InlineKeyboardButton("📸 انستقرام", callback_data="btn_ig"),
        types.InlineKeyboardButton("🎵 تيك توك", callback_data="btn_tt"),
        types.InlineKeyboardButton("🍎 أبل", callback_data="btn_apple"),
        types.InlineKeyboardButton("💰 باي بال", callback_data="btn_paypal"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="btn_stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay")
    )
    text = "✨ **مرحباً بك في متجر الأرقام الرسمي**\n\nاختر الخدمة من القائمة:"
    if hasattr(m, 'message_id'): bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    cid, mid = call.message.chat.id, call.message.message_id
    
    if call.data in SERVICES:
        srv = SERVICES[call.data]
        kb = types.InlineKeyboardMarkup(row_width=1)
        for country in srv["countries"]:
            kb.add(types.InlineKeyboardButton(f"{country}", callback_data=f"price_{call.data}_{country}"))
        kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text(f"🛍 **ماذا تريد أن تشتري من {srv['name']}؟**", cid, mid, reply_markup=kb, parse_mode="Markdown")
        
    elif call.data.startswith("price_"):
        parts = call.data.split("_")
        srv_key = f"{parts[1]}_{parts[2]}"
        country = parts[3]
        price, stars = SERVICES[srv_key]["countries"][country]
        
        # تنسيق متباعد بمسافات إضافية
        details = f"""📝 **تفاصيل الطلب:**

الدولة: {country}

💰 السعر: `{price}`

⭐️ التكلفة: `{stars}`

➖➖➖➖➖➖

📌 *تواصل مع الدعم للطلب.*"""
        
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("🛒 شراء", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data=srv_key))
        bot.edit_message_text(details, cid, mid, reply_markup=kb, parse_mode="Markdown")

    elif call.data == "btn_stars":
        kb = types.InlineKeyboardMarkup(); kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text(STARS_SHOP, cid, mid, reply_markup=kb, parse_mode="Markdown")

    elif call.data == "btn_pay":
        kb = types.InlineKeyboardMarkup(); kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text(PAYMENT_METHODS, cid, mid, reply_markup=kb, parse_mode="Markdown")
        
    elif call.data == "back_main":
        send_main_menu(call.message)

@bot.message_handler(commands=['start'])
def start(m): send_main_menu(m)

bot.polling(none_stop=True)

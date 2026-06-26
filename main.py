import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT = "@elegramSMS_Support23"

# القنوات
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262"]

def check_sub(uid):
    for ch in CHANNELS:
        try:
            if bot.get_chat_member(ch, uid).status in ['left', 'kicked']: return False
        except: return False
    return True

# القائمة الرئيسية
def main_menu(m, edit=False):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("📱 WhatsApp", callback_data="cat_wa"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="cat_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="cat_tt"),
        types.InlineKeyboardButton("💳 Payment", callback_data="pay")
    )
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nChoose your service below 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    if not check_sub(m.chat.id):
        kb = types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.add(types.InlineKeyboardButton(f"JOIN {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.add(types.InlineKeyboardButton("✅ CHECK", callback_data="check"))
        bot.send_message(m.chat.id, "⚠️ **Must join our channels first!**", reply_markup=kb, parse_mode="Markdown")
    else: main_menu(m)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    if c.data == "check":
        if check_sub(cid): main_menu(c.message)
        else: bot.answer_callback_query(c.id, "❌ Not joined yet!", show_alert=True)
    elif c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "pay":
        text = ("💳 **Payment Methods:**\n\nTON: `UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n"
                "USDT (Poly/BEP): `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
                "USDT (ERC20): `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
                "USDT (TRC20): `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n"
                "Cwallet: `61824874` | Faucet: `telegramsms71@gmail.com`")
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb, parse_mode="Markdown")
    elif c.data == "cat_wa":
        text = "📱 **WhatsApp Pricing:**\nNigeria: 20ن | Sudan: 15ن | Venezuela: 25ن | Germany: 20ن"
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("BUY", callback_data="buy"), types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)
    elif c.data == "cat_tg":
        text = "✈️ **Telegram Pricing:**\nUSA: 20ن | Egypt: 50ن | Syria: 110ن"
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("BUY", callback_data="buy"), types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)
    elif c.data == "cat_fb":
        text = "🔵 **Facebook Pricing:**\nGermany: 20ن | Jordan: 30ن"
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("BUY", callback_data="buy"), types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)
    elif c.data == "cat_ig":
        text = "📸 **Instagram Pricing:**\nGhana: 25ن | Jordan: 30ن"
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("BUY", callback_data="buy"), types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)
    elif c.data == "cat_tt":
        text = "🎵 **TikTok Pricing:**\nNorway: 0.3 Star"
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("BUY", callback_data="buy"), types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)
    elif c.data == "buy":
        bot.send_message(cid, f"✅ Send receipt to support: {SUPPORT}")

bot.polling(none_stop=True)

import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

# إعدادات
SUPPORT = "@elegramSMS_Support23"

def main_menu(m, edit=False):
    kb = types.InlineKeyboardMarkup(row_width=2) 
    kb.add(
        types.InlineKeyboardButton("🔥 Tinder", callback_data="cat_tinder"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="cat_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="cat_tt"),
        types.InlineKeyboardButton("🔍 Google", callback_data="cat_goog"),
        types.InlineKeyboardButton("🍎 Apple", callback_data="cat_apple"),
        types.InlineKeyboardButton("💰 PayPal", callback_data="cat_paypal"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="pay")
    )
    kb.add(types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nChoose your service below 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    
    elif c.data == "cat_tinder":
        bot.edit_message_text("🔥 **Tinder Services:**\n\n• Indonesia: $0.20 (20ن)\n• Mozambique: $0.30 (30ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tg":
        bot.edit_message_text("✈️ **Telegram Services:**\n\n• USA: $0.25 (20ن)\n• Egypt: $0.50 (50ن)\n• Syria: $1.10 (110ن)\n• India: $0.30 (30ن)\n• Mixed: $0.28 (28ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_fb":
        bot.edit_message_text("🔵 **Facebook Services:**\n\n• Germany: $0.20 (20ن)\n• Madagascar: $0.20 (20ن)\n• Sudan: $0.20 (20ن)\n• Jordan: $0.30 (30ن)\n• Ghana: $0.25 (25ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_ig":
        bot.edit_message_text("📸 **Instagram Services:**\n\n• Ghana: $0.25 (25ن)\n• Jordan: $0.30 (30ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tt":
        bot.edit_message_text("🎵 **TikTok Services:**\n\n• Norway: $0.30 (30ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_goog":
        bot.edit_message_text("🔍 **Google Services:**\n\n• Venezuela: $0.20 (20ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_apple":
        bot.edit_message_text("🍎 **Apple Services:**\n\n• Sudan: $0.30 (30ن)\n• Zimbabwe: $0.25 (25ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_paypal":
        bot.edit_message_text("💰 **PayPal Services:**\n\n• Venezuela: $0.30 (30ن)", cid, mid, reply_markup=back_kb)
        
    elif c.data == "pay":
        bot.edit_message_text("""💳 **طرق الدفع:**
🔹 C-Wallet: `61824874`
🔹 FaucetPay: `Telegramsms71@gmail.com`
🔹 USDT Polygon/BEP20: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
🔹 USDT ERC20: `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
🔹 USDT TRC20: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`""", cid, mid, reply_markup=back_kb, parse_mode="Markdown")
        
    elif c.data == "stars":
        bot.edit_message_text("⭐️ **متجر النجوم:**\n\n• النجمة الواحدة = 0.015$\n• دب: $0.2\n• وردة: $0.29\n• كيكة: $0.55\n• خاتم: $1.1", cid, mid, reply_markup=back_kb)

@bot.message_handler(commands=['start'])
def start(m):
    main_menu(m)

bot.polling(none_stop=True)

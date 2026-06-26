import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT = "@elegramSMS_Support27" 
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262", "@tanadolsms"]
ADMIN_ID = 8767607098 

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
        types.InlineKeyboardButton("🎥 YouTube", callback_data="cat_yt"),
        types.InlineKeyboardButton("🐦 Twitter", callback_data="cat_tw"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="pay")
    )
    kb.add(types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nالسعر الموحد: 1 نجمة (0.01$) لكل متابع/إعجاب، أو لكل 10 مشاهدات 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    
    price_note = "\n\n💰 السعر: 1 نجمة (0.01$) لكل متابع/إعجاب، أو 10 مشاهدات."

    if c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "cat_tinder":
        bot.edit_message_text("🔥 Tinder: إندونيسيا/موزمبيق" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tg":
        bot.edit_message_text("✈️ Telegram Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_fb":
        bot.edit_message_text("🔵 Facebook Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_ig":
        bot.edit_message_text("📸 Instagram Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tt":
        bot.edit_message_text("🎵 TikTok Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_goog":
        bot.edit_message_text("🔍 Google Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_apple":
        bot.edit_message_text("🍎 Apple Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_paypal":
        bot.edit_message_text("💰 PayPal Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_yt":
        bot.edit_message_text("🎥 YouTube Services" + price_note, cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tw":
        bot.edit_message_text("🐦 Twitter Services" + price_note, cid, mid, reply_markup=back_kb)
    
    elif c.data == "pay":
        bot.edit_message_text("""💳 **طرق الدفع:**
🔹 C-Wallet: `61824874`
🔹 FaucetPay: `Telegramsms71@gmail.com`
🔹 USDT: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`""", cid, mid, reply_markup=back_kb, parse_mode="Markdown")
        
    elif c.data == "stars":
        bot.edit_message_text("⭐️ النجمة الواحدة = 0.015$\n🎁 الهدايا المتاحة في المتجر.", cid, mid, reply_markup=back_kb)

@bot.message_handler(commands=['start'])
def start(m):
    main_menu(m)

bot.polling(none_stop=True)

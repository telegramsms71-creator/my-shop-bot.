import telebot
from telebot import types

# توكن البوت
BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

# الإعدادات
SUPPORT = "@elegramSMS_Support23"
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262", "@tanadolsms"]
ADMIN_ID = 8767607098 

# إشعار للأدمن عند دخول عضو جديد
def send_notification(user):
    try:
        user_info = f"👤 **عضو جديد في بوت الأرقام!**\n\nالاسم: {user.first_name}\nاليوزر: @{user.username}\nالـ ID: `{user.id}`"
        bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")
    except: pass

# التحقق من الاشتراك الإجباري
def check_sub(uid):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, uid).status
            if status in ['left', 'kicked']: return False
        except: return False
    return True

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
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nأهلاً بك في بوت الأرقام، اختر الخدمة المطلوبة 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    send_notification(m.from_user)
    if not check_sub(m.chat.id):
        kb = types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.add(types.InlineKeyboardButton(f"JOIN {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.add(types.InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check"))
        bot.send_message(m.chat.id, "⚠️ **يجب الاشتراك في القنوات التالية لتشغيل البوت:**", reply_markup=kb)
    else: main_menu(m)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "check":
        if check_sub(cid): main_menu(c.message)
        else: bot.answer_callback_query(c.id, "❌ يرجى الاشتراك في جميع القنوات أولاً!", show_alert=True)
    
    elif c.data == "pay":
        bot.edit_message_text("""💳 **طرق الدفع المتوفرة:**
🔹 C-Wallet: `61824874`
🔹 FaucetPay: `Telegramsms71@gmail.com`
🔹 TON Network: `UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7`
🔹 USDT Polygon: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
🔹 USDT BEP20: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
🔹 USDT ERC20: `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
🔹 USDT TRC20: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`""", cid, mid, reply_markup=back_kb, parse_mode="Markdown")
        
    elif c.data == "stars":
        bot.edit_message_text("⭐️ **متجر النجوم:**\n• النجمة الواحدة = 0.015$\n• دب: 0.2$ | وردة: 0.29$ | كيكة: 0.55$ | خاتم: 1.1$", cid, mid, reply_markup=back_kb)
    
    # أقسام الدول
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

bot.polling(none_stop=True)

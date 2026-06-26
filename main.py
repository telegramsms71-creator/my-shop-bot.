import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

# إعدادات النظام
SUPPORT = "@elegramSMS_Support23" 
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262", "@tanadolsms"]
ADMIN_ID = 8767607098 

# إشعارات دخول عضو جديد
def send_notification(user):
    try:
        user_info = f"👤 **عضو جديد دخل البوت!**\n\nالاسم: {user.first_name}\nاليوزر: @{user.username}\nالـ ID: `{user.id}`"
        bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")
    except Exception as e:
        print(f"Error: {e}")

# التحقق من الاشتراك
def check_sub(uid):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, uid).status
            if status in ['left', 'kicked']: return False
        except: return False
    return True

def main_menu(m, edit=False):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("👤 قسم المتابعين (Followers)", callback_data="all_foll"),
        types.InlineKeyboardButton("📊 قسم الأرقام والمشاهدات (Views/Likes)", callback_data="all_nums"),
        types.InlineKeyboardButton("💳 طرق الدفع (Payment Methods)", callback_data="pay"),
        types.InlineKeyboardButton("⭐️ متجر النجوم (Stars Store)", callback_data="stars"),
        types.InlineKeyboardButton("📞 الدعم الفني (Support)", url=f"https://t.me/{SUPPORT[1:]}")
    )
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nأهلاً بك، اختر القسم الذي تريده من الأزرار الكبيرة أدناه 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    send_notification(m.from_user)
    if not check_sub(m.chat.id):
        kb = types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.add(types.InlineKeyboardButton(f"JOIN {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.add(types.InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check"))
        bot.send_message(m.chat.id, "⚠️ **يجب الاشتراك في جميع القنوات لتشغيل البوت:**", reply_markup=kb, parse_mode="Markdown")
    else: main_menu(m)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="back"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "check":
        if check_sub(cid): main_menu(c.message)
        else: bot.answer_callback_query(c.id, "❌ يرجى الاشتراك في جميع القنوات أولاً!", show_alert=True)
    
    elif c.data == "pay":
        bot.edit_message_text("""💳 **طرق الدفع:**
🔹 C-Wallet: `61824874`
🔹 FaucetPay: `Telegramsms71@gmail.com`
🔹 USDT Polygon/BEP20: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
🔹 USDT ERC20: `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
🔹 USDT TRC20: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`""", cid, mid, reply_markup=back_kb, parse_mode="Markdown")
    
    elif c.data == "stars":
        bot.edit_message_text("⭐️ **متجر النجوم:**\nنجمة واحدة = 0.015$", cid, mid, reply_markup=back_kb)

bot.polling(none_stop=True)

import telebot
import os

# التوكن الجديد المعتمد
TOKEN = '8851361153:AAE4bKy0_KtSEqCEm9LEQlKV9avGE-kIy_w' 
bot = telebot.TeleBot(TOKEN)
SUPPORT_USER = "@Sultan_Support27"
ADMIN_ID = 8767607098 

# --- نظام حفظ المستخدمين للإشعارات ---
def save_user(user_id):
    try:
        if not os.path.exists("users.txt"):
            with open("users.txt", "w") as f: f.write("")
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
        if str(user_id) not in users:
            with open("users.txt", "a") as f:
                f.write(str(user_id) + "\n")
    except: pass

def get_users():
    try:
        with open("users.txt", "r") as f:
            return set(line.strip() for line in f)
    except: return set()

# --- القوائم الأساسية ---
def main_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("♡ شراء أرقام وهمية ♡", callback_data="numbers_type"),
        telebot.types.InlineKeyboardButton("♡ خدمات الرشق والمتابعين ♡", callback_data="rashq_menu"),
        telebot.types.InlineKeyboardButton("♡ اشحن حسابك (طرق الدفع) ♡", callback_data="charge"),
        telebot.types.InlineKeyboardButton("♡ الدعم الفني ♡", callback_data="support")
    )
    return markup

def select_number_type():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("📱 تليجرام", callback_data="numbers_telegram"),
        telebot.types.InlineKeyboardButton("💬 واتساب", callback_data="numbers_whatsapp"),
        telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu")
    )
    return markup

def rashq_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("📢 رشق تليجرام", callback_data="contact_tg_rashq"),
        telebot.types.InlineKeyboardButton("📸 رشق إنستجرام", callback_data="contact_insta_rashq"),
        telebot.types.InlineKeyboardButton("🎵 رشق تيك توك", callback_data="contact_tiktok_rashq"),
        telebot.types.InlineKeyboardButton("📺 رشق يوتيوب", callback_data="contact_yt_rashq"),
        telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu")
    )
    return markup

def payment_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    payments = [
        ("💎 Cwallet | 61824874", "cwallet"), ("📧 FaucetPay | TelegramSMS", "faucetpay"),
        ("⛓️ Tron (TRC20)", "trc20"), ("🌐 USDT (ERC20)", "erc20"),
        ("🌐 USDT (BEP20)", "bep20"), ("🌐 USDT (Polygon)", "polygon")
    ]
    for name, cb in payments: markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"contact_{cb}"))
    markup.add(telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu"))
    return markup

# --- المعالج الأساسي ---
@bot.message_handler(commands=['start'])
def start(message):
    save_user(message.chat.id)
    bot.send_message(message.chat.id, "👋 أهلاً بك في بوت السلطان", reply_markup=main_menu())

@bot.message_handler(commands=['notify'])
def notify_users(message):
    if message.from_user.id == ADMIN_ID:
        text = message.text.replace("/notify ", "")
        for user_id in get_users():
            try: bot.send_message(user_id, f"🔔 إشعار من السلطان:\n\n{text}")
            except: pass
        bot.reply_to(message, "تم إرسال الإشعار.")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "main_menu": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="القائمة الرئيسية:", reply_markup=main_menu())
    elif call.data == "numbers_type": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اختر نوع الخدمة:", reply_markup=select_number_type())
    elif call.data == "rashq_menu": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قسم الرشق:", reply_markup=rashq_menu())
    elif call.data == "charge": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="طرق الدفع:", reply_markup=payment_menu())
    elif call.data.startswith(("buy_", "contact_")): bot.send_message(call.message.chat.id, f"✅ تواصل مع الدعم لإتمام الطلب:\n{SUPPORT_USER}")

# --- التشغيل الآمن ---
if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True, interval=0, timeout=60)

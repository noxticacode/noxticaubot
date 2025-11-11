# updates by @noxtica on TG
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot.core.database import mongo_client
from PyroUbot import bot, OWNER_ID, ubot # [PERBAIKAN] Impor ubot
from PyroUbot.core.database.variabel import get_list_from_vars, remove_from_vars, get_vars, remove_vars
from PyroUbot.core.database.userbot import remove_ubot # [PERBAIKAN] Impor remove_ubot

userEXP = mongo_client["PyroUbot"]["users"]

async def get_expired_date(user_id: int):
    user = await userEXP.users.find_one({"_id": user_id})
    if user:
        return user.get("expire_date")
    else:
        return None

async def set_expired_date(user_id: int, expire_date: int):
    await userEXP.users.update_one(
        {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
    )

async def rem_expired_date(user_id: int):
    await userEXP.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )

# Fungsi check_if_already_tried menggunakan database
async def check_if_already_tried(user_id):
    """Check if user has already used free trial using database"""
    free_trial_users = await get_list_from_vars(bot.me.id, "FREE_TRIAL_USERS") or []
    return user_id in free_trial_users

# --- [FUNGSI KEDALUWARSA OTOMATIS YANG DIPERBAIKI] ---
async def check_expired_users():
    """Periksa dan hapus semua pengguna premium yang telah kedaluwarsa."""
    premium_users = await get_list_from_vars(bot.me.id, "PREM_USERS") or []
    
    for user_id in premium_users:
        # [PERBAIKAN] Hapus cek 'if user_id in free_trial_users'
        # Sekarang ini akan memeriksa SEMUA pengguna di PREM_USERS
        
        expired_date = await get_expired_date(user_id)
        if expired_date and expired_date < datetime.now():
            # Hapus dari daftar premium
            await remove_from_vars(bot.me.id, "PREM_USERS", user_id)
            
            # Hapus expired date dari database
            await rem_expired_date(user_id)
            
            # [PERBAIKAN] Hapus sesi bot dari database dan list
            if user_id in ubot._get_my_id:
                for X in ubot._ubot:
                    if user_id == X.me.id:
                        await X.unblock_user(bot.me.username)
                        await remove_ubot(X.me.id)  # Hapus dari database userbot
                        ubot._get_my_id.remove(X.me.id)
                        ubot._ubot.remove(X)
                        await X.log_out()
                        break
            
            # Beri tahu pengguna
            try:
                await bot.send_message(
                    user_id,
                    f"""
<blockquote><b>⏰ ᴍᴀsᴀ PREMIUM ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ</b>

<b>ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʟᴀʏᴀɴᴀɴ ᴋᴀᴍɪ. sᴇsɪ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs.</b>

<b>ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ, sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ: <a href=tg://openmessage?user_id={OWNER_ID}>@ibradecode</a> ᴀᴛᴀᴜ ᴊᴀʟᴀɴᴋᴀɴ ᴋᴏᴍᴀɴᴅᴏ /start</b></blockquote>
""",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("💰 ʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ", callback_data="bahan")]
                    ])
                )
            except Exception:
                pass
            
            # Beri tahu logs
            try:
                from PyroUbot import LOGS_MAKER_UBOT
                
                await bot.send_message(
                    LOGS_MAKER_UBOT,
                    f"""
<blockquote><b>⏰ PREMIUM ᴇxᴘɪʀᴇᴅ</b>
<b> ├ ᴜsᴇʀ ɪᴅ:</b> <code>{user_id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ ᴀᴛ:</b> <code>{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}</code></blockquote>
""",
                    disable_web_page_preview=True
                )
            except Exception:
                pass

# Function to get seller expiration date
async def get_seles_expired_date(user_id: int):
    """Get the expiration date for a seller account"""
    # Try to get from the database
    exp_date_str = await get_vars(bot.me.id, f"SELES_EXP_{user_id}")
    if exp_date_str:
        try:
            # Parse the date string to a datetime object
            return datetime.strptime(exp_date_str, "%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(f"Error parsing seller expiration date: {str(e)}")
    return None

# Function to check if a seller is permanent
async def is_permanent_seller(user_id: int):
    """Check if a user is a permanent seller"""
    perm_flag = await get_vars(bot.me.id, f"SELES_PERM_{user_id}")
    return perm_flag == "1"

# Function to check for expired sellers
async def check_expired_sellers():
    """Check and remove expired seller accounts"""
    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS") or []
    
    for user_id in seles_users:
        # Skip if it's the owner
        if user_id == OWNER_ID:
            continue
            
        # Check if user is a permanent seller
        is_permanent = await is_permanent_seller(user_id)
        if is_permanent:
            continue  # Skip expiration check for permanent sellers
        
        # Check expiration date
        expired_date = await get_seles_expired_date(user_id)
        if expired_date and expired_date < datetime.now():
            # Remove from sellers list
            await remove_from_vars(bot.me.id, "SELER_USERS", user_id)
            
            # Remove expiration data
            await remove_vars(bot.me.id, f"SELES_EXP_{user_id}")
            
            # Notify user
            try:
                await bot.send_message(
                    user_id,
                    f"""
<blockquote><b>⏰ MASA AKTIF RESELLER TELAH BERAKHIR</b></blockquote>

<blockquote><b>Status reseller Anda telah berakhir pada {expired_date.strftime('%d-%m-%Y %H:%M:%S')}</b></blockquote>

<blockquote><b>Untuk memperpanjang status reseller, silahkan hubungi:</b>
<b>👨‍💼 <a href=tg://openmessage?user_id={OWNER_ID}>@ibradecode</a></b></blockquote>

<blockquote><b>Atau gunakan perintah /start untuk memperpanjang secara otomatis</b></blockquote>
""",
                    disable_web_page_preview=True
                )
            except Exception:
                pass
            
            # Notify logs
            try:
                from PyroUbot import LOGS_MAKER_UBOT
                
                await bot.send_message(
                    LOGS_MAKER_UBOT,
                    f"""
<blockquote><b>⏰ SELLER EXPIRED</b></blockquote>
<blockquote><b> ├ USER ID:</b> <code>{user_id}</code></blockquote>
<blockquote><b> ╰ EXPIRED AT:</b> <code>{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}</code></blockquote>
""",
                    disable_web_page_preview=True
                )
            except Exception:
                pass

# Update the main check_expired_trials function to also check seller expirations
async def check_all_expirations():
    """Check both trial and seller expirations at bot startup"""
    # [PERBAIKAN] Ganti nama fungsi yang dipanggil
    await check_expired_users()
    
    # Check expired sellers
    await check_expired_sellers()

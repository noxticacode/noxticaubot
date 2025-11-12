# File: PyroUbot/modules/bakekok.py

from PyroUbot import *
import asyncio

__MODULE__ = "ʙᴀᴋᴇᴋᴏᴋ"
__HELP__ = """
<blockquote>Bantuan Untuk Bakekok

perintah : <code>{0}bakekok</code> [id_channel/group]
    untuk menyalin semua media, gif, dan berkas dari channel/group target.
    
Noted:
Proses ini mungkin memakan waktu lama tergantung jumlah media di target.
Pastikan akun userbot Anda telah bergabung ke channel/group target.</blockquote>
"""

@PY.UBOT("bakekok")
async def bakekok_command(client, message):
    """
    Menyalin semua media dari chat target ke chat saat ini.
    """
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    args = get_arg(message)
    if not args:
        await message.edit(f"{ggl} **Perintah tidak valid.**\n\n<b>Contoh:</b> <code>{0}bakekok -100123456789</code> atau <code>{0}bakekok @usernamechannel</code>")
        return

    # Tentukan ID target
    try:
        # Coba konversi ke integer (untuk ID chat -100...)
        target_chat_id = int(args)
    except ValueError:
        # Jika gagal, anggap sebagai username (untuk @username)
        target_chat_id = args

    # Beri pesan status awal
    try:
        status_msg = await message.edit(f"{prs} Memulai proses menyalin media dari <code>{target_chat_id}</code>...\n\nIni mungkin butuh waktu lama.")
    except Exception as e:
        await message.edit(f"{ggl} **Error:** Tidak dapat mengakses chat. Pastikan ID/username benar dan userbot Anda telah bergabung.\n\n<code>{e}</code>")
        return

    copied_count = 0
    total_checked = 0
    
    try:
        # Iterasi melalui seluruh riwayat chat dari target
        async for msg in client.get_chat_history(target_chat_id):
            total_checked += 1
            
            # Cek apakah pesan adalah media yang diminta (foto, video, gif/animasi, berkas/dokumen, audio, voice)
            if msg.photo or msg.video or msg.animation or msg.document or msg.audio or msg.voice:
                try:
                    # Salin pesan ke chat tempat perintah dieksekusi
                    await msg.copy(message.chat.id)
                    copied_count += 1
                    
                    # Tambahkan jeda 1 detik untuk menghindari FloodWait
                    await asyncio.sleep(1) 
                    
                except Exception as e:
                    # Jika gagal menyalin (mungkin karena FloodWait), jeda 5 detik
                    print(f"Gagal menyalin pesan {msg.id}: {e}")
                    await asyncio.sleep(5) # Jeda lebih lama jika terjadi error

            # Update status setiap 100 pesan yang diperiksa
            if total_checked % 100 == 0:
                await status_msg.edit(f"{prs} Memeriksa...\n\nTotal Pesan Diperiksa: {total_checked}\nTotal Media Disalin: {copied_count}")

        # Kirim pesan sukses setelah selesai
        await status_msg.edit(f"{sks} **Proses Salin Selesai!**\n\nTotal media berhasil disalin: <b>{copied_count}</b>\nTotal pesan diperiksa: <b>{total_checked}</b>")

    except Exception as e:
        await status_msg.edit(f"{ggl} **Terjadi error saat proses:**\n<code>{e}</code>")

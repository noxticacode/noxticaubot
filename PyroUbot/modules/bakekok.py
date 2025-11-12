# File: PyroUbot/modules/bakekok.py

from PyroUbot import *
import asyncio
import os  # <-- Penting untuk menghapus file

__MODULE__ = "ʙᴀᴋᴇᴋᴏᴋ"
__HELP__ = """
<blockquote>Bantuan Untuk Bakekok

perintah : <code>{0}bakekok</code> [id_channel/group]
    untuk menyalin semua media, gif, dan berkas dari channel/group target.
    
Noted:
Proses ini mungkin memakan waktu lama tergantung jumlah media di target.
Pastikan akun userbot Anda telah bergabung ke channel/group target.
<b>Modul ini menggunakan metode unduh-unggah untuk melewati batasan forward.</b></blockquote>
"""

@PY.UBOT("bakekok")
async def bakekok_command(client, message):
    """
    Menyalin semua media dari chat target ke chat saat ini.
    Menggunakan metode download-upload untuk bypass forward restrictions.
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
        target_chat_id = int(args)
    except ValueError:
        target_chat_id = args

    # Beri pesan status awal
    try:
        status_msg = await message.edit(f"{prs} Memulai proses menyalin media dari <code>{target_chat_id}</code>...\n\nMetode: <b>Download & Upload</b> (Untuk bypass restriksi).\nIni akan jauh lebih lambat.")
    except Exception as e:
        await message.edit(f"{ggl} **Error:** Tidak dapat mengakses chat. Pastikan ID/username benar dan userbot Anda telah bergabung.\n\n<code>{e}</code>")
        return

    copied_count = 0
    total_checked = 0
    
    try:
        # Iterasi melalui seluruh riwayat chat dari target
        async for msg in client.get_chat_history(target_chat_id):
            total_checked += 1
            caption = msg.caption or None
            
            # Cek media dan gunakan metode download-upload
            try:
                if msg.photo:
                    anu = await client.download_media(msg)
                    await client.send_photo(message.chat.id, anu, caption)
                    os.remove(anu)
                    copied_count += 1
                
                elif msg.video:
                    anu = await client.download_media(msg)
                    await client.send_video(message.chat.id, anu, caption)
                    os.remove(anu)
                    copied_count += 1
                    
                elif msg.animation: # Untuk GIF
                    anu = await client.download_media(msg)
                    await client.send_animation(message.chat.id, anu, caption)
                    os.remove(anu)
                    copied_count += 1

                elif msg.document:
                    anu = await client.download_media(msg)
                    await client.send_document(message.chat.id, anu, caption)
                    os.remove(anu)
                    copied_count += 1
                    
                elif msg.audio:
                    anu = await client.download_media(msg)
                    await client.send_audio(message.chat.id, anu, caption)
                    os.remove(anu)
                    copied_count += 1
                    
                elif msg.voice:
                    anu = await client.download_media(msg)
                    await client.send_voice(message.chat.id, anu) # Pesan suara tidak punya caption
                    os.remove(anu)
                    copied_count += 1
                
                # Tambahkan jeda 2 detik setelah operasi berhasil
                if msg.media:
                     await asyncio.sleep(2) # Beri jeda lebih lama karena proses download/upload berat

            except Exception as e:
                # Jika gagal (misal file terlalu besar atau error lain), log dan lanjutkan
                print(f"Gagal memproses pesan {msg.id}: {e}")
                await asyncio.sleep(5) # Jeda lebih lama jika terjadi error

            # Update status setiap 20 pesan (karena prosesnya lambat)
            if total_checked % 20 == 0:
                await status_msg.edit(f"{prs} Memeriksa...\n\nTotal Pesan Diperiksa: {total_checked}\nTotal Media Disalin: {copied_count}")

        # Kirim pesan sukses setelah selesai
        await status_msg.edit(f"{sks} **Proses Salin Selesai!**\n\nTotal media berhasil disalin: <b>{copied_count}</b>\nTotal pesan diperiksa: <b>{total_checked}</b>")

    except Exception as e:
        await status_msg.edit(f"{ggl} **Terjadi error saat proses:**\n<code>{e}</code>")

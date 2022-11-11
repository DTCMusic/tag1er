import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**𝐊 𝐎 𝐋 𝐆 Ə_𝐓 𝐀 𝐆 𝐆 𝐄 𝐑**⚡\n ilə Qrupunuzdakı Üyələri Etiket Edə Bilərəm\nƏmrlırlə Tanış olmaq üçün =======> /help yazın**",
                    buttons=(
                   
		      [Button.url('Beni Gruba Ekle ➕', 'https://t.me/kolgetaggerbot?startgroup=a')],
                      [Button.url('SAHİB 👮‍♂️', 'https://t.me/sesizKOLGE')],
                      [Button.url('DİGƏR BOTUM 🤖', 'https://t.me/menimbotlarim')],
		      [Button.url('OWNER 👨🏻‍💻', 'https://t.me/sesizKOLGE')],
		    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**𝐊 𝐎 𝐋 𝐆 Ə_𝐓 𝐀 𝐆 𝐆 𝐄 𝐑  Un Əmrləri **\n\n**/tag <səbəb> - 7-li Tağ Edər**\n\n**/etag <səbəb> - Emoji İlə Tağ Edər**\n\n**/tektag <səbəb> - Tək Teək Tağ Edər**\n\n**/admins <səbəb> - Yönəticiləri Tağ Edər(7-7)**\n\n**/start - Botu Başladar\n/reklam - Bot Haqda Qisa Məlumat**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Beni Gruba Ekle➕', 'https://t.me/kolgetaggerbot?startgroup=a')],
                      [Button.url('SAHİB 👮‍♂️', 'https://t.me/sesizKOLGE')],
                      [Button.url('DİGƏR BOTUM 🤖', 'https://t.me/menimbotlarim')],
		      [Button.url('OWNER 👨‍💻', 'https://t.me/sesizKOLGE')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Çox Özəllikli Tağ Botu Axtarmağa Çalışan Qrub Sahibləri  𝐊 𝐎 𝐋 𝐆 Ə_𝐓 𝐀 𝐆 𝐆 𝐄 𝐑  Bot Sizə Görə:\n\n📌 7-Li Tağ\n📌 7 Li Emoji İlə Tağ\n📌 Təkli Tağ\n📌 Yalnız Admimləri Tağ\n\n\nBelə Çox Özəllikli @kolgetaggerbot 'u Qrupunuza Yönətici Olaraq Alıb Rahatlıqla , Tağ edə bilirsiz **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Botu Gruba Ekle➕', 'https://t.me/kolgetaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri sadacə Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş Mesajlar Üçin Tağ Edə Bilmirəm **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tağ Eləmək Üçün Bir Səbəb yox❗️")
  else:
    return await event.respond("**📢 Tağ ı Başlatmaq Üçün Bir Səbəb Yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Tağ Prosesi Uğurla Durduruldu**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu\n\n**📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @sesizKOLGE**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Yanlız Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ Əvvəlki Mesajlara Cavab Verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Prosesi Başlatmaq Üçün Səbəb yoxdur ❗️")
  else:
    return await event.respond("❌ Tağ Edmək Üçün Səbəb Yox ")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu**\n\n📢 Burda Sizin Reklamınız Ola Bilər\n\n☎️ Əlaqə:- @sesizKOLGE**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Proses Uğurla Sonlandırıldı**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Sadacə Arminlər İadifadə Edə Bilər 〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Əvvəlki Mesajı Tağ Edə Bilmərəm*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamaq Üçün Səbəb Yazın❗️")
  else:
    return await event.respond("**ℹ Prosesə Başlamağım Üçün səbəb Yazın..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**➢ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan: 
        await event.respond("**✅ Proses Uğurla Durduruldu\n\n**\n\n📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @sesizKOLGE****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("✅ Proses Uğirla Durduruldu\n\n**📢 Burda Sizin Reklamınlz Ola Bilər\n☎️ Əlaqə:- @sesizKOLGE**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel')) 
async def cancel(event): 
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id) 
    
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}") 
  
@client.on(events.NewMessage()) 
async def mentionalladmin(event): 
  global etiketuye 
  if event.is_group: 
     if event.chat_id in etiketuye: 
       pass 
     else: 
       etiketuye.append(event.chat_id) 
  
  
  
 @client.on(events.NewMessage(pattern="^/tagg ?(.*)")) 
 async def mentionall(event): 
   global anlik_calisan 
   rxyzdev_tagTot[event.chat_id] = 0 
   if event.is_private: 
     return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.") 
    
   admins = [] 
   async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins): 
     admins.append(admin.id) 
   if not event.sender_id in admins: 
     return await event.respond("**Bu komutu sadece yöneticiler kullanabilir. 🐙**") 
    
   if event.pattern_match.group(1): 
     mode = "text_on_cmd" 
     msg = event.pattern_match.group(1) 
   elif event.reply_to_msg_id: 
     mode = "text_on_reply" 
     msg = event.reply_to_msg_id 
     if msg == None: 
         return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__") 
   elif event.pattern_match.group(1) and event.reply_to_msg_id: 
     return await event.respond("Bana bir metin verin.") 
   else: 
     return await event.respond("**Etikete Başlamak için sebep yazın... 🐙\n\n(Örnek: /tag Herkese Merhaba!)**") 
    
   if mode == "text_on_cmd": 
     anlik_calisan.append(event.chat_id) 
     usrnum = 0 
     usrtxt = "" 
     await event.respond("**✅ Etiket işlemi başladı. 🐙**") 
          
     async for usr in client.iter_participants(event.chat_id, aggressive=False): 
       rxyzdev_tagTot[event.chat_id] += 1 
       usrnum += 1 
       usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , " 
       if event.chat_id not in anlik_calisan: 
         return 
       if usrnum == 7: 
         await client.send_message(event.chat_id, f"**{msg}**\n{usrtxt}") 
         await asyncio.sleep(3) 
         usrnum = 0 
         usrtxt = "" 
          
     sender = await event.get_sender() 
     rxyzdev_initT = f"\n🐙 - [{sender.first_name}](tg://user?id={sender.id})" 
     if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}") 
    
   if mode == "text_on_reply": 
     anlik_calisan.append(event.chat_id) 
   
     usrnum = 0 
     usrtxt = "" 
     async for usr in client.iter_participants(event.chat_id, aggressive=False): 
       rxyzdev_tagTot[event.chat_id] += 1 
       usrnum += 1 
       usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , " 
       if event.chat_id not in anlik_calisan: 
         return 
       if usrnum == 7: 
         await client.send_message(event.chat_id, usrtxt, reply_to=msg) 
         await asyncio.sleep(3) 
         usrnum = 0 
         usrtxt = "" 
       
     sender = await event.get_sender() 
     rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"       
     if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiketlenen Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}") 
 


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=1
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot Uğurla İşləyir. Narahat olma 🚀 @sesizKOLGE dən məlumat ala bilırsən<<")
client.run_until_disconnected()

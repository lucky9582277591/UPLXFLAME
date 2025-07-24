await editable.edit("📛 𝗘𝗻𝘁𝗲𝗿 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 📛\n\n🐥 𝗦𝗲𝗻𝗱 `1` 𝗙𝗼𝗿 𝗨𝘀𝗲 𝗗𝗲𝗳𝗮𝘂𝗹𝘁 🐥")
input3: Message = await bot.listen(editable.chat.id)
raw_text3 = input3.text
await input3.delete(True)
# Default credit message with link
credit = "️[𝗧𝘂𝘀𝗵𝗮𝗿](https://t.me/Tushar0125)"
if raw_text3 == '1':
    CR = '[𝗧𝘂𝘀𝗵𝗮𝗿](https://t.me/Tushar0125)'
elif raw_text3:
    try:
        text, link = raw_text3.split(',')
        CR = f'[{text.strip()}]({link.strip()})'
    except ValueError:
        CR = raw_text3  # In case the input is not in the expected format, use the raw text
else:
    CR = credit

await editable.edit("**𝗘𝗻𝘁𝗲𝗿 𝗣𝘄 𝗧𝗼𝗸𝗲𝗻 𝗙𝗼𝗿 𝗣𝘄 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗼𝗿 𝗦𝗲𝗻𝗱 `3` 𝗙𝗼𝗿 𝗢𝘁𝗵𝗲𝗿𝘀**")
input4: Message = await bot.listen(editable.chat.id)
raw_text4 = input4.text
await input4.delete(True)
if raw_text4 == '3':
    MR = token
else:
    MR = raw_text4

await editable.edit("𝗡𝗼𝘄 𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗧𝗵𝘂𝗺𝗯 𝗨𝗿𝗹 𝗘𝗴 » https://graph.org/file/13a89d77002442255efad-989ac290c1b3f13b44.jpg\n\n𝗢𝗿 𝗜𝗳 𝗗𝗼𝗻'𝘁 𝗪𝗮𝗻𝘁 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗦𝗲𝗻𝗱 = 𝗻𝗼")
input6: Message = await bot.listen(editable.chat.id)
raw_text6 = input6.text
await input6.delete(True)
await editable.delete()

if raw_text6.lower() == "no":
    thumb = "no"
else:
    thumb = raw_text6

failed_count = 0
if len(links) == 1:
    count = 1
else:
    count = int(raw_text)

try:
    for i in range(count - 1, len(links)):
        V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
        url = "https://" + V

        if "visionias" in url:
            async with ClientSession() as session:
                async with session.get(url, headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Pragma': 'no-cache',
                    'Referer': 'http://www.visionias.in/',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'cross-site',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                }) as resp:
                    text = await resp.text()
                    url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

        elif 'media-cdn.classplusapp.com/drm/' in url:
            url = f"https://dragoapi.vercel.app/video/{url}"

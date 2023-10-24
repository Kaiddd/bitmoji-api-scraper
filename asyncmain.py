import asyncio
import aiohttp
import json
import re

gender = "2"

thenumber = 0

url = "https://preview.bitmoji.com/bm-preview/v3/avatar/body?scale=1&gender={}&style=5&rotation=0&beard=-1&blush_tone=16299718&body=7&breast=1&brow=1575&clothing_type=0&ear=1430&earringL_lobe1=14&earringL_lobe1_tone1=6646385&earringL_lobe1_tone2=16316410&earringL_lobe1_tone3=16316410&earringL_lobe1_tone4=16316410&earringR_lobe1=14&earringR_lobe1_tone1=6646385&earringR_lobe1_tone2=16316410&earringR_lobe1_tone3=16316410&earringR_lobe1_tone4=16316410&eye=1616&eyelash=2279&eyeshadow_tone=14725305&eye_size=2&eye_spacing=0&face_proportion=1&glasses=-1&hair=1706&hair_tone=2566954&hair_treatment_tone=16764902&hat=8663&hat_tone1=3355443&hat_tone2=3355443&hat_tone3=3355443&hat_tone4=3355443&hat_tone5=3355443&hat_tone6=3355443&hat_tone7=3355443&hat_tone8=3355443&hat_tone9=3355443&jaw=1407&lipstick_tone=14588595&mouth=2344&nose=1490&outfit={}&pupil=2152&pupil_tone=0&skin_tone=16765370&version=0"


async def excepted_get(session,i):
    try:
        return await session.get(url.format(gender, str(i)), ssl=False)
    except Exception:
        return None


def get_tasks(session):
    tasks = []
    for i in range(thenumber,thenumber+1000000):
        tasks.append(asyncio.create_task(excepted_get(session,i)))
    return tasks


async def read_data(stream_reader):
    data = await stream_reader.read(1024)
    
    if isinstance(data, str):
        data = data.encode('utf-8')


async def get_outfits():
    global thenumber
    regex = re.compile("&outfit=.*?&")
    regex2 = re.compile("&outfit=|&")
    while thenumber < 100000000:
        print(thenumber)
        timeout = aiohttp.ClientTimeout(total=600)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            tasks = get_tasks(session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                if response != None and response.status == 200 and response.text != "":
                    filename = regex2.sub('',re.search(regex,str(response.url)).group(0))
                    with open("./imgs2/"+filename+".webp","wb") as outf:
                        outf.write(await response.content.read())
        thenumber += 1000000


asyncio.run(get_outfits())
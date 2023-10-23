import requests
import json

counter = 900000

while True:
    counter += 1
    try:
        if counter % 1000 == 0:
            print(counter)
        url = "https://preview.bitmoji.com/bm-preview/v3/avatar/body?scale=1&gender=2&style=5&rotation=0&beard=-1&blush_tone=16299718&body=7&breast=1&brow=1575&clothing_type=0&ear=1430&earringL_lobe1=14&earringL_lobe1_tone1=6646385&earringL_lobe1_tone2=16316410&earringL_lobe1_tone3=16316410&earringL_lobe1_tone4=16316410&earringR_lobe1=14&earringR_lobe1_tone1=6646385&earringR_lobe1_tone2=16316410&earringR_lobe1_tone3=16316410&earringR_lobe1_tone4=16316410&eye=1616&eyelash=2279&eyeshadow_tone=14725305&eye_size=2&eye_spacing=0&face_proportion=1&glasses=-1&hair=1706&hair_tone=2566954&hair_treatment_tone=16764902&hat=8663&hat_tone1=3355443&hat_tone2=3355443&hat_tone3=3355443&hat_tone4=3355443&hat_tone5=3355443&hat_tone6=3355443&hat_tone7=3355443&hat_tone8=3355443&hat_tone9=3355443&jaw=1407&lipstick_tone=14588595&mouth=2344&nose=1490&outfit="+str(counter)+"&pupil=2152&pupil_tone=0&skin_tone=16765370&version=0"

        response = requests.request("GET", url)

        if response.status_code == 200 and response.text != "":
            with open("./imgs/"+str(counter)+".webp","wb") as outf:
                outf.write(response.content)
    except Exception:
        pass

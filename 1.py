rocket={'speed':30 , 'height':0} # soraate avalie  va  ertefae avalie
heights=[]#ليست براي ذخيره ارتفاع
time=0 # زمان شروع
while rocket['height']<100 : # حلقه رو تکرار کن تا زماني که ارتفاع به 100 برسه
    time+=1  #يکي اضافه کن  ثانيه ها رو يکي 
    rocket['height']=rocket['speed']*time  # طبق رابزه h=vt ارتفاع جديد رو حساب کن
    heights.append(rocket['height'])# ارتفاع جديد رو به ليست اضافه کن
    if rocket['height']>=50: # اگر ارتفاع از 50 بيشتر شد پيام زير رو چاپ کن
        print('موشک داه به فضا نزديک ميشهگ')
    if rocket['height']>=100: # اگر ارتفاع به 100 يل بيشتر رسيد پيغام زير رو چاپ کن
        print('The rocket reached space')
    else:
        print('The rocket still has a way to go') # در غير اين صورت بگو موشک هنوز راه داره
    if rocket['height']<0: # اگر ارتفاع کتر از صفر شد بگو موشک سقوط کرد
        print('The rocket crashed')
        #break

print('height=',heights)
speed=[rocket['speed']]
while rocket['speed']<=30: # مي خوام سرعت رو کم کنم يا بگم نثلا در اثر جاذبه سرعت داره کم ميشه 
    rocket['speed']-=1
    speed.append(rocket['speed'])
    if rocket['speed']<=0:# اگر سرعت 0 شد بگو ديگه بالاتر نميره
        print('The rocket can not go any higher')
        break
print('speed=',speed)

    


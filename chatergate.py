import vk
import time
import datetime
 
session = vk.Session(access_token="21f9450c821b598e48415877aff99a22e71264fc18e421ef1a319e0e5690bc99a64a87a5600dd76c8f23d")
vk_api = vk.API(session, v='5.62')
print("Версия v2 "*5)
ass = vk_api.messages.getDialogs(count=10)
print("Список бесед:")
for msg in ass['items']:
    if 'chat_id' in msg['message']:
        print(msg['message']['title'], "|чат-айди »",
              msg['message']['chat_id'], "«")
print("====chaterGate====")
#while True:
##try:
targetchat = int(input("Введите id чата для анализа: "))
targetchat = vk_api.messages.getChat(chat_id=targetchat)
# except Exception as e:
#      print("Нет такого чат-айди введите верный!!!")
#      continue
targetuser = targetchat["users"]
i = len(targetuser) 
cnt = 0
step = 5
while cnt < i:
    tmpusers = targetuser[cnt:cnt + step]
    response = vk_api.users.get(user_ids=tmpusers, fields="first_name,last_name,sex,bdate,last_seen")
    for user in response:
        try:
                print("»Профиль: {} {}, пол: {}, дата рождения: {}".format(user["first_name"], user["last_name"], user["sex"], user["bdate"]))
                tstamp = user["last_seen"]["time"]
                value = datetime.datetime.fromtimestamp(tstamp)
                print("»Последний визит:", value.strftime('%Y-%m-%d %H:%M:%S'))
        except Exception as e:
                print("Возникла ошибка у",vk_api.users.get(user_ids=targetuser)[0]["first_name"],vk_api.users.get(user_ids=targetuser)[0]["last_name"],"невозможно получить: {}".format(e))
    cnt += step
    time.sleep(0.5)

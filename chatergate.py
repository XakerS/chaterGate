import vk
import time
import datetime

#timestamp = 1339521878.04


session=vk.Session(access_token="ТОКЕН СЮДА!")
vk_api = vk.API(session, v='5.62')
print("Версия v1 "*5)
ass=vk_api.messages.getDialogs(count=10)
print("Список бесед:")
for msg in ass['items']:
           if 'chat_id' in msg['message']:
               print(msg['message']['title'],"|чат-айди »",msg['message']['chat_id'],"«")
print("====chaterGate====")
targetchat=int(input("Введите id чата для анализа: "))
targetchat=vk_api.messages.getChat(chat_id=targetchat)
targetuser=targetchat["users"]
print(targetuser)
i=len(targetuser)
for o in range(len(targetuser)):
 #print(vk_api.users.get(user_ods=o,fields="sex"))
 print("Профиль: ",vk_api.users.get(user_ids=targetuser[o])[0]['first_name'],vk_api.users.get(user_ids=targetuser[o])[0]['last_name'],"Пол:",vk_api.users.get(user_ids=targetuser[o],fields="sex")[0]["sex"],"Дата рождения:",vk_api.users.get(user_id=targetuser[o],fields="bdate")[0]["bdate"])
 timestamp=vk_api.users.get(user_id=targetuser[o],fields="last_seen")[0]["last_seen"]["time"]
 value = datetime.datetime.fromtimestamp(timestamp)
 print("Последний визит:",value.strftime('%Y-%m-%d %H:%M:%S'))
 time.sleep(2)
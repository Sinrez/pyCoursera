import dbm

db = dbm.open('captions','c')
db['foto.png'] = 'фото пользователя'
db['foto.png'] = 'фото на прогулке юзера'

# for key in db:
#     print(qkey, db[key])
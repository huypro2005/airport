from app.models.Chuyenbay import Chuyenbay
from app import db
from library import *

c = Chuyenbay.query.all()

for i in c:
    print(i)
    print(i.id)
    print(i.sanbaydi)
    print(i.sanbayden)
    print(i.giokhoihanh)
    print(i.giave)
    print(i.thoigianbay)
    print(i.maybayid)
    print(i.hangveid)
    print(i.trangthai)
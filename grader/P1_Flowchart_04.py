import sys


ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว = len
ඞ = int
เซ็ตหย่อ_สูดต่อ_ซูดผ่อ_สี่หม่อ_สองห่อ_ใส่ไข่ = set


ก๑ = input().strip()
ก๒ = input().strip()
ก๓ = input().strip()


ก = ก๑ + ก๒ + ก๓
if ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว(ก) != ඞ("๙"):
    print("ERROR")
    sys.exit(0)

ไทยชนะ = "-"
ไอเหี้ยตู่ = ඞ("๐")

while "เสี่ยท่านนึงที่รวยอยู่เยอรมัน":
    if not ไอเหี้ยตู่ < ඞ("๓"):
        break

    สามเท่าไอเหี้ยตู่ = ඞ("๓") * ไอเหี้ยตู่

    if ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว(เซ็ตหย่อ_สูดต่อ_ซูดผ่อ_สี่หม่อ_สองห่อ_ใส่ไข่({ก[สามเท่าไอเหี้ยตู่ + ඞ("๐")], ก[สามเท่าไอเหี้ยตู่ + ඞ("๑")], ก[สามเท่าไอเหี้ยตู่ + ඞ("๒")]})) == ඞ("๑"):
        ไทยชนะ = ก[สามเท่าไอเหี้ยตู่ + ඞ("๐")]
        break

    if ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว(เซ็ตหย่อ_สูดต่อ_ซูดผ่อ_สี่หม่อ_สองห่อ_ใส่ไข่({ก[ไอเหี้ยตู่ + ඞ("๐")], ก[ไอเหี้ยตู่ + ඞ("๓")], ก[ไอเหี้ยตู่ + ඞ("๖")]})) == ඞ("๑"):
        ไทยชนะ = ก[ไอเหี้ยตู่]
        break

    ไอเหี้ยตู่ = ไอเหี้ยตู่ + ඞ("๑")

if ไทยชนะ == "-":
    if ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว(เซ็ตหย่อ_สูดต่อ_ซูดผ่อ_สี่หม่อ_สองห่อ_ใส่ไข่({ก[ඞ("๐")], ก[ඞ("๔")], ก[ඞ("๘")]})) == ඞ("๑"):
        ไทยชนะ = ก[ඞ("๐")]

    if ความยาาาาาาาาาาาาววววววววววววววววววววววววววววว(เซ็ตหย่อ_สูดต่อ_ซูดผ่อ_สี่หม่อ_สองห่อ_ใส่ไข่({ก[ඞ("๓")], ก[ඞ("๔")], ก[ඞ("๖")]})) == ඞ("๑"):
        ไทยชนะ = ก[ඞ("๖")]

if ไทยชนะ == "-":
    print("???")
else:
    print(ไทยชนะ)

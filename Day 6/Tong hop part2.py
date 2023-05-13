# Bài 2 dict
import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list:": [
            "Speak to Me",
            "Breathe",
            "On the Run",
            "Time",
            "The Great Gig in the Sky",
            "Money",
            "Us and Them",
            "Any Coulour You Like",
            "Brain Damage",
            "Eclipse"
    ]
}
"""Yêu cầu
1. Lấy ra giá trị của các key sau:album_name,release_year bằng 2 cách 
"""
print(album_info["album_name"])
print(album_info.get("album_name"))

print(album_info["release_year"])
print(album_info.get("release_year"))
# 2.Thay đổi giá trị của:release_year từ 1973 thành 1971
album_info["release_year"] = 1971
print(json.dumps(album_info, indent=4))
# 3.Xóa phần từ với key là track_list

del album_info["track_list:"]
print(json.dumps(album_info, indent=4))
# 4.Thêm một key mới là amount = 2000 bằng 2 cách
album_info.update(amount=2000)
album_info["amount1"] = 3000
print(album_info)
# 5.Làm trống dict: album_info
album_info.clear()
print(album_info)

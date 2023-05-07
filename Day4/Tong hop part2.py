#1. Cho một danh sách (list) friends = ["Jen","Jack","Kenny","Jelly","Bob","Hẻny","Anne"]
friends = ["Jen","Jack","Kenny","Jelly","Bob","Henry","Anne"]
print (friends)
#a.Lấy ra 4 người bạn đầu tiên trong friends

new_list_friend_terminal = friends[0:4:]
print (new_list_friend_terminal) 
#b.Lấy ra 4 người bạn cuối trong friend 

new_list_friend_end = friends[3:]
print (new_list_friend_end) 
#c.Đảo ngược danh sách friends 

"""c_firends = friends[::-1]#start= 0  , stop = max , sep = -1 => 0+ -1 = -1 chạy từ cứ như thế in ra từ -1 đến 0
print (c_firends)"""

friends.reverse()
print (friends)
#d.Lấy ra những người bạn từ vị trí số 1 đến hết 

new_list_friend_terminal_1 = friends[1:]
print (new_list_friend_terminal_1)
#e.Copy danh sách ban đầu thành một danh sách mớii

friends_two = friends
print (friends_two)
#f.Lấy ra những người bạn từ vị trí số 2 đến sát cuối

friends_termial_one = friends[2:-1]#friends[2:6:]
print (friends_termial_one)




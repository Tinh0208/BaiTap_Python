USER_MENU = """ Nhập
a - Thêm vào bộ phim mới
l - Hiển thị danh sách phim
s - Tìm kiếm các bộ phim theo tên
x - Xóa phim theo tên
u - Cập nhật thông tin phim
q - thoát
Lựa chọn của bạn:  """

movies = []

preves = set()

#Thêm phim mới
def add_movie():
    name_movie = input("Nhập tên bộ phim:\t ")
    while name_movie in preves:
        print("Tên phim bị trùng,vui lòng nhập lại")
        name_movie = input("Nhập tên bộ phim:\t ")
    director = input("Nhập vào tên đạo diễn:\t ")
    release_year = input("Nhập vào năm phát hành:\t ")
    # Tạo data cho tập dữ liệu phim
    movie = {
        'name' : name_movie,
        'director' : director, # đạo diễn
        'release_year': release_year # năm phát hành 
    }

    # thêm vào danh sách phim
    movies.append(movie)
    preves.add(name_movie)
    print("Add successful movie .")# add phim thành công(successful)

# Hiển thị thông tin chi tiết phim = Display detailed movie information    
# detail = chi tiết, Display = trưng bày
def show_movie(movie):
    movie_name = movie['name']
    movie_director = movie['director']
    movie_release_year = movie['release_year']
    print(f'Tên bộ phim t: {movie_name}')
    print(f'Đạo diễn\t: {movie_director}')
    print(f'Năm phát hành\t: {movie_release_year}')
#Hiển thị các bộ phim = show all movie 
def show_movies():
    if movies:
        for idx,movie in enumerate(movies,start=1):
            print("Thông tin bộ phim: ",idx)
            show_movie(movie)
    else:
        print("Dánh sách phim trống!") 
#Search by movie name = Tìm kiếm theo tên phim 
def search_movie():
    if movies:
        movie_name = input("Nhập vào tên phim: ")
        for idx,movie in enumerate(movies,start=1):
            if movie['name'] == movie_name:
                print("Thông tin bộ phim: ",idx)
                show_movie(movie)
                break
            else:
                print('Không tìm thấy tên phim: ',movie_name)
        else:
            print("Dánh sách phim trống!")         
#Delete by movie name 
def remove_movie():
    if movies:
        movie_name = input("Nhập vào tên phim: ")
        for idx,movie in enumerate(movies,start=1):
            if movie['name'] == movie_name:
                del movies[idx]
                print('Đã xóa thành công')
                break
            else:
                print('Không tìm thấy tên phim: ',movie_name)
        else:
            print("Dánh sách phim trống!")       

#Update info movie
def update_movie():
    if movies:
        movie_name = input("Nhập vào tên phim: ")
        founds = [
            idx 
            for idx,movie in enumerate(movies)
            if movie['name'] == movie_name
        ]
        if founds:
            position = founds[0]
            movies[position]['director']   = input("Nhập vào tên đạo diễn:\t ")
            movies[position]['release_year'] = input("Nhập vào năm phát hành:\t ")
            
            print("Cập nhật phim thành công thành công")
            print('-'*20)
            # print('Thong tin bo phim sau khi cap nhat la')
            # show_movie(idx)
        else:
                print('Không tìm thấy tên phim: ',movie_name)
    else:
        print("Dánh sách phim trống!")               

#Nhập vào sự lựa chọn của người dùng = Enter the user's choice
#choice = sự lựa chọn , còn selection là lựa chọn 
user_choice = input(USER_MENU)

#Định nghĩa các sự lựa chọn bằng dict = Define options using dict
operations ={
    'a': add_movie,
    'l': show_movies,
    's': search_movie,
    'x':remove_movie,
    'u':update_movie
}
while user_choice != 'q':
    if user_choice in operations:
        operation = operations[user_choice]
        operation()
    else:
        print("Lựa chonk không hợp lệ hãy nhập lại")   
    #Nhập lại sự chọn của người dùng = Re- enter the user's selection
    user_choice = input(USER_MENU)

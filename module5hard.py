from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.nickname)

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __repr__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration      # продолжительность, секунды
        self.time_now = time_now      # секунда остановки
        self.adult_mode = adult_mode  # ограничение по возрасту

    def __eq__(self, other):
        return self.title.upper() == other.title.upper()

    def __hash__(self):
        return hash(self.title.upper())

    def __contains__(self, item):
        if item.upper() in self.title.upper():
            return True

    def __repr__(self):
        return f"'{self.title}'"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None  # текущий пользователь

    def log_in(self, login, password):
        user_new = User(login, password, 0)
        for user in self.users:
            if user == user_new and hash(user.password) == hash(password):
                self.current_user = user
                break

        else:
            print(f"Пользователя {login} не существует")

    def register(self, nickname, password, age):
        user_new = User(nickname, password, age)
        if user_new in self.users:
            print(f"Пользователь {nickname} уже существует")

        else:
            self.users.append(user_new)
            self.current_user = user_new

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for obj in args:
            if not isinstance(obj, Video):
                continue

            if not (obj in self.videos):
                self.videos.append(obj)

    def get_videos(self, find_str: str) -> list:
        result = []
        for video in self.videos:
            if find_str in video:
                result.append(video)

        return result

    def watch_video(self, video_name):
        video_find = Video(video_name, 0)
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        if not (video_find in self.videos):
            return

        index = self.videos.index(video_find)
        video = self.videos[index]
        self.show(video, self.current_user.age)

    def show(self, video: Video, user_age: int):
        if video.adult_mode and user_age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for i in range(video.time_now+1, video.duration+1):
            print(i, end=" ")
            sleep(1)

        video.time_now = 0
        print("Конец видео")

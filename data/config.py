from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5564855599:AAFo5fyqQYgN8NzEcjoA3VKIhZ92Oh-fCWk"  # Bot toekn
ADMINS = [1649621185]  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

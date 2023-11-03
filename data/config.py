from environs import Env


env = Env()
env.read_env()


TOKEN = env('TOKEN')
admin = env('admin')


admin_ids = [admin]

from twython import Twython

C_KEY = "ATiON7Rxxxxxxxxxxxxxxxxxxrb"
C_SECRET = "Tox1KBtpC8bQub98xxxxxxxxxxxxMDA1hgbtpZguMU3FpaXw8CT3YB5"
A_TOKEN = "4914151872-1UOofoJ4xxxxxxxxxx3qr8NYZo7Z7mCqgpfvRdMi"
A_SECRET = "VMAGKh66cER0qhwT14xxxxxxxxxxxxxxLiIwOKqh9FYffiXHc"

api = Twython (C_KEY, C_SECRET, A_TOKEN, A_SECRET)
api.update_status(status= "Hi abhishekcentos!")

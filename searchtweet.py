from twython import TwythonStreamer
i=0
C_KEY = "ATiON7RDMFjjVtQpBExfNpNrb"
C_SECRET = "Tox1KBtpC8bQub984AcI0PxMDA1hgbtpZguMU3FpaXw8CT3YB5"
A_TOKEN = "4914151872-1UOofoJ4DmgNrktYV3qr8NYZo7Z7mCqgpfvRdMi"
A_SECRET = "VMAGKh66cER0qhwT14NP5XqxjkrXLiIwOKqh9FYffiXHc"

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        global i
        if 'text' in data:
            if i < 3:
		i=i+1
            else:
                print("Ian G. Harris is popular")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
stream.statuses.filter(track= "Ian G. Harris")

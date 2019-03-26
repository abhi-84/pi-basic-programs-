from twython import TwythonStreamer

global i

i=0

class MyStreamer (TwythonStreamer):

    def on_success(self, data):

        global i

        print(i)

        if 'text' in data:

            if (i+1)%3 == 0:

                print "Who is Abhishek.centos"

            i=i+1



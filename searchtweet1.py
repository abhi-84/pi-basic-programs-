from twython import TwythonStreamer

global i

i=0

class MyStreamer (TwythonStreamer):

    def on_success(self, data):

        global i

        print(i)

        if 'text' in data:

            if (i+1)%3 == 0:

                print "Ian G. Harris is popular!"

            i=i+1



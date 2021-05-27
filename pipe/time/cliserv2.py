import os
from datetime import datetime


def servidor(w):
    wf = os.fdopen(w, 'w')
    now = datetime.now()
    now_str = now.strftime("%H:%M:%S")
    wf.write(now_str)
    wf.close()
      

def cliente(r):
    rf = os.fdopen(r)
    now = rf.read()
    print(now)
    rf.close()


def lanzador():
    r, w = os.pipe()
    if os.fork():
        # padre
        print("padre {}".format(os.getpid()))
        if os.fork():
            # padre
            print("padre {}".format(os.getpid()))
        else:
            # hijo
            print("hijo 2 {}".format(os.getpid()))
            os.close(r)
            servidor(w)

    else:
        # hijo
        print("hijo 1 {}".format(os.getpid()))
        os.close(w)
        cliente(r)


if __name__ == "__main__":
    lanzador()


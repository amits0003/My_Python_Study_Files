from Common.WCR_public import *

def try_fun():
    wcr_user_act.user_action("test input")

if __name__ == '__main__':
    try:
        try_fun()
    except:
        raise


argfile = '/home/furkankykc/Desktop/twBot.txt'


def readFile():
    try:
        filename = open(argfile, 'r')
        f = filename.readlines()
        print(f)
        filename.close()

    except IOError:
        filename = open(argfile, 'w')
        filename.close()


def writeFile(username, access_token, access_token_secret):
    filename = open(argfile, 'a')
    filename.write(username + '\t' + access_token + '\t' + access_token_secret + '\n')
    filename.close()

#! /usr/bin/python

from initium_ai import InitiumAI

def main():
    iai = InitiumAI('chrome')
    # iai = initium_ai('phantomjs')

    while True:
        # wait for user input
        usr_in = input("Accepting commands: ")
        print('AIA recieved {}'.format(usr_in))

        if usr_in.lower() in ['q', 'quit', 'exit']:
            print('Exiting.')
            break
        elif usr_in.lower() in ['start', 'go']:
            # open up the browser, navigate to main site, and login
            iai.start()
        elif usr_in.lower() in ['recon', 'reconnect']:
            # open up the browser, navigate to main site, and login
            iai.reconnect()
        elif usr_in.lower() in ['s', 'status']:
            # open up the browser, navigate to main site, and login
            iai.status()
        else:
            print('Unknown command: {}'.format(usr_in))

if __name__ == '__main__':
    main()

'''
most useful is rest/defend or explore/loot loop

'''
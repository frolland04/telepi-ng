#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys

file = __file__.split('\\')[-1]

print(file, 'HELLO!')

stop = False

while not stop:
    try:
        print('>>> GO')

        # On se reverra dans 3s
        time.sleep(3)

        # raise (Exception('aaaabbbb'))
        # or
        # sys.exit(0)
        # or
        # hit [CTRL-C]

    except (KeyboardInterrupt, SystemExit) as e:
        print('>>> INTERRUPTED !', e)
        stop = True

    except BaseException as e:
        # En cas de souci, on quitte la boucle
        print('>>> BASE EXCEPTION RAISED !', e)
        stop = True

    except Exception as e:
        # En cas de souci, on quitte la boucle
        print('>>> EXCEPTION RAISED !', e)
        stop = True

    else:
        print('No Problem. (ELSE)')

    finally:
        print('Executed. (FINALLY)')

    print('>>> STOP?', stop)

# Message final
print('<<< STOP')

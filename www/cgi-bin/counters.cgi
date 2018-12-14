#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import telepi_cgi


# -------------------------------------------------------
#
# -------------------------------------------------------

if __name__ == "__main__":
    """
    Exemple d'une 'cgi' en Python, 100% faite à la main :-)
    """
    print('Content-type: text/html; charset=UTF-8\n\n')
    print('<!DOCTYPE html>')
    print("<html lang='FR'>")

    print('<head>')
    print("<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>")
    print('<title>CGI PYTHON</title>')
    print('<link rel="stylesheet" type="text/css" href="ss/style.css" />')
    print('</head>')

    print('<body>')
    print('<p>Coucou depuis la CGI Python!</p>')
    print('</body>')
    print('</html>')

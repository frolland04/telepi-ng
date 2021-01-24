import sys


def read_table_rows(cs, name, nb, order='', reverse=False):
    """
    Lecture des N lignes d'une table
    """
    opt = ''

    if order != '':
        opt = ' order by ' + order
        if reverse:
            opt += ' desc'

    sql = 'select * from ' + name + opt + ' limit ' + str(nb)

    try:
        cs.execute(sql)

        s = cs.fetchall()
        d = cs.description

    except Exception as e:
        print('Unable to fetch data from table', name, '!<br><br>', e, '<br><br>')
        sys.exit(1)

    print('<table>')
    print('<th colspan=', len(d), '>Fetching', nb, 'data from table', name, '..</th>')
    print('<tr>')
    for hdr_idx in range(len(d)):
        print('<th>', d[hdr_idx][0], '</th>')
    print('</tr>')

    for row_idx in range(len(s)):
        print('<tr>')
        for hdr_idx in range(len(d)):
            print('<td>', s[row_idx][hdr_idx], '</td>')
        print('</tr>')

    print('</table>')
    print('<br>')
    return


# ---------------------------------------------
#

def read_table_for_unique_row(cs, name):
    """
    Lecture d'une ligne de la table
    """
    sql = 'select * from ' + name

    try:
        cs.execute(sql)

        s = cs.fetchall()
        d = cs.description

    except Exception as e:
        print('Unable to fetch data from table', name, '!<br><br>', e, '<br><br>')

    i = 0

    print('<table>')
    print('<th colspan=3>Fetching data. Table', name, '..</th>')

    while i < len(d):
        print('<tr>')
        print('<td>', i, '</td>')
        print('<td>', d[i][0], '</td>')
        print('<td>', s[0][i], '</td>')
        print('</tr>')
        i = i + 1

    print('</table>')
    print('<br>')
    return


def execute_request_for_unique_value(cs, sql):
    """
    Lecture du résultat unique d'une requête
    """
    try:
        cs.execute(sql)

        s = cs.fetchall()

    except Exception as e:
        print('Unable to fetch data !', '<br><br>', e)

    return s[0][0]

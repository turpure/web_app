#!usr/bin/env/python
# -*- coding:utf_8 -*-
import MySQLdb


def insert_kw(owner,kw):
    query = "insert into category_kw_dict (key_words,owner,curdate) values (%s,%s, now())"
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
        cur = con.cursor()
        cur.execute(query, (kw, owner,))
        con.commit()
        # print "insert %s into database" % kw
        con.close()
    except Exception as e:
        print e


if __name__ == "__main__":
    insert_kw("james", "outdoor")

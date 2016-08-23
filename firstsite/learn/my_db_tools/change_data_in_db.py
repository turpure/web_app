#!usr/bin/env/python
# -*- coding:utf_8 -*-
import MySQLdb


def insert_kw(owner, kw):
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


def insert_user(owner, user):
    query = "insert into shop_user_dict (user_name,owner, curdate) values (%s,%s, now())"
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
        cur = con.cursor()
        cur.execute(query, (user, owner,))
        con.commit()
        con.close()
    except Exception as e:
        print e


def remove_item(itemid, owner):
    query = "delete from "+ owner +"_kw_items where itemid=%s"
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
        cur = con.cursor()
        cur.execute(query, (itemid,))
        con.commit()
        # print "remove %s from database" % itemid
        con.close()
    except Exception as e:
        print e


def set_sku(itemid, sku):
    query = "update is_recommend set sku=%s where itemid=%s"
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
        cur = con.cursor()
        cur.execute(query, (sku,itemid))
        con.commit()
        print " set %s from database" % itemid
        con.close()
    except Exception as e:
        print e


if __name__ == "__main__":
    # insert_kw("james", "outdoor")
    # insert_user('test', 'lovingpets99')
    # remove_item('112015783996', 'sxb')
    set_sku('112095726345', 'sxb')

#!usr/bin/env/python
# -*- coding:utf_8 -*-
import  MySQLdb


def get_data(owner):
    query = "select galleryurl,title,location,startttime,quantitysold,currentprice,itemid,currency from %s_kw_items where quantitysold+0 > 0 and datediff(curdate,startttime)<8" % owner
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='',db='ebaydata')
        cur = con.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(query)
        for item in cur.fetchall():
            item['title'] = unicode("<a href='http://www.ebay.com/itm/" +item['itemid'] + "' target='_Blank'>" + item['title'] + "</a>", errors='replace')
            item['galleryurl'] = "<img src='"+ item['galleryurl'] +"' width='80' height='80'>"
            item['startttime'] = str(item['startttime'])
            item['quantitysold'] = str(item['quantitysold'])
            item['location'] = unicode(item['location'], errors='replace')
            yield item
        con.close()
    except Exception as e:
        print e


if __name__ == "__main__":
    print [ i for i in get_data("sxb")]

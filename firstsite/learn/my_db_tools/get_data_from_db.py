#!usr/bin/env/python
# -*- coding:utf_8 -*-
import  MySQLdb


def get_data(owner):
    query = "select galleryurl,title,location,starttime,quantitysold,currentprice,itemid from %s_kw_items where quantitysold+0 > 0 and datediff(curdate,starttime)<8" % owner
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='',db='ebaydata')
        cur = con.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(query)
        for item in cur.fetchall():
            item['title'] = unicode("<a href='http://www.ebay.com/itm/" +item['itemid'] + "'>" + item['title'] + "</a>", errors='replace')
            item['galleryurl'] = "<img src='"+ item['galleryurl'] +"' width='80' height='80'>"
            item['starttime'] = str(item['starttime'])
            item['quantitysold'] = str(item['quantitysold'])
            item['location'] = unicode(item['location'], errors='replace')
            yield item
        con.close()
    except Exception as e:
        print e


if __name__ == "__main__":

    print [ item for item in get_data('sxb')]
#!usr/bin/env/python
# -*- coding:utf_8 -*-
import MySQLdb


def get_data(owner):
    query = "select b.*,cat.kw, is_recommend.pstatus from (select galleryurl,title,location,startttime,quantitysold,currentprice,itemid,currency,curdate from %s_kw_items where quantitysold+0 > 0 and datediff(curdate,startttime)<8) as b inner JOIN %s_category_items as cat on b.itemid=cat.itemid LEFT JOIN  is_recommend on is_recommend.itemid=cat.itemid" % (
    owner, owner)
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
            item['owner'] = owner
            item['curdate'] = str(item['curdate'])[:10]
            if item['pstatus'] == 1:
                item['pstatus'] = 'wanted'
            # if item['pstatus'] is None:
            #     item['pstatus'] = 'unknown'
            yield item
        con.close()
    except Exception as e:
        print e


def get_data_20_days(owner):
    query = "select b.*,cat.kw, is_recommend.pstatus from (select galleryurl,title,location,startttime,quantitysold,currentprice,itemid,currency,curdate from %s_kw_items where quantitysold+0 > 0 and datediff(curdate,startttime)<8) as b inner JOIN %s_category_items as cat on b.itemid=cat.itemid LEFT JOIN  is_recommend on is_recommend.itemid=cat.itemid" % (owner,owner)
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
            item['kw'] = unicode(item['kw'], errors='replace')
            item['curdate'] = str(item['curdate'])[:10]
            if item['pstatus'] == 1:
                item['pstatus'] = 'wanted'
            # if item['pstatus'] is None:
            #     item['pstatus'] = 'unknown'
            yield item
        con.close()
    except Exception as e:
        print e


def get_kw_data():
    query = "select Nid,key_words,owner,curdate from category_kw_dict order by nid desc"
    try:
        con = MySQLdb.connect(host='192.168.0.134',user='root',passwd='',db='ebaydata')
        cur = con.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(query)
        for kw in cur.fetchall():
            kw['key_words'] = unicode(kw['key_words'], errors='replace')
            kw['curdate'] = str(kw['curdate'])[:10]
            yield kw
    except Exception as e:
        print e


def wanted_product(itemid, owner):
    insert_query = "insert into is_recommend values (%s,1,%s,'___',now()) "
    check_query = 'select * from is_recommend where itemid=%s'
    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata');
        cur = con.cursor()
        if not cur.execute(check_query, (itemid,)):
            cur.execute(insert_query, (itemid, owner))
            con.commit()
            con.close()
    except Exception as e:
        print e


def get_wanted():
    # query = 'select wan.owner, wan.itemid,wan.curdate,detail.galleryurl,detail.title from is_recommend as wan Left JOIN  %s_kw_items as detail on wan.itemid=detail.itemid' % owner
    query = "select itemid,owner,curdate,sku from is_recommend"

    try:
        con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
        cur = con.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(query)
        id_owner = cur.fetchall()
        for item in id_owner:
            detail_query = "select title,galleryurl,itemid from " + item['owner']+ "_kw_items where itemid=%s"
            cur.execute(detail_query, (item['itemid'],))
            detail = cur.fetchone()
            detail['title'] = unicode(
                "<a href='http://www.ebay.com/itm/" + detail['itemid'] + "' target='_Blank'>" + detail['title'] + "</a>",
                errors='replace')
            detail['galleryurl'] = "<img src='" + detail['galleryurl'] + "' width='80' height='80'>"
            # yield item
            detail['owner'] = item['owner']
            detail['sku'] = item['sku']
            detail['curdate'] = str(item['curdate'])[:10]
            yield detail
        con.close()
    except Exception as e:
        print e


def alter_table(owner):
    # ['sxb','sxz','chy','ymm','ysl','wq']
    query = 'alter table %s_category_items drop column  flag' % owner
    con = MySQLdb.connect(host='192.168.0.134', user='root', passwd='', db='ebaydata')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()


if __name__ == "__main__":
    owner = ['sxb','sxz','chy','ymm','ysl','wq']
    for i in owner:
        alter_table(i)




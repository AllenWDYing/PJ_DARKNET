#-*-encoding:utf-8-*-
import invoice.config.db as db_config
table_name = "pe_invoice"


class PeInvoice:
    def __init__(self, dict_row=None):
        if dict_row:
            self.file_src = dict_row.get("file_src")
            self.file_target = dict_row.get("file_target")
            self.request_type = dict_row.get("request_type")
            self.idcard = dict_row.get("idcard")
            self.organ = dict_row.get("organ")
            self.vin = dict_row.get("vin")
            self.engine = dict_row.get("engine")
            self.price = dict_row.get("price")
            self.md5_code = dict_row.get("md5_code")
            self.id = dict_row.get("id")
            self.created = dict_row.get("created")
            self.modified = dict_row.get("modified")
            self.status = dict_row.get("status")
            self.file_name=dict_row.get("file_name")
        else:
            self.file_src = ''
            self.file_target = ''
            self.request_type = ''
            self.idcard = ''
            self.organ = ''
            self.vin = ''
            self.engine = ''
            self.price = 0.0
            self.md5_code = ''
            self.id = None
            self.created = None
            self.modified = None
            self.status = 0


def get_invoice_by_src(img_src):
    result = None
    sql = "select * from "+table_name+" where file_src= %s"
    db = db_config.get_db()
    row = db.get(sql, img_src)
    if row:
        result = PeInvoice(row)
    return result


def get_invoice_by_md5(md5_code):
    result = None
    sql = "select * from  "+table_name+" where md5_code= %s limit 1"
    db = db_config.get_db()
    row = db.get(sql, md5_code)
    if row:
        result = PeInvoice(row)
    return result


def insert(invoice):
    sql = "INSERT INTO  "+table_name+" (file_src,file_target,request_type,md5_code,file_name) VALUES (%s,%s,%s,%s,%s)"
    #print(sql)
    db = db_config.get_db()
    result =db.execute(sql, invoice.file_src,invoice.file_target,invoice.request_type,invoice.md5_code,invoice.file_name)
    return result


def update_idcardno_by_id(idcard,id):
    #print(idcard,id)
    sql = "UPDATE "+table_name+" set idcard = %s ,status =1 where id=%s "
    #print(sql)
    db = db_config.get_db()
    result = db.execute(sql, idcard,id)
    return result


def update_vin_by_id(vin,id):
    sql = "UPDATE "+table_name+" set vin = %s, status =1 where id=%s"
    db = db_config.get_db()
    result = db.execute(sql, vin,id)
    return result

def update_roganno_by_id(organ,id):
    sql = "UPDATE "+table_name+" set organ = %s, status =1 where id=%s"
    db = db_config.get_db()
    result = db.execute(sql, organ,id)
    return result


def query_unprocess_data(num):
    result = None
    sql = "SELECT * FROM "+table_name+" where status =0  order by id asc limit "+str(num)
    db = db_config.get_db()
    rows = db.query(sql)
    if rows and len(rows)>0:
        result=[]
        for row in rows:
            result.append(PeInvoice(row))
    return result


def query_unprocess_data_random(num):
    result = None
    sql = "SELECT * FROM "+table_name+" where status =0  order by RAND() limit "+str(num)
    db = db_config.get_db()
    rows = db.query(sql)
    if rows and len(rows)>0:
        result=[]
        for row in rows:
            result.append(PeInvoice(row))
    return result

def query_by_filename(filename):
    result = None
    sql = "SELECT * FROM "+table_name+" where file_name =%s "
    db = db_config.get_db()
    rows = db.query(sql,filename)
    if rows and len(rows)>0:
        result=[]
        for row in rows:
            result.append(PeInvoice(row))
    return result


def update_error_status_by_id(remark, id):
    sql = "UPDATE " + table_name + " set remark = %s, status =3 where id=%s"
    db = db_config.get_db()
    result = db.execute(sql, remark, id)
    return result


def update_unknow_status_by_id(id):
    sql = "UPDATE " + table_name + " set  status =6 where id=%s"
    db = db_config.get_db()
    result = db.execute(sql , id)
    return result


def query_data(start,limit):
    result = None
    sql = "SELECT * FROM "+table_name+" order by id asc limit %s,%s "
    db = db_config.get_db()
    rows = db.query(sql,start,limit)
    if rows and len(rows)>0:
        result=[]
        for row in rows:
            result.append(PeInvoice(row))
    return result
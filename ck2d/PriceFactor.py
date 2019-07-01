import win32com.client


def get_factor():
    """
    获取价格数据库中的系数设置
    :return:
    """
    # 建立数据库连接
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    DSN = 'PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=..\\kitdat\\YfStdWardrobePrice2017.mdb'
    conn.Open(DSN)

    # 打开一个记录集
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs_name = 'PriceFactor'
    rs.Open('[' + rs_name + ']', conn, 1, 3)



    rs.MoveFirst()  #光标移到首条记录
    factor = rs.Fields[0].Value # 获取价格数据库中的系数设置
    print(factor)

    # 关闭数据库
    conn.Close()

    return factor

def set_factor(new_factor):
    """
    设置价格数据库中的系数设置
    :return:
    """
    # 建立数据库连接
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    DSN = 'PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=..\\kitdat\\YfStdWardrobePrice2017.mdb'
    conn.Open(DSN)

    # 打开一个记录集
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs_name = 'PriceFactor'
    rs.Open('[' + rs_name + ']', conn, 1, 3)

    # 改
    sql = "Update " + rs_name + " Set Factor = " + str(new_factor)
    conn.Execute(sql)

    # 关闭数据库
    conn.Close()

    return True

if __name__ == '__main__':
    a = get_factor()
    print("价格系数是" + str(a))
    set_factor(7)
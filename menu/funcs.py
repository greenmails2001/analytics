from dateutil.rrule import rrule, MONTHLY
from django.db import connection


def pd_strftime(rows):
    if rows:
        rows = rows.strftime("%Y-%m-%d(%Hh)")
    return rows

def pd_tonumber(s):
    try:
        s1 = float(s)
        return s1
    except ValueError:
        return s


def my_custom_sql(sql):
        cursor = connection.cursor()
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [baz])
        #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [baz])

        cursor.execute(sql)
        #row = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            from jinja2._compat import izip
            row_dict = dict(izip(col_names, row))
            yield row_dict
        return
        return row


#convert pandas to json, có chèn thêm tên filter:là giá trị để javascript có thể filter
#vidu o day là 'site': 'S103'
#filter với 1 column, sẽ phat trien filter với multi column
def pd_tojson_withfilter(pd_data,pd_filter,column):
    json_data=[]
    for i, f in pd_filter.iterrows():
        pd_data_filter = pd_data[pd_data[column] == f[column]]
        json_data += [{'filter': f[column],
                       'data': list((value.values)),
                       'name': key} for key, value in pd_data_filter.items()]
    #print(json_data)
    return json_data

def pd_tojson_bycols(pd_data):
    json_data = [{'data': list((value.values)),
                   'name': key} for key, value in pd_data.items()]
    return json_data


def pd_tojson_byrows(pd_data):
    json_data=[]
    for i, d in pd_data.iterrows():
        list = {key:value for key,value in d.items()}
        json_data.append(list)

        #0./ list = {key:value for key,value in d.items()}
        #json_data.append(list) --->[{'SiteID': 'S103', 'SiteName': '203NHT-phần-thân-khuA'}, {'SiteID': 'S117', 'SiteName': '117_Sheraton-PL1,2'}, ..., {'SiteID': 'S127', 'SiteName': '47-Nguyen Tuan-phanngam'}]
        #1./ list={l for l in d}
        #json_data.append(list) --->[{'S103', '203NHT-phần-thân-khuA'}, {'117_Sheraton-PL1,2', 'S117'}, ..., {'47-Nguyen Tuan-phanngam', 'S127'}]
        #2./ list=[l for l in d]
        #json_data.append(list)# --->[['S103', '203NHT-phần-thân-khuA'], ['S117', '117_Sheraton-PL1,2'], ..., ['S127', '47-Nguyen Tuan-phanngam']]
    #print(json_data)
    return json_data
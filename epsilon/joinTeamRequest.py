from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime
from DAO import DAO


def team_request_load(dao, tid):
    # Get data for pending join team requests
<<<<<<< Updated upstream:epsilon/joinTeamRequest.py
    cur = mysql.connection.cursor()
    sql_q = '''SELECT uid, create_date, req_id FROM Request WHERE tid = %s AND sid = 3 ORDER BY create_date'''
    cur.execute(sql_q,(tid,))
    data = cur.fetchall()
=======
    sql_q = '''SELECT uid, creation_date, req_id FROM Request WHERE tid = %s AND sid = 3 ORDER BY creation_date'''
    data = dao.get_data(sql_q, (tid,))
>>>>>>> Stashed changes:epsilon/business.py
    return data

def team_request_accept(dao, req_id):
    # Update Request and Teams to reflect on accept action
    message = team_request_update(dao, req_id, 1)

    if message == None:
        sql_q = '''SELECT tid, uid FROM Request WHERE req_id = %s'''
        data = dao.get_data(sql_q, (req_id,))
        sql_q = '''INSERT INTO Teams VALUES (%s, %s, 3)'''
        update = (data[0][1])
        dao.updateRoleOfEmployee(update, 3)
        data = (data[0][0], data[0][1])
        dao.modify_data(sql_q, data)
        message = "Accept Successful!"
    return message

def team_request_decline(dao, req_id):
    # Update Request to reflect on decline action
    message = team_request_update(dao, req_id, 2)
    if message == None:
        message = "Decline Successful!"
    return message

def team_request_update(dao, req_id, status):
    sql_q = '''SELECT sid FROM Request WHERE req_id = %s'''
<<<<<<< Updated upstream:epsilon/joinTeamRequest.py
    cur.execute(sql_q,(req_id,))
    data = cur.fetchone()
    if data[0] == 3:
        sql_q = '''UPDATE Request Set sid = %s, seen = false WHERE req_id = %s'''
        data = (status, req_id)
        add_data(mysql, sql_q, data)
=======
    data = dao.get_data(sql_q, (req_id,))
    if data[0][0] == 3:
        sql_q = '''UPDATE Request Set sid = %s, last_update = %s, seen = false WHERE req_id = %s'''
        data = (status, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), req_id)
        dao.modify_data(sql_q, data)
>>>>>>> Stashed changes:epsilon/business.py
        return
    else:
        return "Status is not pending!"
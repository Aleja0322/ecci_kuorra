import web

db_host = 'h7xe2knj2qb6kxal.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'n2u2e874kz5jxuv2'
db_user = 'v3sa6hmu2epbf83x'
db_pw = 'y2o5ba1yh7ucyobi'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
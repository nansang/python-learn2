'''

数据库操作
show databases;
use [databasename];
create database [name];

数据库表操作
show tables;
create table [name]
    (

    );

数据操作
insert into ** values(**);
delete from ** where id = **;
update ** set ** = '*' where id = **;
select ** from **;

其它
主键
外键
左右连接
（这几个倒是不是很理解，后面还是要研究）

============================

python mysql API

1.插入数据; 2.删除数据; 3.修改数据; 4.查询数据;
connect(host,user,passwd,db)//连接数据库
cursor()//游标是做什么用的？（用来获得python执行Mysql命令的方法,也就是我们所说的操作游标）
cur.execute('sql语句')//要进行的sql数据处理
conn.commit()//提交到数据库执行（方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。）
cur.close()//关闭游标
conn.close()//断开连接

总共六步
'''
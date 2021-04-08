
show tables;
desc user;

insert into user values(null, "Dingdong", "gudboy@naver.com", "1234", "male", now());

select * from user;
select name, email, gender from user where no=10;

-- login
select no, name from user where email="gudboy@naver.com" and password = "1234";

-- update
update user set name = "둘리", password="1234" where no="1";

-- delete 
delete from user where name="JJ";


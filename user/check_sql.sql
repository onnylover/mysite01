
show tables;
desc user;

insert into user values(null, "Dingdong", "gudboy@naver.com", "1234", "male", now());

-- login
select no, name from user where email="gudboy@naver.com" and password = "1234"

-- update
update user set name = "둘리", password="1234" where no="1";


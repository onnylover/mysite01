
show tables;
desc board;

select * from board;

-- select max(no) as max from board; -- g_no +1로 해결하면 될듯

select count(no) from board;
select a.g_no, a.o_no, a.depth, a.title, b.name, a.hit, a.reg_date from board a, user b where a.user_no = b.no order by a.g_no desc, a.o_no asc;
select a.g_no, a.o_no, a.depth, a.title, b.name, a.hit, a.reg_date from board a, user b where a.user_no = b.no order by a.g_no desc, a.o_no asc limit 0,2;

-- 검색
select a.g_no, a.o_no, a.depth, a.title, b.name, a.hit, a.reg_date from board a, user b where a.user_no = b.no order by a.g_no desc, a.o_no asc;

select title, contents, user_no, g_no, o_no from board where no = 10;

insert into board values(null, "test1", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,1,1,0,now(),11);
insert into board values(null, "test1-1", "테스트테스트테스트테스트. \n 줄바꿈도 확인해봅니다.\n 줄바꿈도 확인해봅니다.", 1,1,2,1,now(),11);
insert into board values(null, "test2", "테스트입니다. 테스트입니다. \n 테스트입니다.", 1,2,1,0,now(),11);
insert into board values(null, "test2-2", "테스트2222 입니다. 테스트입니다. \n 테스트입니다.", 1,2,3,2,now(),11);
insert into board values(null, "test2-2-1", "테스트33333 입니다. 테스트입니다. \n 테스트입니다.", 1,2,2,1,now(),11);
insert into board values(null, "test3", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,3,1,0,now(),11);
insert into board values(null, "test4", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,4,1,0,now(),11);
insert into board values(null, "test8", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,8,1,0,now(),11);
insert into board values(null, "test9", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,9,1,0,now(),11);
insert into board values(null, "test10", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,10,1,0,now(),11);
insert into board values(null, "test11", "테스트입니다. 일단 글 쓰고 봅니다 \n 줄바꿈도 확인해봅니다", 1,11,1,0,now(),11);


-- 사용자 번호로 작성자 join
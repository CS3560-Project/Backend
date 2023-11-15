INSERT INTO user(username,useremail,userpassword)
VALUES ('test','test','test')

-- @block
SELECT * FROM user where useremail = "tt@cpp.edu";
-- @block
show tables
-- @block
drop table user
-- @block
select * from message
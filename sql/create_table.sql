
create table if not exists `department`
       (dept_name varchar(20),
        building varchar(20),
	budget numeric(12,2),
	primary key (dept_name)
       ) charset=utf8;

create table if not exists `instructor`
       (ID varchar(5),
        name varchar(20),
	dept_name varchar(20),
	salary numeric(8,2),
	primary key (ID),
	foreign key (dept_name) references department(dept_name)
       ) charset=utf8;

create table if not exists `course`
       (course_id varchar(7),
        title varchar(50),
	dept_name varchar(20),
	credits numeric(2,0),
	primary key (course_id),
	foreign key (dept_name) references department(dept_name)
       ) charset=utf8;


create table if not exists `section`
       (course_id varchar(8),
        sec_id varchar(8),
	semester varchar(6),
	year numeric(4,0),
	building varchar(20),
	room_number varchar(7),
	time_slot_id varchar(4),
	primary key (course_id, sec_id, semester, year),
	foreign key (course_id) references course (course_id)
       ) charset=utf8;

create table if not exists `teaches`
       (ID varchar(5),
        course_id varchar(8),
	sec_id varchar(8),
	semester varchar(6),
	year numeric(4,0),
	primary key (ID, course_id, sec_id, semester, year),
	foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year),
	foreign key (ID) references instructor (ID)
       ) charset=utf8;

create table if not exists `student`
       (ID varchar(5),
        name varchar(20) not null,
	dept_name varchar(20),
	tot_cred numeric(3,0) default 0,
	primary key (ID),
	foreign key (dept_name) references department (dept_name)
       ) charset=utf8;
       

create table if not exists `takes`
       (ID varchar(5),
        course_id varchar(8),
	sec_id varchar(8),
	semester varchar(6),
	year numeric(4,0),
	grade varchar(4),
	primary key (ID, course_id, sec_id, semester, year),
	foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year),
	foreign key (ID) references student (ID)
       ) charset=utf8;

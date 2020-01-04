create user IF NOT EXISTS `teleinfo` ;
alter user `teleinfo` identified by "ti" ;

create database IF NOT EXISTS `D_TELEINFO` DEFAULT CHARACTER SET utf8 ;
grant all on `D_TELEINFO`.`*` to `teleinfo` ;

create database IF NOT EXISTS `D_TEST` DEFAULT CHARACTER SET utf8 ;
grant all on `D_TEST`.`*` to `teleinfo` ;

use `D_TEST` ;

CREATE TABLE IF NOT EXISTS `T_TEST_SQL` (
  `Id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `msg` varchar(250) DEFAULT NULL,
  `val` bigint(20) DEFAULT NULL,
  `ts` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) DEFAULT CHARSET=utf8 ;

select * from `T_TEST_SQL` ;

insert into `T_TEST_SQL` set msg = 'hello' ;

select * from `T_TEST_SQL` ;



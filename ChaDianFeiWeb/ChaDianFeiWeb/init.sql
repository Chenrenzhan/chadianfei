CREATE DATABASE IF NOT EXISTS `chadianfei`;

CREATE TABLE IF NOT EXISTS `chadianfei_chadianfei`(
  `dorm` varchar(8),
  `mail` varchar(50),
  PRIMARY KEY (dorm,mail)
) DEFAULT CHARSET=utf8;

INSERT INTO `chadianfei_chadianfei` (`dorm`,`mail`) VALUES
('3313','dengzuoheng@gmail.com'),
('3313','chenrenzhan@gmail.com');
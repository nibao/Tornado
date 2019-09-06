
CREATE TABLE IF NOT EXISTS `t_users` (
  `f_id` binary(16) NOT NULL,
  `f_username` char(20) NOT NULL,
  `f_password` binary(32) NOT NULL,
  `f_enabled` tinyint(1) NOT NULL,
  `f_create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`f_id`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
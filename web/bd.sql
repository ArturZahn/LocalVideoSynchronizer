DROP DATABASE IF EXISTS `localvideossynchronizer`;
CREATE DATABASE `localvideossynchronizer`;
USE `localvideossynchronizer`;

CREATE TABLE `connection` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `ip` VARCHAR(50)
);

CREATE TABLE `lastreset` (
    `cod` INT PRIMARY KEY,
    `time` DATETIME
);

CREATE TABLE `cmd` (
    `cmd_cod` INT PRIMARY KEY AUTO_INCREMENT,
    `numb` INT,
    `opt` VARCHAR(1000),
    `dt_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `cmd_executed` (
    `cmd_cod` INT,
    `id` INT,

    FOREIGN KEY (`cmd_cod`) REFERENCES `cmd` (`cmd_cod`),
    FOREIGN KEY (`id`) REFERENCES `connection` (`id`)
);

DELIMITER //



CREATE PROCEDURE `deleteOldCmds` ()
BEGIN

		SET @oldCmdList = (SELECT GROUP_CONCAT(cmd_cod) FROM cmd WHERE dt_created < DATE_ADD(NOW(),INTERVAL -2 SECOND));
		
		DELETE FROM cmd_executed WHERE FIND_IN_SET(cmd_cod, @oldCmdList) > 0;
		DELETE FROM cmd WHERE FIND_IN_SET(cmd_cod, @oldCmdList) > 0;
		
END //
 
DELIMITER ;


-- INSERT INTO `lastreset` (`cod`, `time`) VALUE (1, NOW());
INSERT INTO `lastreset` (`cod`, `time`) VALUE (1, '2021-11-20 15:51:54');
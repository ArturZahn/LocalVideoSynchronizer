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
    `opt` VARCHAR(1000)
);

CREATE TABLE `cmd_executed` (
    `cmd_cod` INT,
    `id` INT,

    FOREIGN KEY (`cmd_cod`) REFERENCES `cmd` (`cmd_cod`),
    FOREIGN KEY (`id`) REFERENCES `connection` (`id`)
);

-- INSERT INTO `lastreset` (`cod`, `time`) VALUE (1, NOW());
INSERT INTO `lastreset` (`cod`, `time`) VALUE (1, '2021-11-20 15:51:54');
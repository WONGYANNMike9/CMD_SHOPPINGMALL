/*
 Navicat Premium Data Transfer

 Source Server         : Tecent
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : 49.235.89.99:3306
 Source Schema         : comp7640

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 02/04/2022 20:02:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `cid` int NOT NULL AUTO_INCREMENT,
  `c_name` char(20) NOT NULL,
  `addr` char(20) NOT NULL,
  `tel` int NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`cid`) USING BTREE,
  UNIQUE INDEX `c_name`(`c_name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1, '111', 'shatin', 101, '109');
INSERT INTO `customer` VALUES (2, 'wa', 'shatin', 9299, '123456');
INSERT INTO `customer` VALUES (3, 'qingtian', 'shatin', 10086, '123');
INSERT INTO `customer` VALUES (4, 'samuel', 'samuel', 11111, 'abcd');
INSERT INTO `customer` VALUES (5, 'xxxx', 'xxxx', 1111, 'xxxx');
INSERT INTO `customer` VALUES (6, 'TAN', 'CHINA', 123456, '123456');

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `gid` int NOT NULL AUTO_INCREMENT,
  `g_name` char(20) NOT NULL,
  `sid` int NOT NULL,
  `tag1` char(20) NULL DEFAULT NULL,
  `tag2` char(20) NULL DEFAULT NULL,
  `price` float NULL DEFAULT NULL,
  `quantity` int NULL DEFAULT NULL,
  PRIMARY KEY (`gid`) USING BTREE,
  INDEX `fk_sid`(`sid` ASC) USING BTREE,
  CONSTRAINT `fk_sid` FOREIGN KEY (`sid`) REFERENCES `shop` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 10 ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES (1, 'GPhone22', 3, '512', 'White', 8888, 100);
INSERT INTO `goods` VALUES (10, 'iPhone13', 1, '256', 'Grey', 9999, 225);
INSERT INTO `goods` VALUES (11, 'Mate40', 4, '128', 'Pink', 6999, 14);

-- ----------------------------
-- Table structure for order_info
-- ----------------------------
DROP TABLE IF EXISTS `order_info`;
CREATE TABLE `order_info`  (
  `oid` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `createdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `o_gid` int NOT NULL,
  `o_cid` int NOT NULL,
  `o_quantity` int NOT NULL,
  PRIMARY KEY (`oid`, `o_gid`, `o_cid`) USING BTREE,
  INDEX `o_gid_idx`(`o_gid` ASC) USING BTREE,
  INDEX `o_cid_idx`(`o_cid` ASC) USING BTREE,
  CONSTRAINT `o_cid` FOREIGN KEY (`o_cid`) REFERENCES `customer` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `o_gid` FOREIGN KEY (`o_gid`) REFERENCES `goods` (`gid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of order_info
-- ----------------------------
INSERT INTO `order_info` VALUES (1, '2022-03-31 17:54:55', 10, 1, 5);
INSERT INTO `order_info` VALUES (1, '2022-03-30 15:54:58', 10, 2, 1);
INSERT INTO `order_info` VALUES (2, '2022-03-30 17:36:04', 10, 2, 2);

-- ----------------------------
-- Table structure for shop
-- ----------------------------
DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop`  (
  `sid` int NOT NULL AUTO_INCREMENT,
  `s_name` char(20) NOT NULL,
  `location` char(20) NULL DEFAULT NULL,
  `rating` int NULL DEFAULT NULL,
  PRIMARY KEY (`sid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shop
-- ----------------------------
INSERT INTO `shop` VALUES (1, 'apple', 'china', 1);
INSERT INTO `shop` VALUES (3, 'ai', 'china', 3);
INSERT INTO `shop` VALUES (4, 'Huawei', 'china', 5);
INSERT INTO `shop` VALUES (5, 'Samsung', 'Korea', 4);
INSERT INTO `shop` VALUES (6, 'OPPO', 'china', 1);

-- ----------------------------
-- Triggers structure for table order_info
-- ----------------------------
DROP TRIGGER IF EXISTS `order_info_AFTER_INSERT`;
delimiter ;;
CREATE TRIGGER `order_info_AFTER_INSERT` AFTER INSERT ON `order_info` FOR EACH ROW BEGIN
update goods
set quantity = quantity - new.o_quantity
where gid = new.o_gid;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table order_info
-- ----------------------------
DROP TRIGGER IF EXISTS `order_info_AFTER_DELETE`;
delimiter ;;
CREATE TRIGGER `order_info_AFTER_DELETE` AFTER DELETE ON `order_info` FOR EACH ROW BEGIN
update goods
set quantity = quantity + old.o_quantity 
where gid = old.o_gid;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;

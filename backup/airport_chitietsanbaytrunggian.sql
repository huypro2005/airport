-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: airport
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chitietsanbaytrunggian`
--

DROP TABLE IF EXISTS `chitietsanbaytrunggian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietsanbaytrunggian` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Ma_chuyen_bay` int DEFAULT NULL,
  `Ma_san_bay_trung_gian` varchar(20) DEFAULT NULL,
  `Thoi_gian_dung` int DEFAULT NULL,
  `Ghi_chu` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Ma_chuyen_bay` (`Ma_chuyen_bay`),
  KEY `Ma_san_bay_trung_gian` (`Ma_san_bay_trung_gian`),
  CONSTRAINT `CHITIETSANBAYTRUNGGIAN_ibfk_1` FOREIGN KEY (`Ma_chuyen_bay`) REFERENCES `chuyenbay` (`id`),
  CONSTRAINT `CHITIETSANBAYTRUNGGIAN_ibfk_2` FOREIGN KEY (`Ma_san_bay_trung_gian`) REFERENCES `sanbay` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietsanbaytrunggian`
--

LOCK TABLES `chitietsanbaytrunggian` WRITE;
/*!40000 ALTER TABLE `chitietsanbaytrunggian` DISABLE KEYS */;
INSERT INTO `chitietsanbaytrunggian` VALUES (1,18,'DNANG',15,'Tg 1'),(3,19,'DNANG',15,'Trung gian 1'),(4,19,'Vinh',15,'Trung gian 2'),(13,111,'HAIPHONG',20,'dừng ăn bánh đa cua'),(14,222,'VINH',15,'hẹ hẹ hẹ'),(15,55,'THANHHOA',15,'123'),(16,69,'HNOI',20,'60'),(17,88,'THANHHOA',10,'dừng nghỉ ăn cơm trưa'),(18,1235,'HUE',15,'ăn uống ngủ nghỉ'),(19,96,'HUE',12,'ngủ nghỉ ăn trưa'),(22,125,'SGON',10,'ngủ nghỉ ăn trưa'),(23,90,'HUE',10,'dừng ngủ trưa'),(24,90,'VINH',15,'thăm nhà Huy'),(25,65432,'VINH',60,'123'),(26,721,'HAIPHONG',50,'nghỉ'),(27,725,'HUE',50,'aaa'),(28,728,'UK',50,'55'),(29,801,'THANHHOA',15,'bbb'),(30,802,'UK',50,'aaa'),(31,888,'THANHHOA',50,'nghỉ ngơi'),(32,878,'THANHHOA',20,'nghỉ ngơi'),(33,878,'UK',30,'nghỉ ngơi'),(34,878,'VINH',50,'aaa'),(35,55555,'VINH',52,'55'),(36,55555,'VINH',45,'55'),(37,2708,'THANHHOA',30,'nghỉ ngơi'),(38,2708,'UK',30,'nghỉ ngơi'),(39,2106,'THANHHOA',30,'nghỉ ngơi '),(40,2106,'VINH',30,'nghỉ ngơi'),(41,564,'HNOI',12,'awn cowm ngu nghi');
/*!40000 ALTER TABLE `chitietsanbaytrunggian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-22 15:34:08

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
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` text,
  `email` varchar(120) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `tinhtrang` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
INSERT INTO `nhanvien` VALUES (2,'John Doe','john.doe','scrypt:32768:8:1$maO5Cd4knTAp2Tz0$acc538b853a57f6916bda69e1f3d4d5decc3e8aca4e34598d61f1c31272a33cd9dd2ff3be4d06caa71ab869ef4dd8ec12abfc148b21510a4484c0b95b205045e','john.doe@example.com','admin',1),(4,'Hello anh em','aaa','scrypt:32768:8:1$rfNlV0KjyRdGoPRU$2d8e9791f7a4f4fa1354ae8260d598d09fb7eec432706291bf668e4ad0f9da27326b464594ffc94b8bd823e3fad55a9bb40e76f531b50fb77f738b67bdfc37a0','hello@example.com','admin',1),(5,'John Doea','bbb','scrypt:32768:8:1$gpGf3PsLi5ALgdKB$66f86d5cd9571db05c6bf23045351fb93731f6b69378375e5e3d3dc994faec02d81716791d3caa8a09292489a77a3fd74b07dddf89a22c7238a9e2d9b4d858d5','john.do@example.com','stuff',1),(6,'Admin','admin','scrypt:32768:8:1$QG3dqSjDzUEGK7SG$bd3bd6aef4e5681e4345dc20ee4de80dd3dec18a37e6d51bc5c838a66ebc58ca85e78589b39a53396259bff376fa68907d76e58f5282b8c1007052ed6924751c','admin@gmail.com','admin',1);
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
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

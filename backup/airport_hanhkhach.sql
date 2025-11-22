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
-- Table structure for table `hanhkhach`
--

DROP TABLE IF EXISTS `hanhkhach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hanhkhach` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Hoten` varchar(50) NOT NULL,
  `cmnd` varchar(30) NOT NULL,
  `sdt` varchar(15) NOT NULL,
  `gioi_tinh` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmnd` (`cmnd`),
  UNIQUE KEY `sdt` (`sdt`),
  KEY `ix_HANHKHACH_id` (`id`),
  KEY `ix_HANHKHACH_Hoten` (`Hoten`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hanhkhach`
--

LOCK TABLES `hanhkhach` WRITE;
/*!40000 ALTER TABLE `hanhkhach` DISABLE KEYS */;
INSERT INTO `hanhkhach` VALUES (1,'nguyen van a','116468466314','24544346','Nam'),(2,'Nguyen Van A','123456780','0909090909','Nam'),(4,'nguyen van a','11646846614','2544346','Nam'),(6,'Nguyen Van A','123456','0908529599','Nam'),(7,'Hello aas','123434234','2645168','male'),(8,'Cao Thanh Huy','546861321','0353735497','female'),(9,'ant','123123','12423432','Nam'),(10,'abc','42345234','123353','Nữ'),(11,'đâsd','123124','124324','Nam'),(12,'học','34634324','5324123','Nam'),(13,'dfgdfg','124123','23453425','Nam'),(14,'test','457243','3457234','Nam'),(15,'tdgf','5123','345142134','Nam'),(16,'Nguyen thai hoc','054205000279','0859699488','Nam'),(23,'ânnnn','1234567890','0846006878','Nam'),(24,'Thanh huy','147896325456','0214567896','Nam'),(27,'Huy gg','147896325666','0598765432','Nam'),(28,'ffff  âsasa','777777777777','0211277777','Nam'),(29,'hello aaaa','147896325654','0466524833','Nam'),(30,'Huy Cao Tha','123654987789','0247896355','Nam'),(31,'Huy Cao T','123654987788','0258963147','Nam'),(32,'anh','123456789123','0223456789','Nam'),(33,'Nguyễn Văn Hoàng','365665656565','0232323232','Nam'),(35,'Nguyễn Văn Hoàng','123654987784','0353735491','Nam'),(36,'Tạ Ngọc Ân','123456789012','0345678901','Nam');
/*!40000 ALTER TABLE `hanhkhach` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-22 15:34:09

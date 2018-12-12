-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `football`
--

DROP TABLE IF EXISTS `football`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `football` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8_bin NOT NULL,
  `rfid` varchar(45) COLLATE utf8_bin NOT NULL,
  `position` varchar(45) COLLATE utf8_bin NOT NULL,
  `left-right` varchar(45) COLLATE utf8_bin NOT NULL,
  `in` int(11) DEFAULT '0',
  `out` int(11) DEFAULT '0',
  `field_goal` float DEFAULT '0',
  `contact_1` int(11) DEFAULT '0',
  `contact_2` int(11) DEFAULT '0',
  `contact_3` int(11) DEFAULT '0',
  `contact_4` int(11) DEFAULT '0',
  `goalzone_1` int(11) DEFAULT '0',
  `goalzone_2` int(11) DEFAULT '0',
  `goalzone_3` int(11) DEFAULT '0',
  `goalzone_4` int(11) DEFAULT '0',
  `goalzone_5` int(11) DEFAULT '0',
  `goal zone 6` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `rfid` (`rfid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `football`
--

LOCK TABLES `football` WRITE;
/*!40000 ALTER TABLE `football` DISABLE KEYS */;
/*!40000 ALTER TABLE `football` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-12 21:23:28

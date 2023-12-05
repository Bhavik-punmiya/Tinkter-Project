-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.48-MariaDB-0+deb9u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `instructors`
--

DROP TABLE IF EXISTS `instructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instructors` (
  `instructorID` tinyint(4) DEFAULT NULL,
  `name` varchar(14) DEFAULT NULL,
  `gender` varchar(4) DEFAULT NULL,
  `danceStyles` varchar(6) DEFAULT NULL,
  `telNo` bigint(20) DEFAULT NULL,
  `hrRate` decimal(3,1) DEFAULT NULL,
  `availability` varchar(9) DEFAULT NULL,
  `availableDays` varchar(6) DEFAULT NULL,
  `username` varchar(7) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instructors`
--

LOCK TABLES `instructors` WRITE;
/*!40000 ALTER TABLE `instructors` DISABLE KEYS */;
INSERT INTO `instructors` VALUES (9,'Bhavik Punmiya','Male','HipHop',8767856787,12.0,'AVAILABLE','Monday','Bhavik_','Bhavik0310'),(10,'Janhavi Nate ','Male','HipHop',87675876767,10.0,'AVAILABLE','','John','John1234');
/*!40000 ALTER TABLE `instructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sessions` (
  `sessionID` tinyint(4) DEFAULT NULL,
  `studentName` varchar(18) DEFAULT NULL,
  `danceStyle` varchar(8) DEFAULT NULL,
  `sessDate` varchar(10) DEFAULT NULL,
  `sessDay` varchar(9) DEFAULT NULL,
  `maxRate` decimal(5,1) DEFAULT NULL,
  `instructorName` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` VALUES (1,'Kalpana Wijethunga','Ballroom','29/10/2021','Friday',1000.0,'Hansi Radhakrishnan'),(2,'Adisha  Udunuwara','Zumba','16/11/2021','Tuesday',800.0,'Vihangi Rajapaksha'),(3,'Gihan Wanninayake','Salsa','27/10/2021','Wednesday',1200.0,' '),(4,'Kalpana Wijethunga','Ballroom','25/10/2021','Monday',900.0,'Gayani Kulathunga'),(5,'Gimhani Ranathunga','HipHop','16/11/2021','Tuesday',1250.0,' '),(6,'Navodi Kumarage','Zumba','31/10/2021','Sunday',1500.0,' '),(7,'Adisha  Udunuwara','Salsa','22/11/2021','Monday',1000.0,' ');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `studentID` tinyint(4) DEFAULT NULL,
  `firstName` varchar(7) DEFAULT NULL,
  `surName` varchar(11) DEFAULT NULL,
  `email` varchar(21) DEFAULT NULL,
  `DOB` varchar(10) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `telNo` bigint(20) DEFAULT NULL,
  `address` varchar(37) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Kalpana','Wijethunga','kalpanawije@gmail.com','01/02/2000','Female',817508901,'No:16,\nDiyatha Rd,\nColombo\n'),(2,'Gihan','Wanninayake','giha98@yahoo.com','08/07/1998','Male',764896752,'\"Sirini Niwasa\",\nPitipana,\nHomagama\n'),(3,'Gimhani','Ranathunga','gimhanirana@gmail.com','20/10/1999','Female',712809874,'No.53/2,\nSamagi Mawatha,\nKirbathgoda\n'),(4,'Adisha ','Udunuwara','adishau@gmail.com','03/04/2001','Male',776547899,'No: 32.\n4th Mile Post,\nPeliyagoda\n'),(5,'Navodi','Kumarage','navokuma98@yahoo.com','01/10/1999','Female',776587644,'354/2,\nLady Mannings Drive,\nKandana\n');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-18 10:46:24

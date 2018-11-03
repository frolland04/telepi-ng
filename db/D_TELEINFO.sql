-- MySQL dump 10.13  Distrib 5.5.60, for debian-linux-gnu (armv8l)
--
-- Host: localhost    Database: D_TELEINFO
-- ------------------------------------------------------
-- Server version	5.5.60-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `T_COUNTERS`
--

DROP TABLE IF EXISTS `T_COUNTERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_COUNTERS` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `RecvMsgNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgNbOk` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgNbBad` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgDataLineNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgDataLineNbOk` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgDataLineNbBad` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgDataLineNbUnsupp` bigint(20) unsigned NOT NULL DEFAULT '0',
  `RecvMsgLastTs` datetime DEFAULT NULL,
  `CleanHistoRunNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `CleanHistoLastRunTs` datetime DEFAULT NULL,
  `CleanHistoLastRunDelNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `CleanHistoLastRunHasNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoRunNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoLastRunTs` datetime DEFAULT NULL,
  `AutoMinMaxTeleinfoMinInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoMinDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoMinUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoMaxInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoMaxDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTeleinfoMaxUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaRunNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaLastRunTs` datetime DEFAULT NULL,
  `AutoMinMaxPaMinInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaMinDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaMinUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaMaxInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaMaxDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxPaMaxUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhRunNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhLastRunTs` datetime DEFAULT NULL,
  `AutoMinMaxRhMinInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhMinDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhMinUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhMaxInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhMaxDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxRhMaxUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempRunNb` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempLastRunTs` datetime DEFAULT NULL,
  `AutoMinMaxTempMinInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempMinDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempMinUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempMaxInsNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempMaxDelNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `AutoMinMaxTempMaxUpdNbTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvTemperatureNbReadTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvTemperatureNbReadOk` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvTemperatureNbReadFailed` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvTemperatureNbReadInvalid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvTemperatureReadLastTs` datetime DEFAULT NULL,
  `EnvRelativeHumidityNbReadTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvRelativeHumidityNbReadOk` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvRelativeHumidityNbReadFailed` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvRelativeHumidityNbReadInvalid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvRelativeHumidityReadLastTs` datetime DEFAULT NULL,
  `EnvAirPressureNbReadTotal` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvAirPressureNbReadOk` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvAirPressureNbReadFailed` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvAirPressureNbReadInvalid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `EnvAirPressureReadLastTs` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_COUNTERS`
--

LOCK TABLES `T_COUNTERS` WRITE;
/*!40000 ALTER TABLE `T_COUNTERS` DISABLE KEYS */;
INSERT INTO `T_COUNTERS` VALUES (0,0,0,0,0,0,0,0,NULL,0,NULL,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,NULL,0,0,0,0,NULL);
/*!40000 ALTER TABLE `T_COUNTERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_DBG_ENTRIES`
--

DROP TABLE IF EXISTS `T_DBG_ENTRIES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_DBG_ENTRIES` (
  `Id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `DbgMessage` varchar(60) DEFAULT NULL,
  `DbgContext` varchar(250) DEFAULT NULL,
  `DbgTs` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_DBG_ENTRIES`
--

LOCK TABLES `T_DBG_ENTRIES` WRITE;
/*!40000 ALTER TABLE `T_DBG_ENTRIES` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_DBG_ENTRIES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_HISTO`
--

DROP TABLE IF EXISTS `T_HISTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_HISTO` (
  `PTEC` varchar(2) NOT NULL,
  `PAPP` int(11) NOT NULL,
  `IINST` int(11) NOT NULL,
  `HC` int(11) NOT NULL,
  `HP` int(11) NOT NULL,
  `ETAT` int(11) NOT NULL,
  `TEMP` float NOT NULL,
  `RH` float NOT NULL,
  `PA` float NOT NULL,
  `TS` datetime NOT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=FIXED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_HISTO`
--

LOCK TABLES `T_HISTO` WRITE;
/*!40000 ALTER TABLE `T_HISTO` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_HISTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_PA_INST`
--

DROP TABLE IF EXISTS `T_PA_INST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_PA_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `PA` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=FIXED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_PA_INST`
--

LOCK TABLES `T_PA_INST` WRITE;
/*!40000 ALTER TABLE `T_PA_INST` DISABLE KEYS */;
INSERT INTO `T_PA_INST` VALUES (0,0,NULL);
/*!40000 ALTER TABLE `T_PA_INST` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`teleinfo`@`%`*/ /*!50003 TRIGGER `AutoMinMaxPaUpdInst` AFTER UPDATE ON `T_PA_INST` FOR EACH ROW BEGIN

   DECLARE OLD_PA_MIN INTEGER ;

   DECLARE OLD_PA_MAX INTEGER ;
   
   DECLARE TS_DATE DATE ;

   DECLARE TS_TIME TIME ;

   DECLARE DeletedNb INTEGER ;

   DECLARE InsertedNb INTEGER ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaRunNb = T_COUNTERS.AutoMinMaxPaRunNb + 1, T_COUNTERS.AutoMinMaxPaLastRunTs = NOW() ;

   SET @TS_DATE = DATE( NEW.TS ) ;

   SET @TS_TIME = TIME( NEW.TS ) ;

   INSERT T_PA_MIN SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, PA = 1000000000 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMinInsNbTotal = T_COUNTERS.AutoMinMaxPaMinInsNbTotal + @InsertedNb ;
   
   INSERT T_PA_MAX SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, PA = 0 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMaxInsNbTotal = T_COUNTERS.AutoMinMaxPaMaxInsNbTotal + @InsertedNb ;
  
   SET @OLD_PA_MIN = ( SELECT PA FROM T_PA_MIN WHERE T_PA_MIN.TS_DATE = @TS_DATE ) ;

   SET @OLD_PA_MAX = ( SELECT PA FROM T_PA_MAX WHERE T_PA_MAX.TS_DATE = @TS_DATE ) ;

   IF NEW.PA < @OLD_PA_MIN

   THEN

      UPDATE T_PA_MIN SET T_PA_MIN.PA = NEW.PA, T_PA_MIN.TS_TIME = @TS_TIME WHERE T_PA_MIN.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMinUpdNbTotal = T_COUNTERS.AutoMinMaxPaMinUpdNbTotal + 1 ;

   END IF ;
   
   IF NEW.PA > @OLD_PA_MAX

   THEN

      UPDATE T_PA_MAX SET T_PA_MAX.PA = NEW.PA, T_PA_MAX.TS_TIME = @TS_TIME WHERE T_PA_MAX.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMaxUpdNbTotal = T_COUNTERS.AutoMinMaxPaMaxUpdNbTotal + 1 ;

   END IF ;

   DELETE FROM T_PA_MIN WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMinDelNbTotal = T_COUNTERS.AutoMinMaxPaMinDelNbTotal + @DeletedNb ;
   
   DELETE FROM T_PA_MAX WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxPaMaxDelNbTotal = T_COUNTERS.AutoMinMaxPaMaxDelNbTotal + @DeletedNb ;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `T_PA_MAX`
--

DROP TABLE IF EXISTS `T_PA_MAX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_PA_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PA` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_PA_MAX`
--

LOCK TABLES `T_PA_MAX` WRITE;
/*!40000 ALTER TABLE `T_PA_MAX` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_PA_MAX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_PA_MIN`
--

DROP TABLE IF EXISTS `T_PA_MIN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_PA_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PA` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_PA_MIN`
--

LOCK TABLES `T_PA_MIN` WRITE;
/*!40000 ALTER TABLE `T_PA_MIN` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_PA_MIN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_RH_INST`
--

DROP TABLE IF EXISTS `T_RH_INST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_RH_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `RH` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=FIXED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_RH_INST`
--

LOCK TABLES `T_RH_INST` WRITE;
/*!40000 ALTER TABLE `T_RH_INST` DISABLE KEYS */;
INSERT INTO `T_RH_INST` VALUES (0,0,NULL);
/*!40000 ALTER TABLE `T_RH_INST` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`teleinfo`@`%`*/ /*!50003 TRIGGER `AutoMinMaxRhUpdInst` AFTER UPDATE ON `T_RH_INST` FOR EACH ROW BEGIN

   DECLARE OLD_RH_MIN INTEGER ;

   DECLARE OLD_RH_MAX INTEGER ;
   
   DECLARE TS_DATE DATE ;

   DECLARE TS_TIME TIME ;

   DECLARE DeletedNb INTEGER ;

   DECLARE InsertedNb INTEGER ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhRunNb = T_COUNTERS.AutoMinMaxRhRunNb + 1, T_COUNTERS.AutoMinMaxRhLastRunTs = NOW() ;

   SET @TS_DATE = DATE( NEW.TS ) ;

   SET @TS_TIME = TIME( NEW.TS ) ;

   INSERT T_RH_MIN SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, RH = 1000000000 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMinInsNbTotal = T_COUNTERS.AutoMinMaxRhMinInsNbTotal + @InsertedNb ;
   
   INSERT T_RH_MAX SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, RH = 0 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMaxInsNbTotal = T_COUNTERS.AutoMinMaxRhMaxInsNbTotal + @InsertedNb ;
  
   SET @OLD_RH_MIN = ( SELECT RH FROM T_RH_MIN WHERE T_RH_MIN.TS_DATE = @TS_DATE ) ;

   SET @OLD_RH_MAX = ( SELECT RH FROM T_RH_MAX WHERE T_RH_MAX.TS_DATE = @TS_DATE ) ;

   IF NEW.RH < @OLD_RH_MIN

   THEN

      UPDATE T_RH_MIN SET T_RH_MIN.PA = NEW.RH, T_RH_MIN.TS_TIME = @TS_TIME WHERE T_RH_MIN.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMinUpdNbTotal = T_COUNTERS.AutoMinMaxRhMinUpdNbTotal + 1 ;

   END IF ;
   
   IF NEW.RH > @OLD_RH_MAX

   THEN

      UPDATE T_RH_MAX SET T_RH_MAX.PA = NEW.RH, T_RH_MAX.TS_TIME = @TS_TIME WHERE T_RH_MAX.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMaxUpdNbTotal = T_COUNTERS.AutoMinMaxRhMaxUpdNbTotal + 1 ;

   END IF ;

   DELETE FROM T_RH_MIN WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMinDelNbTotal = T_COUNTERS.AutoMinMaxRhMinDelNbTotal + @DeletedNb ;
   
   DELETE FROM T_RH_MAX WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMaxDelNbTotal = T_COUNTERS.AutoMinMaxRhMaxDelNbTotal + @DeletedNb ;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `T_RH_MAX`
--

DROP TABLE IF EXISTS `T_RH_MAX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_RH_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `RH` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_RH_MAX`
--

LOCK TABLES `T_RH_MAX` WRITE;
/*!40000 ALTER TABLE `T_RH_MAX` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_RH_MAX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_RH_MIN`
--

DROP TABLE IF EXISTS `T_RH_MIN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_RH_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `RH` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_RH_MIN`
--

LOCK TABLES `T_RH_MIN` WRITE;
/*!40000 ALTER TABLE `T_RH_MIN` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_RH_MIN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_TELEINFO_HISTO`
--

DROP TABLE IF EXISTS `T_TELEINFO_HISTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TELEINFO_HISTO` (
  `PTEC` varchar(2) NOT NULL,
  `PAPP` int(11) unsigned NOT NULL,
  `IINST` int(11) unsigned NOT NULL,
  `HC` int(11) unsigned NOT NULL,
  `HP` int(11) unsigned NOT NULL,
  `ETAT` int(11) unsigned NOT NULL,
  `TEMPERATURE` float NOT NULL,
  `RH` float unsigned NOT NULL,
  `PRESSION_ATMOS` float unsigned NOT NULL,
  `TS` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`TS`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TELEINFO_HISTO`
--

LOCK TABLES `T_TELEINFO_HISTO` WRITE;
/*!40000 ALTER TABLE `T_TELEINFO_HISTO` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_TELEINFO_HISTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_TELEINFO_INST`
--

DROP TABLE IF EXISTS `T_TELEINFO_INST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TELEINFO_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `PTEC` varchar(2) NOT NULL DEFAULT '''''',
  `PAPP` int(11) unsigned NOT NULL DEFAULT '0',
  `IINST` int(11) unsigned NOT NULL DEFAULT '0',
  `HC` int(11) unsigned NOT NULL DEFAULT '0',
  `HP` int(11) unsigned NOT NULL DEFAULT '0',
  `ADCO` bigint(20) unsigned NOT NULL DEFAULT '0',
  `ISOUSC` int(11) unsigned NOT NULL DEFAULT '0',
  `OPTARIF` varchar(2) NOT NULL DEFAULT '''''',
  `HHPHC` varchar(2) NOT NULL DEFAULT '''''',
  `IMAX` int(11) unsigned NOT NULL DEFAULT '0',
  `ETAT` int(11) unsigned NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TELEINFO_INST`
--

LOCK TABLES `T_TELEINFO_INST` WRITE;
/*!40000 ALTER TABLE `T_TELEINFO_INST` DISABLE KEYS */;
INSERT INTO `T_TELEINFO_INST` VALUES (0,'\'\'',0,0,0,0,0,0,'\'\'','\'\'',0,0,NULL);
/*!40000 ALTER TABLE `T_TELEINFO_INST` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`teleinfo`@`%`*/ /*!50003 TRIGGER `AutoMinMaxTeleinfoUpdInst` AFTER UPDATE ON `T_TELEINFO_INST` FOR EACH ROW BEGIN

   DECLARE OLD_PAPP_MIN INTEGER ;

   DECLARE OLD_PAPP_MAX INTEGER ;
  
   DECLARE TS_DATE DATE ;

   DECLARE TS_TIME TIME ;

   DECLARE DeletedNb INTEGER ;

   DECLARE InsertedNb INTEGER ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoRunNb = T_COUNTERS.AutoMinMaxTeleinfoRunNb + 1, T_COUNTERS.AutoMinMaxTeleinfoLastRunTs = NOW() ;
   
   SET @TS_DATE = DATE( NEW.TS ) ;

   SET @TS_TIME = TIME( NEW.TS ) ;

   INSERT T_TELEINFO_MIN SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, PAPP = 10000000, IINST = 10000000 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMinInsNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMinInsNbTotal + @InsertedNb ;
   
   INSERT T_TELEINFO_MAX SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, PAPP = 0, IINST = 0 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMaxInsNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMaxInsNbTotal + @InsertedNb ;
  
   SET @OLD_PAPP_MIN = ( SELECT PAPP FROM T_TELEINFO_MIN WHERE T_TELEINFO_MIN.TS_DATE = @TS_DATE ) ;

   SET @OLD_PAPP_MAX = ( SELECT PAPP FROM T_TELEINFO_MAX WHERE T_TELEINFO_MAX.TS_DATE = @TS_DATE ) ;
   
   IF NEW.PAPP < @OLD_PAPP_MIN

   THEN

      UPDATE T_TELEINFO_MIN SET T_TELEINFO_MIN.PAPP = NEW.PAPP, T_TELEINFO_MIN.IINST = NEW.IINST, T_TELEINFO_MIN.TS_TIME = @TS_TIME WHERE T_TELEINFO_MIN.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMinUpdNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMaxInsNbTotal + 1 ;

   END IF ;
   
   IF NEW.PAPP > @OLD_PAPP_MAX

   THEN

      UPDATE T_TELEINFO_MAX SET T_TELEINFO_MAX.PAPP = NEW.PAPP, T_TELEINFO_MAX.IINST = NEW.IINST, T_TELEINFO_MAX.TS_TIME = @TS_TIME WHERE T_TELEINFO_MAX.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMaxUpdNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMaxUpdNbTotal + 1 ;

   END IF ;

   DELETE FROM T_TELEINFO_MIN WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMinDelNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMinDelNbTotal + @DeletedNb ;
   
   DELETE FROM T_TELEINFO_MAX WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTeleinfoMaxDelNbTotal = T_COUNTERS.AutoMinMaxTeleinfoMaxDelNbTotal + @DeletedNb ;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `T_TELEINFO_MAX`
--

DROP TABLE IF EXISTS `T_TELEINFO_MAX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TELEINFO_MAX` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PAPP` int(11) unsigned NOT NULL DEFAULT '0',
  `IINST` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TELEINFO_MAX`
--

LOCK TABLES `T_TELEINFO_MAX` WRITE;
/*!40000 ALTER TABLE `T_TELEINFO_MAX` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_TELEINFO_MAX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_TELEINFO_MIN`
--

DROP TABLE IF EXISTS `T_TELEINFO_MIN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TELEINFO_MIN` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PAPP` int(11) unsigned NOT NULL DEFAULT '0',
  `IINST` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TELEINFO_MIN`
--

LOCK TABLES `T_TELEINFO_MIN` WRITE;
/*!40000 ALTER TABLE `T_TELEINFO_MIN` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_TELEINFO_MIN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_TEMP_INST`
--

DROP TABLE IF EXISTS `T_TEMP_INST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TEMP_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TEMP` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=FIXED;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TEMP_INST`
--

LOCK TABLES `T_TEMP_INST` WRITE;
/*!40000 ALTER TABLE `T_TEMP_INST` DISABLE KEYS */;
INSERT INTO `T_TEMP_INST` VALUES (0,0,NULL);
/*!40000 ALTER TABLE `T_TEMP_INST` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`teleinfo`@`%`*/ /*!50003 TRIGGER `AutoMinMaxTempUpdInst` AFTER UPDATE ON `T_TEMP_INST` FOR EACH ROW BEGIN

   DECLARE OLD_TEMP_MIN INTEGER ;

   DECLARE OLD_TEMP_MAX INTEGER ;
   
   DECLARE TS_DATE DATE ;

   DECLARE TS_TIME TIME ;

   DECLARE DeletedNb INTEGER ;

   DECLARE InsertedNb INTEGER ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempRunNb = T_COUNTERS.AutoMinMaxTempRunNb + 1, T_COUNTERS.AutoMinMaxTempLastRunTs = NOW() ;

   SET @TS_DATE = DATE( NEW.TS ) ;

   SET @TS_TIME = TIME( NEW.TS ) ;

   INSERT T_TEMP_MIN SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, TEMP = 10000000 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMinInsNbTotal = T_COUNTERS.AutoMinMaxTempMinInsNbTotal + @InsertedNb ;
   
   INSERT T_TEMP_MAX SET TS_DATE = @TS_DATE, TS_TIME = @TS_TIME, TEMP = 0 ON DUPLICATE KEY UPDATE Id = Id ; 
   
   SET @InsertedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMaxInsNbTotal = T_COUNTERS.AutoMinMaxTempMaxInsNbTotal + @InsertedNb ;
  
   SET @OLD_TEMP_MIN = ( SELECT TEMP FROM T_TEMP_MIN WHERE T_TEMP_MIN.TS_DATE = @TS_DATE ) ;

   SET @OLD_TEMP_MAX = ( SELECT TEMP FROM T_TEMP_MAX WHERE T_TEMP_MAX.TS_DATE = @TS_DATE ) ;

   IF NEW.TEMP < @OLD_TEMP_MIN

   THEN

      UPDATE T_TEMP_MIN SET T_TEMP_MIN.TEMP = NEW.TEMP, T_TEMP_MIN.TS_TIME = @TS_TIME WHERE T_TEMP_MIN.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMinUpdNbTotal = T_COUNTERS.AutoMinMaxTempMinUpdNbTotal + 1 ;

   END IF ;
   
   IF NEW.TEMP > @OLD_TEMP_MAX

   THEN

      UPDATE T_TEMP_MAX SET T_TEMP_MAX.TEMP = NEW.TEMP, T_TEMP_MAX.TS_TIME = @TS_TIME WHERE T_TEMP_MAX.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMaxUpdNbTotal = T_COUNTERS.AutoMinMaxTempMaxUpdNbTotal + 1 ;

   END IF ;

   DELETE FROM T_TEMP_MIN WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMinDelNbTotal = T_COUNTERS.AutoMinMaxTempMinDelNbTotal + @DeletedNb ;
   
   DELETE FROM T_TEMP_MAX WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxTempMaxDelNbTotal = T_COUNTERS.AutoMinMaxTempMaxDelNbTotal + @DeletedNb ;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `T_TEMP_MAX`
--

DROP TABLE IF EXISTS `T_TEMP_MAX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TEMP_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `TEMP` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TEMP_MAX`
--

LOCK TABLES `T_TEMP_MAX` WRITE;
/*!40000 ALTER TABLE `T_TEMP_MAX` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_TEMP_MAX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `T_TEMP_MIN`
--

DROP TABLE IF EXISTS `T_TEMP_MIN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T_TEMP_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `TEMP` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `T_TEMP_MIN`
--

LOCK TABLES `T_TEMP_MIN` WRITE;
/*!40000 ALTER TABLE `T_TEMP_MIN` DISABLE KEYS */;
/*!40000 ALTER TABLE `T_TEMP_MIN` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-03  8:14:22

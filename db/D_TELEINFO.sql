-- Database `D_TELEINFO`

CREATE DATABASE IF NOT EXISTS `D_TELEINFO` DEFAULT CHARACTER SET utf8 ;
USE `D_TELEINFO`;

--
-- Table `T_COUNTERS`
--

CREATE TABLE IF NOT EXISTS `T_COUNTERS` (
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

--
-- Data of table `T_COUNTERS`
--

LOCK TABLES `T_COUNTERS` WRITE;
INSERT INTO `T_COUNTERS` VALUES (0,0,0,0,0,0,0,0,NULL,0,NULL,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,NULL,0,0,0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES;

--
-- Table `T_DBG_ENTRIES`
--

CREATE TABLE IF NOT EXISTS `T_DBG_ENTRIES` (
  `Id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `DbgMessage` varchar(60) DEFAULT NULL,
  `DbgContext` varchar(250) DEFAULT NULL,
  `DbgTs` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_HISTO`
--

CREATE TABLE IF NOT EXISTS `T_HISTO` (
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
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_PA_INST`
--

CREATE TABLE IF NOT EXISTS `T_PA_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `PA` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Data of table `T_PA_INST`
--

LOCK TABLES `T_PA_INST` WRITE;
INSERT INTO `T_PA_INST` VALUES (0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES;

--
-- Triggers of table `T_PA_INST`
--

DELIMITER |

DROP TRIGGER IF EXISTS AutoMinMaxPaUpdInst |

CREATE TRIGGER `AutoMinMaxPaUpdInst`

AFTER UPDATE ON `T_PA_INST`

FOR EACH ROW

BEGIN

   DECLARE OLD_PA_MIN FLOAT ;

   DECLARE OLD_PA_MAX FLOAT ;
   
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

END |

DELIMITER ;

--
-- Table `T_PA_MAX`
--

CREATE TABLE IF NOT EXISTS `T_PA_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PA` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_PA_MIN`
--

CREATE TABLE IF NOT EXISTS `T_PA_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PA` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_RH_INST`
--

CREATE TABLE IF NOT EXISTS `T_RH_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `RH` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Data of table `T_RH_INST`
--

LOCK TABLES `T_RH_INST` WRITE;
INSERT INTO `T_RH_INST` VALUES (0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES;

--
-- Triggers of table `T_RH_INST`
--

DELIMITER |

DROP TRIGGER IF EXISTS AutoMinMaxRhUpdInst |

CREATE TRIGGER `AutoMinMaxRhUpdInst`

AFTER UPDATE ON `T_RH_INST`

FOR EACH ROW

BEGIN

   DECLARE OLD_RH_MIN FLOAT ;

   DECLARE OLD_RH_MAX FLOAT ;
   
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

      UPDATE T_RH_MIN SET T_RH_MIN.RH = NEW.RH, T_RH_MIN.TS_TIME = @TS_TIME WHERE T_RH_MIN.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMinUpdNbTotal = T_COUNTERS.AutoMinMaxRhMinUpdNbTotal + 1 ;

   END IF ;
   
   IF NEW.RH > @OLD_RH_MAX

   THEN

      UPDATE T_RH_MAX SET T_RH_MAX.RH = NEW.RH, T_RH_MAX.TS_TIME = @TS_TIME WHERE T_RH_MAX.TS_DATE = @TS_DATE ;
      
      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMaxUpdNbTotal = T_COUNTERS.AutoMinMaxRhMaxUpdNbTotal + 1 ;

   END IF ;

   DELETE FROM T_RH_MIN WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMinDelNbTotal = T_COUNTERS.AutoMinMaxRhMinDelNbTotal + @DeletedNb ;
   
   DELETE FROM T_RH_MAX WHERE TS_DATE < DATE_SUB( NOW(), INTERVAL 120 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;
   
   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxRhMaxDelNbTotal = T_COUNTERS.AutoMinMaxRhMaxDelNbTotal + @DeletedNb ;

END |

DELIMITER ;

--
-- Table `T_RH_MAX`
--

CREATE TABLE IF NOT EXISTS `T_RH_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `RH` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_RH_MIN`
--

CREATE TABLE IF NOT EXISTS `T_RH_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `RH` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_TELEINFO_INST`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_INST` (
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

--
-- Data of table `T_TELEINFO_INST`
--

LOCK TABLES `T_TELEINFO_INST` WRITE;
INSERT INTO `T_TELEINFO_INST` VALUES (0,'\'\'',0,0,0,0,0,0,'\'\'','\'\'',0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES;

--
-- Triggers of table `T_TELEINFO_INST`
--

DELIMITER |

DROP TRIGGER IF EXISTS AutoMinMaxTeleinfoUpdInst |

CREATE TRIGGER `AutoMinMaxTeleinfoUpdInst`

AFTER UPDATE ON `T_TELEINFO_INST`

FOR EACH ROW

BEGIN

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

END |

DELIMITER ;

--
-- Table `T_TELEINFO_MAX`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_MAX` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PAPP` int(11) unsigned NOT NULL DEFAULT '0',
  `IINST` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_TELEINFO_MIN`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_MIN` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `PAPP` int(11) unsigned NOT NULL DEFAULT '0',
  `IINST` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_TEMP_INST`
--

CREATE TABLE IF NOT EXISTS `T_TEMP_INST` (
  `Id` int(11) unsigned NOT NULL DEFAULT '0',
  `TEMP` float NOT NULL DEFAULT '0',
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Data of table `T_TEMP_INST`
--

LOCK TABLES `T_TEMP_INST` WRITE;
INSERT INTO `T_TEMP_INST` VALUES (0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES;

--
-- Triggers of table `T_TEMP_INST`
--

DELIMITER |

DROP TRIGGER IF EXISTS AutoMinMaxTempUpdInst |

CREATE TRIGGER `AutoMinMaxTempUpdInst`

AFTER UPDATE ON `T_TEMP_INST`

FOR EACH ROW

BEGIN

   DECLARE OLD_TEMP_MIN FLOAT ;

   DECLARE OLD_TEMP_MAX FLOAT ;
   
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

END |

DELIMITER ;

--
-- Table `T_TEMP_MAX`
--

CREATE TABLE IF NOT EXISTS `T_TEMP_MAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `TEMP` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Table `T_TEMP_MIN`
--

CREATE TABLE IF NOT EXISTS `T_TEMP_MIN` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS_DATE` date NOT NULL,
  `TS_TIME` time NOT NULL,
  `TEMP` float DEFAULT NULL,
  PRIMARY KEY (`TS_DATE`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8;

--
-- Database Scheduled Events
--

DELIMITER |

DROP EVENT IF EXISTS `CleanOldHisto` |

CREATE EVENT `CleanOldHisto`

ON SCHEDULE

  EVERY 1 HOUR

  STARTS CURRENT_TIMESTAMP

  COMMENT 'Database scheduled event cleaning up histo past 120 DAYS.'

  DO

  BEGIN

    DECLARE DeletedNb INTEGER ;

    DECLARE HasNb INTEGER ;

    SET @HasNb = ( SELECT COUNT(*) FROM T_HISTO ) ;

    DELETE FROM T_HISTO

    WHERE T_HISTO.TS < DATE_SUB(NOW(), INTERVAL 120 DAY) ;

    SET @DeletedNb = ROW_COUNT() ;

    UPDATE T_COUNTERS SET T_COUNTERS.CleanHistoLastRunTs = NOW(), T_COUNTERS.CleanHistoRunNb = T_COUNTERS.CleanHistoRunNb + 1, T_COUNTERS.CleanHistoLastRunDelNb = @DeletedNb, T_COUNTERS.CleanHistoLastRunHasNb = @HasNb ;

END |

DELIMITER ;

---
--- Database Views
---

CREATE OR REPLACE VIEW V_PA_MIN_MAX AS
SELECT
 min.TS_DATE AS 'Date',
 min.TS_TIME AS 'Heure (min)',
 FORMAT(min.PA,2,'fr_FR') AS 'Pression Atmos. (min)',
 max.TS_TIME AS 'Heure (max)',
 FORMAT(max.PA,2,'fr_FR') AS 'Pression Atmos. (max)'
FROM T_PA_MIN AS min JOIN T_PA_MAX AS max ON min.TS_DATE = max.TS_DATE
ORDER BY min.TS_DATE DESC;

CREATE OR REPLACE VIEW V_RH_MIN_MAX AS
SELECT
 min.TS_DATE AS 'Date',
 min.TS_TIME AS 'Heure (min)',
 min.RH AS 'Humidité (min)',
 max.TS_TIME AS 'Heure (max)',
 max.RH AS 'Humidité (max)'
FROM T_RH_MIN AS min JOIN T_RH_MAX AS max ON min.TS_DATE = max.TS_DATE
ORDER BY min.TS_DATE DESC;

CREATE OR REPLACE VIEW V_TELEINFO_MIN_MAX AS
SELECT
 min.TS_DATE AS 'Date',
 min.TS_TIME AS 'Heure (min)',
 min.PAPP AS 'Puissance (min)',
 min.IINST AS 'Intensité (min)',
 max.TS_TIME AS 'Heure (max)',
 max.PAPP AS 'Puissance (max)',
 max.IINST AS 'Intensité (max)'
FROM T_TELEINFO_MIN AS min JOIN T_TELEINFO_MAX AS max ON min.TS_DATE = max.TS_DATE
ORDER BY min.TS_DATE DESC;

CREATE OR REPLACE VIEW V_TEMP_MIN_MAX AS
SELECT
 min.TS_DATE AS 'Date',
 min.TS_TIME AS 'Heure (min)',
 FORMAT(min.TEMP,1,'fr_FR') AS 'Température (min)',
 max.TS_TIME AS 'Heure (max)',
 FORMAT(max.TEMP,1,'fr_FR') AS 'Température (max)'
FROM T_TEMP_MIN AS min JOIN T_TEMP_MAX AS max ON min.TS_DATE = max.TS_DATE
ORDER BY min.TS_DATE DESC;



--
-- Database: `D_TELEINFO`
--

CREATE DATABASE IF NOT EXISTS `D_TELEINFO` DEFAULT CHARACTER SET utf8 ;

USE `D_TELEINFO`;

--
-- Table `T_COUNTERS`
--

CREATE TABLE IF NOT EXISTS `T_COUNTERS` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `RecvMsgNbTotal` bigint(20) DEFAULT NULL,
  `RecvMsgNbOk` bigint(20) DEFAULT NULL,
  `RecvMsgNbBad` bigint(20) DEFAULT NULL,
  `RecvMsgDataLineNbTotal` bigint(20) DEFAULT NULL,
  `RecvMsgDataLineNbOk` bigint(20) DEFAULT NULL,
  `RecvMsgDataLineNbBad` bigint(20) DEFAULT NULL,
  `RecvMsgDataLineNbUnsupp` bigint(20) DEFAULT NULL,
  `RecvMsgLastTs` datetime DEFAULT NULL,
  `CleanHistoRunNb` bigint(20) DEFAULT NULL,
  `CleanHistoLastRunTs` datetime DEFAULT NULL,
  `CleanHistoLastRunDelNb` bigint(20) DEFAULT NULL,
  `CleanHistoLastRunHasNb` bigint(20) DEFAULT NULL,
  `AutoMinMaxHistoRunNb` bigint(20) DEFAULT NULL,
  `AutoMinMaxHistoLastRunTs` datetime DEFAULT NULL,
  `AutoMinMaxHistoInsNbTotal` bigint(20) DEFAULT NULL,
  `AutoMinMaxHistoDelNbTotal` bigint(20) DEFAULT NULL,
  `AutoMinMaxHistoUpdMinNbTotal` bigint(20) DEFAULT NULL,
  `AutoMinMaxHistoUpdMaxNbTotal` bigint(20) DEFAULT NULL,
  `EnvTemperatureNbReadTotal` bigint(20) DEFAULT NULL,
  `EnvTemperatureNbReadOk` bigint(20) DEFAULT NULL,
  `EnvTemperatureNbReadFailed` bigint(20) DEFAULT NULL,
  `EnvTemperatureNbReadInvalid` bigint(20) DEFAULT NULL,
  `EnvTemperatureReadLastTs` datetime DEFAULT NULL,
  `EnvRelativeHumidityNbReadTotal` bigint(20) DEFAULT NULL,
  `EnvRelativeHumidityNbReadOk` bigint(20) DEFAULT NULL,
  `EnvRelativeHumidityNbReadFailed` bigint(20) DEFAULT NULL,
  `EnvRelativeHumidityNbReadInvalid` bigint(20) DEFAULT NULL,
  `EnvRelativeHumidityReadLastTs` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ;

LOCK TABLES `T_COUNTERS` WRITE ;
INSERT INTO `T_COUNTERS` VALUES (0,0,0,0,0,0,0,0,NULL,0,NULL,NULL,NULL,0,NULL,0,0,0,0,0,0,0,0,NULL,0,0,0,0,NULL) ON DUPLICATE KEY UPDATE Id = Id ;
UNLOCK TABLES ;

--
-- Table `T_DBG_ENTRIES`
--

CREATE TABLE IF NOT EXISTS `T_DBG_ENTRIES` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `DbgMessage` varchar(60) DEFAULT NULL,
  `DbgContext` varchar(60) DEFAULT NULL,
  `DbgTs` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ;

--
-- Table `T_TELEINFO_HISTO`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_HISTO` (
  `PTEC` varchar(2) DEFAULT NULL,
  `PAPP` int(11) DEFAULT NULL,
  `IINST` int(11) DEFAULT NULL,
  `HC` int(11) DEFAULT NULL,
  `HP` int(11) DEFAULT NULL,
  `ADCO` bigint(20) DEFAULT NULL,
  `ISOUSC` int(11) DEFAULT NULL,
  `OPTARIF` varchar(2) DEFAULT NULL,
  `HHPHC` varchar(2) DEFAULT NULL,
  `IMAX` int(11) DEFAULT NULL,
  `ETAT` int(11) DEFAULT NULL,
  `TEMPERATURE` float DEFAULT NULL,
  `RH` float DEFAULT NULL,
  `TS` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`TS`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ;

--
-- Table `T_TELEINFO_INST`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_INST` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `PTEC` varchar(2) DEFAULT NULL,
  `PAPP` int(11) DEFAULT NULL,
  `IINST` int(11) DEFAULT NULL,
  `HC` int(11) DEFAULT NULL,
  `HP` int(11) DEFAULT NULL,
  `ADCO` bigint(20) DEFAULT NULL,
  `ISOUSC` int(11) DEFAULT NULL,
  `OPTARIF` varchar(2) DEFAULT NULL,
  `HHPHC` varchar(2) DEFAULT NULL,
  `IMAX` int(11) DEFAULT NULL,
  `ETAT` int(11) DEFAULT NULL,
  `TEMPERATURE` float DEFAULT NULL,
  `RH` float DEFAULT NULL,
  `TS` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ;

LOCK TABLES `T_TELEINFO_INST` WRITE;
DELETE FROM `T_TELEINFO_INST` ;
INSERT INTO `T_TELEINFO_INST` VALUES (0,'..',0,0,0,0,0,0,'..','..',0,0,0,0,NULL);
UNLOCK TABLES;


--
-- Table `T_TELEINFO_MINMAX`
--

CREATE TABLE IF NOT EXISTS `T_TELEINFO_MINMAX` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `TS` date NOT NULL,
  `PAPP_MIN` int(11) DEFAULT NULL,
  `IINST_MIN` int(11) DEFAULT NULL,
  `TEMP_MIN` float DEFAULT NULL,
  `RH_MIN` float DEFAULT NULL,
  `TS_MIN` time DEFAULT NULL,
  `PAPP_MAX` int(11) DEFAULT NULL,
  `IINST_MAX` int(11) DEFAULT NULL,
  `TEMP_MAX` float DEFAULT NULL,
  `RH_MAX` float DEFAULT NULL,
  `TS_MAX` time DEFAULT NULL,
  `TS_HC` time DEFAULT NULL,
  `TS_HP` time DEFAULT NULL,
  `DELTA_HC` time DEFAULT NULL,
  `DELTA_HP` time DEFAULT NULL,
  PRIMARY KEY (`TS`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 ;


--
-- Database Events
--

DELIMITER |

DROP EVENT IF EXISTS `CleanOldHisto` |

CREATE EVENT `CleanOldHisto`

ON SCHEDULE

  EVERY 1 HOUR

  STARTS CURRENT_TIMESTAMP

  COMMENT 'cleaning up histo past 16 DAYS.'

  DO

  BEGIN
 
    DECLARE DeletedNb INTEGER ;
    
    DECLARE HasNb INTEGER ;

    SET @HasNb = ( SELECT COUNT(*) FROM T_TELEINFO_HISTO ) ;	
    
    DELETE FROM T_TELEINFO_HISTO

    WHERE T_TELEINFO_HISTO.TS < DATE_SUB(NOW(), INTERVAL 16 DAY) ;

    SET @DeletedNb = ROW_COUNT() ;    

    UPDATE T_COUNTERS SET T_COUNTERS.CleanHistoLastRunTs = NOW(), T_COUNTERS.CleanHistoRunNb = T_COUNTERS.CleanHistoRunNb + 1, T_COUNTERS.CleanHistoLastRunDelNb = @DeletedNb, T_COUNTERS.CleanHistoLastRunHasNb = @HasNb ;

  END |

DROP TRIGGER IF EXISTS AutoMinMaxInsertHisto |

CREATE TRIGGER AutoMinMaxInsertHisto AFTER INSERT

ON T_TELEINFO_HISTO FOR EACH ROW

BEGIN

   DECLARE OLD_PAPP_MIN INTEGER ;

   DECLARE OLD_PAPP_MAX INTEGER ;
  
   DECLARE TS_DATE DATE ;

   DECLARE TS_TIME TIME ;

   DECLARE DeletedNb INTEGER ;

   DECLARE InsertedNb INTEGER ;

   SET @TS_DATE = DATE( NEW.TS ) ;

   SET @TS_TIME = TIME( NEW.TS ) ;

   INSERT T_TELEINFO_MINMAX SET TS = @TS_DATE, PAPP_MIN = 99999, IINST_MIN = 99999, PAPP_MAX = 0, IINST_MAX = 0 ON DUPLICATE KEY UPDATE Id = Id ; 

   SET @InsertedNb = ROW_COUNT() ;

   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxHistoInsNbTotal = T_COUNTERS.AutoMinMaxHistoInsNbTotal + @InsertedNb ;
  
   SET @OLD_PAPP_MIN = ( SELECT PAPP_MIN FROM T_TELEINFO_MINMAX WHERE TS = @TS_DATE ) ;

   SET @OLD_PAPP_MAX = ( SELECT PAPP_MAX FROM T_TELEINFO_MINMAX WHERE TS = @TS_DATE ) ;
	
   IF NEW.PAPP > @OLD_PAPP_MAX

   THEN

      UPDATE T_TELEINFO_MINMAX SET T_TELEINFO_MINMAX.IINST_MAX = NEW.IINST, T_TELEINFO_MINMAX.PAPP_MAX = NEW.PAPP, T_TELEINFO_MINMAX.TS_MAX = @TS_TIME, T_TELEINFO_MINMAX.TEMP_MAX = NEW.TEMPERATURE, T_TELEINFO_MINMAX.RH_MAX = NEW.RH WHERE TS = @TS_DATE ;

      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxHistoUpdMaxNbTotal = T_COUNTERS.AutoMinMaxHistoUpdMaxNbTotal + 1 ;

   END IF ;

   IF NEW.PAPP < @OLD_PAPP_MIN

   THEN

      UPDATE T_TELEINFO_MINMAX SET T_TELEINFO_MINMAX.IINST_MIN = NEW.IINST, T_TELEINFO_MINMAX.PAPP_MIN = NEW.PAPP, T_TELEINFO_MINMAX.TS_MIN = @TS_TIME, T_TELEINFO_MINMAX.TEMP_MIN = NEW.TEMPERATURE, T_TELEINFO_MINMAX.RH_MIN = NEW.RH WHERE TS = @TS_DATE ;

      UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxHistoUpdMinNbTotal = T_COUNTERS.AutoMinMaxHistoUpdMinNbTotal + 1 ;

   END IF ;

   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxHistoRunNb = T_COUNTERS.AutoMinMaxHistoRunNb + 1, T_COUNTERS.AutoMinMaxHistoLastRunTs = NOW() ;

   DELETE FROM T_TELEINFO_MINMAX WHERE TS < DATE_SUB( NOW(), INTERVAL 32 DAY ) ;

   SET @DeletedNb = ROW_COUNT() ;

   UPDATE T_COUNTERS SET T_COUNTERS.AutoMinMaxHistoDelNbTotal = T_COUNTERS.AutoMinMaxHistoDelNbTotal + @DeletedNb ;

END |

DELIMITER ;
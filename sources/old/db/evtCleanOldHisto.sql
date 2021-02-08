SET GLOBAL event_scheduler = ON;

DELIMITER |

DROP EVENT IF EXISTS `CleanOldHisto` |

CREATE EVENT `CleanOldHisto`

ON SCHEDULE

  EVERY 1 HOUR

  STARTS CURRENT_TIMESTAMP

  COMMENT 'cleaning up histo past 8 DAYS.'

  DO

  BEGIN
 
    DECLARE DeletedNb INTEGER ;
    
    DECLARE HasNb INTEGER ;

    SET @HasNb = ( SELECT COUNT(*) FROM T_TELEINFO_HISTO ) ;	
    
    DELETE FROM T_TELEINFO_HISTO

    WHERE T_TELEINFO_HISTO.TS < DATE_SUB(NOW(), INTERVAL 8 DAY) ;

    SET @DeletedNb = ROW_COUNT() ;    

    UPDATE T_COUNTERS SET T_COUNTERS.CleanHistoLastRunTs = NOW(), T_COUNTERS.CleanHistoRunNb = T_COUNTERS.CleanHistoRunNb + 1, T_COUNTERS.CleanHistoLastRunDelNb = @DeletedNb, T_COUNTERS.CleanHistoLastRunHasNb = @HasNb ;

  END |

DELIMITER ;


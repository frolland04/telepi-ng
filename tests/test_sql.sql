select
MAX(PAPP) as 'Puiss. MAX',
MAX(IINST) as 'Int. MAX',
MAX(TEMPERATURE) as 'Temp. MAX',
MAX(RH) as 'RH. MAX',

ROUND(AVG(PAPP)) as 'Puiss. MOY',
ROUND(AVG(IINST)) as 'Int. MOY',
ROUND(AVG(TEMPERATURE)) as 'Temp. MOY',
ROUND(AVG(RH)) as 'RH. MOY',

MIN(PAPP) as 'Puiss. MIN',
MIN(IINST) as 'Int. MIN',
MIN(TEMPERATURE) as 'Temp. MIN',
MIN(RH) as 'RH. MIN',

DATE(TS) as 'TS' from T_TELEINFO_HISTO group by DATE(TS)\G ;

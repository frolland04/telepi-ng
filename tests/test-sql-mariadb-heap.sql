select round(((@@max_heap_table_size) / 1024 / 1024), 2), "MB";

SELECT round(((data_length + index_length) / 1024 / 1024), 2), "MB" FROM information_schema.TABLES
WHERE table_schema = 'D_TELEINFO' AND table_name = 'T_HISTO';

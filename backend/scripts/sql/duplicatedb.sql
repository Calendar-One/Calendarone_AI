
-- Step 1: Backup the source database
BACKUP DATABASE cal_ai
TO DISK = 'D:\Backup\cal_ai.bak'
WITH INIT;


-- Step 2: Restore into a new database with a different name and file locations
RESTORE DATABASE cal_ai_test
FROM DISK = 'D:\Backup\cal_ai.bak'
WITH MOVE 'cal_ai' TO 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\cal_ai_test.mdf',
     MOVE 'cal_ai_log'TO 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\cal_ai_test_log.ldf',
     REPLACE;

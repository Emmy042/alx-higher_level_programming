-- list the table description
SELECT 
  COLUMN_NAME AS 'Field',
  COLUMN_TYPE AS 'Type',
  IS_NULLABLE AS 'Null',
  COLUMN_KEY AS 'Key',
  COLUMN_DEFAULT AS 'Default',
  EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table'
  AND TABLE_SCHEMA = DATABASE();


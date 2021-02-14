select * from sqlcols1;

CREATE TABLE SQLCols2 ( 
  "Account" VARCHAR(20) NOT NULL , 
  "Entity" VARCHAR(20) NOT NULL , 
  "rowver1" TIMESTAMP NULL , 
  "smalldatetime1" SMALLDATETIME NULL , 
  "smallint" SMALLINT NULL , 
  "Amtsmallmoney" SMALLMONEY NULL , 
  "sqlvariant1" SQL_VARIANT NULL , 
  "sysname" SYSNAME NULL , 
  "Periodtime" TIME NULL , 
  "XML1" XML NULL );

CREATE TABLE SQLCols1 ( 
  "Account" VARCHAR(20) NOT NULL , 
  "Entity" VARCHAR(MAX) NOT NULL , 
  "Datetime" TIME NULL , 
  "Timestamp1" TIMESTAMP NULL , 
  "Tinyint1" TINYINT NULL , 
  "UniqueIdent1" UNIQUEIDENTIFIER NULL , 
  "varbin1" VARBINARY(1) NULL , 
  "bigint1" BIGINT NULL , 
  "binary1" BINARY(1) NULL , 
  "binVary1" VARBINARY(1) NULL , 
  "Bitflag" BIT NULL , 
  "char1" CHAR(1) NULL , 
  "charvarying" VARCHAR(1) NULL , 
  "fullcharacter" CHAR(1) NULL , 
  "fcharactervarying" VARCHAR(1) NULL , 
  "Date1" DATE NULL , 
  "Datetime1" DATETIME NULL , 
  "datetime2" DATETIME2 NULL , 
  "datetimeoffset1" DATETIMEOFFSET NULL , 
  "Dec1" DECIMAL(18, 0) NULL , 
  "Float1" FLOAT(53) NULL , 
  "decimal1" DECIMAL(18, 0) NULL , 
  "Geography1" GEOGRAPHY NULL , 
  "Geometry1" GEOMETRY NULL , 
  "HierarchID1" HIERARCHYID NULL , 
  "Image1" IMAGE NULL , 
  "Int2" INT NULL , 
  "Integer1" INT NULL , 
  "AmountMoney" MONEY NULL , 
  "NatlChar" NCHAR(1) NULL , 
  "NatlCharVary" NVARCHAR(1) NULL , 
  "NatlCharacter1" NCHAR(1) NULL , 
  "NatlCharacterVary1" NVARCHAR(1) NULL , 
  "NatlText" NTEXT NULL , 
  "Nchar2" NCHAR(1) NULL , 
  "Ntext1" NTEXT NULL , 
  "Numeric2" NUMERIC(18, 0) NULL , 
  "NVarchar1" NVARCHAR(1) NULL , 
  "Real1" REAL NULL , 
  "smalldatetime1" SMALLDATETIME NULL );


CREATE VIEW SQLView1 AS SELECT one.account, one.amountmoney, one.binary1, one.date1, two.entity,
two.smalldatetime1, two.smallint
    
FROM 
    sqlcols1 one, sqlcols2 two
    
    where one.account = two.account and one.entity = two.entity;
    

--drop table SQLcols1;

insert into testdb.dbo.sqlcols2 (Account, ENtity, Dec1)  values (0015, 01, 777);
insert into testdb.dbo.sqlcols1 (Account, ENtity, Dec1)  values (0015, 01, 707);


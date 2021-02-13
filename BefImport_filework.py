import java.sql as sql

if str(fdmContext["LOCNAME"]) == 'ANSTAT4_LOC99' and str(fdmContext["RULENAME"]) == 'ANSTAT4_LOC99_DL2':
  fdmAPI.updateImportFormat('ANTest',fdmContext["LOADID"]);

if str(fdmContext["LOCNAME"]) == 'ANSTAT4_LOC98':
  batchName = "Batch_" + str(fdmContext["LOCNAME"])
  insertStmt = """
  INSERT INTO AIF_OPEN_INTERFACE (
     BATCH_NAME
    ,COL01
    ,COL02
    ,AMOUNT
    ,DESC1
    ,YEAR
    ,PERIOD
    ,PERIOD_NUM
  ) VALUES (
     ?
    ,?
    ,?
    ,?
    ,?
    ,2005
    ,'April' 
    ,4
  ) 
  """
  sourceConn = sql.DriverManager.getConnection("jdbc:oracle:thin:@slc02oxk:1521:fdm11gR2", "KFtest", "password");
  # Limiting number of rows to 5 during the test runs.
  selectStmt = "SELECT * FROM orders"
  stmt = sourceConn.prepareStatement(selectStmt)
  stmtRS = stmt.executeQuery()
  while(stmtRS.next()):
    params = [ batchName, stmtRS.getBigDecimal("Customer_Id"), stmtRS.getString("Ship_Country"), 
      stmtRS.getBigDecimal("Freight"), stmtRS.getString("Ship_Name") ]
    fdmAPI.executeDML(insertStmt, params, False)
  fdmAPI.commitTransaction()
  
  stmtRS.close()
  stmt.close()
  sourceConn.close()

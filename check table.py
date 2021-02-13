selectStmt = "SELECT COUNT(*) from TDATAMAP_T  WHERE  PARTITIONKEY = 289 ; "
stmt = conn.prepareStatement(selectStmt)
stmt = stmt.executeQuery()

x=0
while(stmt.next() and x <5):
  params = [ stmt.getString("COL01"), stmt.getBigDecimal("AMOUNT"), stmt.getString("BATCH_NAME"), 
           stmt.getBigDecimal("PERIOD_NUM"), stmt.getString("DESC1") ]
  fdmAPI.log( params[0] + " "+ params[2] +" "+ str(params[1])  )
  #fdmAPI.executeDML(insertStmt, params, False)
  x += 1
#fdmAPI.log( fdmAPI.executeDML(insertStmt, params, False))

fdmAPI.commitTransaction()
#stmtRS.close()
stmt.close()
conn.close()

query = "SELECT COUNT(*) from TDATAMAP_T  WHERE  PARTITIONKEY = 289 ; "
params =  fdmContext["LOADID"] 
pp = [ params ]
print fdmAPI.executeDML(query, pp, False)

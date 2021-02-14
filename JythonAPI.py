'''
Created on Dec 18, 2013

@author: jstolz
'''

if __name__ == '__main__':
    pass
  
import sys
from java.io import FileOutputStream
import java.math.BigDecimal as BigDecimal
import java.sql.Date as Date
import os.path
import java.sql as sql
import com.hyperion.aif.scripting.API as API

 
fdmAPI = API()
conn = None
#if (pEnvName == "slc03zpg_epm"):
#conn = sql.DriverManager.getConnection("jdbc:oracle:thin:@slc02oxk:1521:fdm11gR2", "PS3SLC03GFCERPI", "xx")
#conn = sql.DriverManager.getConnection("jdbc:oracle:thin:@slc03hhe:1521:orcl", "slc03zpg_epm", "xx");
#conn = sql.DriverManager.getConnection("jdbc:oracle:thin:@slc04ysn.us.oracle.com:1521/PDBORCL.US.ORACLE.COM", "joe", "xx")

#conn.setAutoCommit(False)
#fdmAPI.initializeDevMode(conn)
p_process_id = BigDecimal(610)
fdmContext = fdmAPI.initContext(p_process_id)

batchName = "Batch_" + str(fdmContext["LOCNAME"])
fdmAPI.log( fdmContext["LOCNAME"])

#getPOVLocation
location_id = fdmAPI.getPOVLocation(p_process_id)
fdmAPI.log( "Location id " + str(location_id)  )

#getPOVCategory
cat_id = fdmAPI.getPOVCategory(p_process_id)
fdmAPI.log( " Category" + str(cat_id))

#Date getPOVStartPeriod(BigDecimal pLoadId)
startPer = fdmAPI.getPOVStartPeriod(p_process_id)
fdmAPI.log( "POV start period" + str(startPer))

#Date getPOVEndPeriod(BigDecimal pLoadId)
endPer = fdmAPI.getPOVEndPeriod(p_process_id)
fdmAPI.log( "POV end Period" + str(endPer))

#getPOVDataValue(BigDecimal pPartitionKey) 
p_partitionkey = BigDecimal(51)
dataValue = fdmAPI.getPOVDataValue(p_partitionkey)
fdmAPI.log( "data value is " + str(dataValue))

#getDirTopLevel(BigDecimal pApplicationId) 
TopDir = fdmAPI.getDirTopLevel(p_partitionkey)
fdmAPI.log( "Top Directory is " + str(TopDir))

#String getDirInbox(BigDecimal pApplicationId) 
DirInbox = fdmAPI.getDirInbox(p_partitionkey)
fdmAPI.log( "Directory inbox" + str(DirInbox))

#String getDirOutbox(BigDecimal pApplicationId)
DirOutbox = fdmAPI.getDirOutbox(p_partitionkey)
fdmAPI.log( "Directory outbox" + str(DirOutbox))

#String getDirScripts(BigDecimal pApplicationId)
p_App_id = BigDecimal (28)
ScpDir = fdmAPI.getDirScripts (p_App_id)
fdmAPI.log( "Script Directory" + str(ScpDir))

#String getUserIDFromToken(String pSSOToken)
#Q: Should we make this private

#String getProfileOptionValue(String profileOptionName,BigDecimal applicationId,String userIdentity)
#profileOpt = fdmAPI.getProfileOptionValue (application,p_App_id,admin)
fdmAPI.log( fdmAPI.getProfileOptionValue("ENABLE_EVENT_SCRIPT_EXECUTION", BigDecimal(28), "admin"))

#Map getProcessStates(BigDecimal pLoadId)
p_process_id = BigDecimal(610)
processStates = fdmAPI.getProcessStates (p_process_id)
fdmAPI.log( "process states are" + str(processStates))

#ResultSet getCategoryList()
catResultSet = fdmAPI.getCategoryList()
#to get the columns in the resultset
resultSetMetaData = catResultSet.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Category list")
while(catResultSet.next()):
  fdmAPI.log( catResultSet.getString("CATKEY") + catResultSet.getString("CATNAME"));
catResultSet.close
  
#ResultSet getPeriodList()
PeriodResultSet = fdmAPI.getPeriodList()
#to get the columns in the resultset
resultSetMetaData = PeriodResultSet.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Period list")
while(PeriodResultSet.next()):
  fdmAPI.log( PeriodResultSet.getString("PERIODKEY") + PeriodResultSet.getString("PERIODDESC"))
PeriodResultSet.close


  
#ResultSet getValEntGroupList(BigDecimal pApplicationId)
p_App_id1 = BigDecimal(40) 
# 40 is app id for app BudPlan
ChkEntGrpRS = fdmAPI.getCheckEntityGroupList(p_App_id1)
resultSetMetaData = ChkEntGrpRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Check entity group list for given application")
while(ChkEntGrpRS.next()):
  temp =  ChkEntGrpRS.getString("VALENTGROUPDESC")
  if(temp== None):
    temp="-blank-"
  fdmAPI.log( ChkEntGrpRS.getString("VALENTGROUPKEY") + temp  );
ChkEntGrpRS.close

#ResultSet getValEntForGroup(String  pValGroupKey)
#from TBHVVALENTGROUP table or above run identified Plan2Calc 
#error at this call below java.sql.SQLSyntaxErrorException: java.sql.SQLSyntaxErrorException: ORA-00923: FROM keyword not found where expected
EntListChkGrpRS = fdmAPI.getCheckEntityForGroup("Plan2Calc")
resultSetMetaData = EntListChkGrpRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "check rule details for a check entity group are ")
while(EntListChkGrpRS.next()):
  fdmAPI.log( EntListChkGrpRS.getString("VALENTLISTORG") + EntListChkGrpRS.getString("VALENTLISTNAME")+ EntListChkGrpRS.getString("VALENTLISTCONSOL")+ EntListChkGrpRS.getString("VALENTLISTSEQ")+EntListChkGrpRS.getString("VALENTLISTSTARTPERIOD")+ EntListChkGrpRS.getString("VALENTLISTENTTYPE")+EntListChkGrpRS.getString("VALENTLISTENTONREPORT")) ;
EntListChkGrpRS.close


#ResultSet getValGroup(BigDecimal pApplicationId) 
#This parameter should be partition key from table TDATACHECK
#error at this call below java.sql.SQLSyntaxErrorException: java.sql.SQLSyntaxErrorException: ORA-00923: FROM keyword not found where expected
p_App_id2 = BigDecimal(33) 
#32 is partition key for app KFPC2, app id for this is 33
ChkRuleGrpRS = fdmAPI.getCheckGroup(p_App_id2)
resultSetMetaData = ChkRuleGrpRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Check rule group list for given application")
while(ChkRuleGrpRS.next()):
  temp=ChkRuleGrpRS.getString("VALGROUPDESC")
  if(temp== None):
    temp="blank"
  fdmAPI.log( ChkRuleGrpRS.getString("VALGROUPKEY") +  temp );
ChkRuleGrpRS.close

#ResultSet getValGroupList(String  pValItemKey) 
#from TBHVVALENTGROUP table or above run identified Plan2Calc 
#error at this call below java.sql.SQLSyntaxErrorException: java.sql.SQLSyntaxErrorException: ORA-00923: FROM keyword not found where expected
#EntListChkGrpRS = fdmAPI.getCheckGroupList("Plan2Calc")
EntListChkGrpRS = fdmAPI.getCheckGroupList("testcrg")
resultSetMetaData = EntListChkGrpRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "check rule details for a check rule are ")
while(EntListChkGrpRS.next()):
  fdmAPI.log( EntListChkGrpRS.getString("VALRULETARGETACCTKEY") + EntListChkGrpRS.getString("VALRULETARGETACCTDESC") + EntListChkGrpRS.getString("VALRULEDESC") +EntListChkGrpRS.getString("VALRULETEXT") + EntListChkGrpRS.getString("VALRULESEQ")+EntListChkGrpRS.getString("VALRULEENTTYPE")+EntListChkGrpRS.getString("VALRULECATKEY")+EntListChkGrpRS.getString("VALRULELOGIC"));
EntListChkGrpRS.close

#void updateImportFormat(String pImpgroupKey,BigDecimal pLoadId) - applicable for file import formats
#fdmAPI.updateImportFormat(bigDecimal, string)
#not sure how this function is useful and what is updating
if str(fdmContext["LOCNAME"]) == 'ANHC1RC3_LOC1' and str(fdmContext["RULENAME"]) == 'ANHC1RC3_LOC1_DL2':
  fdmAPI.updateImportFormat('ANTest',fdmContext["LOADID"]);
  fdmAPI.log( "done update import format"  )
#int executeDML(String query,Object[] parameters)
#Update in TSA document, it is taking 3 parameters
 
#ResultSet getImportFormatDetails(String pImpGroupKey) - from table TBHVIMPGROUP
ImpFormatDetRS = fdmAPI.getImportFormatDetails("PC2EBS12")
resultSetMetaData = ImpFormatDetRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Import format details ")
while(ImpFormatDetRS.next()):
  fdmAPI.log( ImpFormatDetRS.getString("IMPGROUPKEY")+ ImpFormatDetRS.getString("IMPGROUPDESC")+ ImpFormatDetRS.getString("IMPGROUPFILETYPE"));
ImpFormatDetRS.close

#ResultSet getImportFormatMapDetails(String pImpGroupKey) - applicable for file based import formats only
ImpFormatMapDetRS = fdmAPI.getImportFormatMapDetails("filebased")
resultSetMetaData = ImpFormatMapDetRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Import format mapping details ")
while(ImpFormatMapDetRS.next()):
  fdmAPI.log( ImpFormatMapDetRS.getString("IMPFLDFIELDNAME")+ ImpFormatMapDetRS.getString("IMPFLDFIXEDTEXT")+ str(ImpFormatMapDetRS.getInt("IMPFLDSTARTPOS"))+ str(ImpFormatMapDetRS.getInt("IMPFLDLENGTH"))+ImpFormatMapDetRS.getString("IMPFLDSOURCECOLNAME"));
ImpFormatMapDetRS.close

#String getCategoryMap(BigDecimal pCatKey,String pApplicationName)
#there seems to be a mismatch in the parameter list when using Catkey, "Comm7D" it gives invalid column index
CatKey = BigDecimal(7)
CatMap = fdmAPI.getCategoryMap(CatKey, "COMM7D")
fdmAPI.log( "Category Mapping is " + str(CatMap))

#Map getPeriodDetail(Date pPeriodKey,String pApplicationName) -- if using parameters as App, Periodkey then get invalid column index
d = Date.valueOf("2003-03-01")
fdmAPI.log( str(d))
PeriodDet = fdmAPI.getPeriodDetail(d,"COMM7D")
fdmAPI.log( "Period details are " + str(PeriodDet))

#ResultSet getLocationDetails(BigDecimal pPartitionKey)
p_partitionkey = BigDecimal(32)
LocDetailsRS = fdmAPI.getLocationDetails(p_partitionkey)
resultSetMetaData = LocDetailsRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Location details ")
while(LocDetailsRS.next()):
  fdmAPI.log( LocDetailsRS.getString("PARTNAME")+ LocDetailsRS.getString("PARTIMPGROUP")+ LocDetailsRS.getString("PARTTARGETAPPLICATIONID")+ LocDetailsRS.getString("PARTVALGROUP")+LocDetailsRS.getString("PARTDATAVALUE"));
LocDetailsRS.close

#ResultSet getRuleDetails(BigDecimal pRuleId) --which table is this going against?
p_ruleId = BigDecimal(70)
RuleDetailsRS = fdmAPI.getRuleDetails(p_ruleId)
resultSetMetaData = RuleDetailsRS.getMetaData()
for i in range(1, resultSetMetaData.getColumnCount()+1):
  fdmAPI.log( resultSetMetaData.getColumnName(i) )
fdmAPI.log( "Rule details ")
while(RuleDetailsRS.next()):
  fdmAPI.log( "in loop")
  fdmAPI.log( RuleDetailsRS.getString("RULE_NAME")+ RuleDetailsRS.getString("APPLICATION_ID")+ str(RuleDetailsRS.getInt("SOURCE_SYSTEM_ID")))
RuleDetailsRS.close

#script we used in BefImport to get data from a database table
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
#conn.close 
#    change this to access an FDMEE table instead
#sourceConn = sql.DriverManager.getConnection("jdbc:oracle:thin:@slc02oxk:1521:fdm11gR2", "KFtest", "password");
# Limiting number of rows to 5 during the test runs.
selectStmt = "SELECT * FROM AIF_OPEN_INTERFACE"
stmt = conn.prepareStatement(selectStmt)
stmtRS = stmt.executeQuery()
x=0
while(stmtRS.next() and x <5):
  params = [ batchName, stmtRS.getBigDecimal("AMOUNT"), stmtRS.getString("BATCH_NAME"), 
           stmtRS.getBigDecimal("PERIOD_NUM"), stmtRS.getString("DESC1") ]
  fdmAPI.log( params )
  fdmAPI.executeDML(insertStmt, params, False)
  x += 1
#fdmAPI.log( fdmAPI.executeDML(insertStmt, params, False))

fdmAPI.commitTransaction()
stmtRS.close()
stmt.close()
conn.close()
fdmAPI.log( "ending program")


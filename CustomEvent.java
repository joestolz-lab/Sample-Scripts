package oracle.epm.aif.agent.agentinterface;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Sample custom function implementation sample code. In order to use this class it must be named with the following name including
 * the package name "oracle.epm.aif.agent.agentinterface.CustomInterfaceImplementation" and must implement the "EpmAgentInterface" 
 * java interface.
 *  
 * Customers and Partners can also choose to exclude this class from agent-interface.jar or any class which implements EpmAgentInterface.
 * 
 * This class can also be implemented outside of the agent-interface.jar with a different jar and class Name.
 * In order to do this please specify the jar name and the class name implementing the EpmAgentInterface interface
 * using the below 2 startup parameters in the agent startup parameter file (agentparams.ini) as:
 * CUSTOM_CLASS_PATH=<Full path and name of the jar eg: C:\AgentDeployment\agenthome\myJarFolder\custom.jar>
 * CUSTOM_INTERFACE_CLASS_NAME=<Fully qualified class name of the class in custom.jar which implements EpmAgentInterface
 * eg: com.mycompany.agent.implementation.MyImplementation>
 */
public class CustomEvent implements EpmAgentInterface{

	/**
	 * @see oracle.epm.aif.agent.agentinterface.EpmAgent#executeCustomFunction(java.lang.String, oracle.epm.aif.agent.agentinterface.AgentContext, java.util.Map)
	 * 
	 * Custom implementation method which is called four times during the execution of an extract operation
	 * as described below:
	 * 1. Before the extract query begins execution.
	 * 2. After the extract query has finished and the data file (.dat file) has been generated.
	 * 3. Before the data file is uploaded to cloud
	 * 4. After the data file has been uploaded to cloud
	 * 
	 * @param  String event: defines the event type for each of the four events described above. The can have the values BefExtract, AftExtract, BefUpload
	 * 		   and AftUpload. Use the Enum values defined in EpmAgentInterface.Event to get the full list of events.
	 * 
	 * @param  AgentAPI agentAPI: API object which provides methods which can be called from executeCustomFunction method.
	 * 
	 * @param  Map<String, Object> agentContext: Map containing the parameters which are available to this method during the method call. 
	 * 		   These parameters cannot be removed or modified from the agentContext map. The value, number and type of these parameters can be 
	 * 			different during the different events for which this method is called. 
	 * 
	 */
	@Override
	public void executeCustomFunction(String event, AgentAPI agentAPI, Map<String, Object> agentContext) {
		
		 
		/**
		 * The agentContext map can also be retrieved from the agentContext object directly as shown below.
		 * This is the same as the agentContext Map passed to this method. 
		 */
		Map<String, Object> agentContextDuplicate = agentAPI.getAgentContext();
		
		
		 /**
		  * Print the contents of the agentContext map which is an unmodifiable map. 
		  * Sample print of the below info log:
		  * Name = JOBTYPE, Value = EXTRACT
		  * Name = EPM_AGENT_HOME, Value = C:\AgentDeployment\agenthome
		  * Name = JOBID, Value = 344
		  * Name = EPM_APP_DATA_HOME, Value = C:\AgentDeployment\apphome
		  * Name = DELIMITER, Value = ,
		  * Name = DATAFILENAME, Value = C:\AgentDeployment\apphome\data\344.dat
		  */
		 for (Map.Entry<String,Object> entry : agentContext.entrySet()){
			 agentAPI.logInfo("Name = " + entry.getKey() +", Value = " + entry.getValue()); 
		 }
		
		/**
		 * Sample method calls which can be used to execute before and after the extract and data file upload operations.
		 */
		if(event.equals("BefExtract")){
			executeBeforeExtract(event, agentAPI, agentContext);
		}else if(event.equals("AftExtract")){
			executeAfterExtract(event, agentAPI, agentContext);
		}else if(event.equals("BefUpload")){
			executeBeforeFileUpload(event, agentAPI, agentContext);
		}else if(event.equals("AftUpload")){
			executeAfterFileUpload(event, agentAPI, agentContext);
		}
		
		 
		 /**
		  * Log an info message to the agent process log. This entry will be logged only to the process log in EPM_APP_DATA_HOME\logs
		  * folder and not to epmagent.log. The log entry will be created at INFO log level.
		  *
		 agentAPI.logInfo("SAMPLE: INFO log message from custom interface.");
		 
		 
		 /**
		  * Log an severe message to the agent process log. This entry will be logged into the process log in EPM_APP_DATA_HOME\logs
		  * folder and also into epmagent.log. The log entry will be created at SEVER log level.
		  *		 agentAPI.logError("SAMPLE: SEVER log message from custom interface");
		 */

		}
	
		/**
		 * Code to execute before the extract query begins execution.
		 * @param event
		 * @param agentAPI
		 * @param agentContext
		 */
		private void executeBeforeExtract(String event, AgentAPI agentAPI, Map<String, Object> agentContext){
			 /**
			  * Method to skip the extract data execution. The extract execution can be skipped only during the
			  * befExtract event. This will skip the execution of the extract query and no data file will be uploaded
			  * to cloud. The cloud process will be marked as failed in the Extract data step. 
			  *
			 agentAPI.skipAction(true); 
			 
			 /**
			  * getQuery() Method to fetch the extract query which is used to execute the extract. This is the query which is
			  * passed from cloud to the agent during the extract execution call.
			  */
			 String query = agentAPI.getQuery();
			 
			 /**
			  * updateQuery() Method to update the extract query. This is applicable only when the event parameter is BefExtract.
			  */
			 agentAPI.updateQuery(new String("SELECT * FROM TDATASEG"));
			 agentAPI.logError("BEFORE Extract message");

			 
			 /**
			  * getBindVariables() Method to fetch the bind variables for the extract query. Each bind variable is stored in a Map which
			  * uses the keys NAME and VALUE to define the bind variable.
			  */
			 Map<String,Object> bindVariables = agentAPI.getBindVariables();
			  for (Map.Entry bindVar : bindVariables.entrySet()) {
				  String bindParaName = (String)bindVar.getKey();
				  Object bindParamVal = (Object)bindVar.getValue();
				  agentAPI.logInfo("Bind Variable:"+bindParaName+"  Value:"+bindParamVal);
			  }
			 
			 /**
			  * setBindVariables() Method to update the extract query's bind variables. This is applicable only when the event parameter is BefExtract
			  * The bind variables must be passed as a Map entry for each variable with variable NAME as key and VALUE. Below is a sample code for the same.
			 */
			 Map<String,Object> newBindVariables = new HashMap<String,Object>();
			 newBindVariables.put("RULE_NAME", new String ("SAMPLE_RULE_NAME"));
			 newBindVariables.put("DATAKEY", new Integer(40));
			 newBindVariables.put("ACCOUNT", new String("Gross Margin %"));
			 newBindVariables.put("CATKEY", new Integer(2));
			 agentAPI.setBindVariables(newBindVariables);
		}
		
		
		/**
		 * Code to execute after the extract query has finished and the data file (.dat file) has been generated.
		 * @param event
		 * @param agentAPI
		 * @param agentContext
		 */
		private void executeAfterExtract(String event, AgentAPI agentAPI, Map<String, Object> agentContext){
		
		}
		
		agentAPI.logError("AFTER Extract message");
		/**
		 * Code to execute before the data file is uploaded to cloud
		 * @param event
		 * @param agentAPI
		 * @param agentContext
		 */
		private void executeBeforeFileUpload(String event, AgentAPI agentAPI, Map<String, Object> agentContext){
			 /**
			  * Method to skip data file upload execution. This can be executed only during the BefUpload
			  * event. When set to true, the generated data file will not be uploaded to cloud and the Import data step
			  * will be marked as failed in cloud.
			  *
			 agentAPI.skipAction(true); 
			 */
			agentAPI.logError("BEFORE File Upload message");
		}
		
		
		/**
		 * Code to execute after the data file has been uploaded to cloud
		 * @param event
		 * @param agentAPI
		 * @param agentContext
		 */
		private void executeAfterFileUpload(String event, AgentAPI agentAPI, Map<String, Object> agentContext){
			agentAPI.logError("AFTER File Upload  message");
		
		}
}


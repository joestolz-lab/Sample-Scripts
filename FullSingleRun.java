package FDMEE1;

import static io.restassured.RestAssured.given;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import io.restassured.RestAssured;

@Test
public class FullSingleRun {
	String Name="epm_default_cloud_admin";
	String Passwd="xx";
	String rule1 = "DL_ASO_Curr2";
		
	@BeforeClass
	public void setup() {
		RestAssured.baseURI = "http://slc12cvo.us.oracle.com:9000";
		RestAssured.basePath ="/aif/rest/V1";		
	}
	public void verifyrule() {
		given()
			.auth().preemptive().basic(Name, Passwd)
			.header("Accept", "application/json")
			.header("Content-Type", "application/json")
			.pathParam("ruleName","DL_ASO_Curr2")
		.when()
			.get("/rules/{ruleName}")
		.then()
			.statusCode(200);	
		}
	public void runrule() {
		given()
			.auth().preemptive().basic(Name, Passwd)
			.header("Accept", "application/json")
			.header("Content-Type", "application/json")
			.pathParam("ruleName","DL_ASO_Curr2")
		.when()
			.get("/rules/{ruleName}")
		.then()
			.statusCode(200);	
		}
}

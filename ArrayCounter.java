import java.util.Arrays;
import java.util.*;

public class ArrayCounter {

	public static void main(String[] args) {
		// 
		String[] arrin = {"a","a","b","b","b","c"};
		ArrayList<String> arrout = new ArrayList<String>();
		
		int i=0;
		int j=0;
		String v1[]= {"x"};
		int c1 = 0;
		
		for(i=0; i< arrin.length ; )
		{
			v1[0] = arrin[i];
			arrout.add(v1[0]);
			while ( i< arrin.length && v1[0] == arrin[i] )
			{
				i++;
				c1++;
			}
			arrout.add(Integer.toString(c1));
			c1=0;
		}
		System.out.println(arrout);
  }
}
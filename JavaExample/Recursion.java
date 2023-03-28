public class Main{
    public static void main(String[] args) {
		System.out.println("Hello, World");
		Main m=new Main();
		m.RecursionFun(60);
	}
	public double RecursionFun(double times){
	    double value=times;
	    if(times<2){
	        return value;
	    }
	    else{
	        value=value*RecursionFun(times-1);
	       	System.out.println(value);
	       	return value;
	    }
	}
}

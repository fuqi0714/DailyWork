import java.sql.Date;

public class ThreadExampleTwo implements Runnable{
    public void run(){
        if(Thread.currentThread().getName()=="1"){
            ThreadOne(Thread.currentThread().getName());
        }
        else if(Thread.currentThread().getName()=="2"){
            ThreadTwo(Thread.currentThread().getName());
        }
        else{
            System.out.println(ThreadThree(Thread.currentThread().getName()));
        }
    }
	public static void main(String[] args) {
		System.out.println("Initialize");
		ThreadExampleTwo eo=new ThreadExampleTwo();
		Thread t1=new Thread(eo,"1");
		Thread t2=new Thread(eo,"2");
		Thread t3=new Thread(eo,"67");
		t1.start();
		try{
		    t1.join();
		    
		}
		catch(Exception e)
        {
            System.out.println(e);
        }
		t2.start();
	
		t3.start();
	}
    void ThreadOne(String s){
        for(int i=0;i<7;i++){
            System.out.println("Test thread name is "+Thread.currentThread().getName()+" run and i is "+i);
            try{
                Thread.sleep(100);
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }
    }
    void ThreadTwo(String s){
        System.out.println("Test thread name is "+Thread.currentThread().getName()+" and run once time ");
    }
    String ThreadThree(String s){
        System.out.println("Test thread name is "+Thread.currentThread().getName()+" and return data ");
        Date date = new Date(System.currentTimeMillis());
        
        return date.toString();
    }
}
public class ThreadExampleOne implements Runnable{
    public void run(){
        if(Thread.currentThread().getName()=="1"){
            for(int i=0;i<7;i++){
                System.out.println("Test thread 1 run and i is "+i);
                try{
                    Thread.sleep(100);
                }
                catch(Exception e)
                {
                    System.out.println(e);
                }
            }
        }
        else if(Thread.currentThread().getName()=="2"){
            for(int i=9;i>0;i--){
                System.out.println("Test thread 2 run and i is "+i);
                try{
                    Thread.sleep(100);
                }
                catch(Exception e)
                {
                    System.out.println(e);
                }
            }
        }
        else{
            for(int i=0;i<7;i++){
                System.out.println("Test thread other run");
                try{
                    Thread.sleep(100);
                }
                catch(Exception e)
                {
                    System.out.println(e);
                }
            }
        }
    }
	public static void main(String[] args) {
		System.out.println("Initialize");
		ThreadExampleOne eo=new ThreadExampleOne();
		new Thread(eo,"1").start();
		new Thread(eo,"2").start();
		new Thread(eo,"67").start();
	}
}
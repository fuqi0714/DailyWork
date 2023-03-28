public class ThreadExampleZero extends Thread{
    public void run(){
        for(int i=0;i<7;i++){
            System.out.println("Test thread-1 run name :"+Thread.currentThread().getName());
            try{
                Thread.sleep(100);
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }
    }
	public static void main(String[] args) {
		System.out.println("Initialize");
		ThreadExampleZero eo=new ThreadExampleZero();
		new Thread(eo,"1").start();
		new Thread(eo,"2").start();
	}
}
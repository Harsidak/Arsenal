public class Expose{
    private String secret = "";
    
    public Expose(String text) {
        this.secret = text.toUpperCase();
    }

    public static void main(String[] args) {
        Expose message = new Expose("top secret text");
        System.out.println(message.secret);
    }
}
import java.io.*;
import java.net.*;

class Client{
    public static void main(String[] args){

        try{
            Socket socket = new Socket("localhost",9999);
            String message = "Hello World";
            DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
            dataOutputStream.writeUTF(message);
            System.out.println("Sending Message To Server: "+message);
            DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
            String message1 = (String) dataInputStream.readUTF();
            System.out.println("Received Message From Server: "+message1);
            socket.close();
        }  catch(Exception ex){
            System.out.println(ex);
        }

    }
}
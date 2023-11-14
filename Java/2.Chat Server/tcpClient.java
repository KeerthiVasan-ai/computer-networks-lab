import java.io.*;
import java.net.*;
import java.util.*;

class TcpClient{
    public static void main(String[] args){
        try{
            System.out.println("Type bye to Teriminate!");
            Socket socket = new Socket("localhost",9999);
            Scanner scanner = new Scanner(System.in);
            String message = scanner.nextLine();
            do{
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeUTF(message);

                DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
                String serverMessage = (String) dataInputStream.readUTF();
                System.out.println(serverMessage);

                
                message = scanner.nextLine();
            } while (!message.trim().equals("bye"));
            System.out.println("Terminated");

        } catch(Exception ex){
            System.out.println(ex);
        }
    }
}
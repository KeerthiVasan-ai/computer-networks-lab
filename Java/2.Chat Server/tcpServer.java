import java.io.*;
import java.net.*;
import java.util.*;

class TcpServer{
    public static void main(String[] args){
        try{
            ServerSocket s = new ServerSocket(9999);
            System.out.println("Waiting for the Connection");
            Socket socket = s.accept();

            while (true) {

                /* Receive The Message from Client */

                DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
                String message = (String) dataInputStream.readUTF();
                System.out.println(message);
                Scanner scanner = new Scanner(System.in);

                /* New Message from the Server */

                String serverMessage = scanner.nextLine();

                /* Send the Server's Message to the Client */

                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeUTF(serverMessage);
            }

        } catch(EOFException ex){
            System.out.println("Chat Terminated by the Client");

        } catch(Exception ex){
            System.out.println(ex);
        }
    }
}
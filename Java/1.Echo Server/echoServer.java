import java.io.*;
import java.net.*;

class Server{
        public static void main(String[] args){
            try{
                //Creating a Connection by ServerSocket
                ServerSocket socket = new ServerSocket(9999);
                System.out.println("Waiting for the connection");

                //Accepting the Connection by Creating Socket Object
                Socket s = socket.accept();

                //Creating a InputStream to get the Input from the Client
                DataInputStream dataInputStream = new DataInputStream(s.getInputStream());
                String message = (String) dataInputStream.readUTF();
                System.out.println("Received Message From client: "+message);

                //Creating a OutputStream to sendback the message Received from the client
                DataOutputStream dataOutputStream = new DataOutputStream(s.getOutputStream());
                dataOutputStream.writeUTF(message);

                //Closing the ServerSocket Object
                socket.close();
            } catch(Exception ex){
                System.out.println(ex);
            }
         }
}
[15:54, 4/11/2024] Joash Johnson: import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 12345; // Server port
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is listening on port " + port);
            Socket socket = serverSocket.accept(); // Accept a client connection
            System.out.println("Client connected");

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println("Hello from the server!"); // Send a message to the client
            socket.close(); // Close the connection
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
[15:54, 4/11/2024] Joash Johnson: import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String hostname = "localhost"; // Server hostname
        int port = 12345; // Server port

        try (Socket socket = new Socket(hostname, port)) {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String response = in.readLine(); // Read the message from the server
            System.out.println("Server says: " + response);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

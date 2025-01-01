import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {

    static DiffieHellman dh;
    static byte[] message;

    public static void main(String[] args) throws IOException {
        dh = new DiffieHellman();
        decrypt();
    }

    public static void decrypt() throws IOException {
        message = Files.readString(Path.of("scramble.txt")).getBytes();
        Cube cube = new Cube(message, dh.reverseArrayKey(), "Decrypting");
        message = cube.concatenatedCubeToArray();
        String fileName =  "Rubik's Decrypted Flag";
        Utilities.writeMessage(fileName, message);
    }

}

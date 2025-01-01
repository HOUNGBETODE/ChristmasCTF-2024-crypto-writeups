import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class DiffieHellman {
    private BigInteger sharedKey;

    public DiffieHellman() throws IOException {
        sharedKey = readBigInteger(new File("sharedKey"));
        // System.out.println(sharedKey.toString());
    }

    private static BigInteger readBigInteger(File file) throws IOException {
        FileInputStream fis = new FileInputStream(file);
        byte[] bytes = new byte[(int) file.length()];
        fis.read(bytes);
        fis.close();
        return new BigInteger(new String(bytes));
    }

    public BigInteger getSharedKey() {
        return sharedKey;
    }

    public static int[] arrayKey(String sKey) {
        int remainder = 2466 - sKey.length();
        if (remainder == -1) {
            sKey = sKey.substring(1);
        }
        while (remainder > 0) {
            sKey = '0' + sKey;
            remainder--;
        }
        if (sKey.length() != 2466) {
            throw new Error("Key is " + sKey.length() + " long instead of 2466.");
        }
        int[] key = new int[411];
        String currentInt = "";
        int keyIndex = 0;
        for (int i = 0; i < sKey.length(); i++) {
            if (i % 6 == 0 && i != 0) {
                key[keyIndex] = Integer.parseInt(currentInt);
                currentInt = "";
                keyIndex++;
            }
            currentInt += sKey.charAt(i);
        }
        key[keyIndex] = Integer.parseInt(currentInt);
        return key;
    }

    public int[] arrayKey() {
        String sKey = sharedKey.toString();
        return arrayKey(sKey);
    }

    public int[] reverseArrayKey() {
        return reverseKey(arrayKey());
    }

    public static int[] reverseKey(int[] key) {
        int[] reverse = new int[key.length];
        for (int i = 0; i < key.length; i++) {
            int keyI = key[key.length - i - 1];
            keyI = keyI % 2 == 0 ? keyI + 1 : keyI - 1;
            reverse[i] = keyI;
        }
        return reverse;
    }
}

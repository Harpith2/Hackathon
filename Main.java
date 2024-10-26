import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
        boolean hasBeenPrinted = false;
        Scanner sc = new Scanner(System.in);
        int aLength = sc.nextInt();
        sc.nextLine();
        
        int[] aIntegers = new int[aLength];
        for (int i=0; i<aLength; i++) {
            aIntegers[i] = sc.nextInt();
            
        }
        
        sc.nextLine();
        int bLength = sc.nextInt();
        sc.nextLine();
        
        int[] bIntegers = new int[bLength];
        for (int i=0; i<bLength; i++) {
            bIntegers[i] = sc.nextInt();
            
        }
        
        for (int i=0; i<aIntegers.length; i++) {
            for (int j=0; j<bIntegers.length; j++) {
                int firstInt = aIntegers[i];
                int secondInt = bIntegers[j];
                int sum = firstInt + secondInt;
                boolean sumIsUnique = true;
                for (int k=0; k<aIntegers.length; k++) {
                    if (aIntegers[k] == sum) {
                        sumIsUnique = false;
                    }
                }
                for (int l=0; l<bIntegers.length; l++) {
                    if (bIntegers[l] == sum) {
                        sumIsUnique = false;
                    }
                }
                if (sumIsUnique) {
                    System.out.print(firstInt + " ");
                    System.out.println(secondInt);
                    System.exit(0);
                }
            }

        }
    }
}

package greedy_search;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

public class Greedy_main {

    public static void main(String[] args) {
        int bit = 10;
        int total = 0;
        for (int n = 10; n < 70; n = n + 2) {
            total = 0;
            for (int i = 0; i < 100; i++) {
                total += begin(n, bit);
            }
            System.out.println(n + ": " + total/100);
        }
    }

    public static int begin(int n, int bit) {
        int max_n_bit_number = (int) Math.pow(2, bit - 1);
        Integer[] S = new Integer[n];
        Random rand = new Random();
        int temp;
        for (int i = 0; i < n; i++) {
            temp = rand.nextInt(max_n_bit_number) + 0;
            S[i] = temp;
        }
        int t = 10000;
        Arrays.sort(S, Collections.reverseOrder());
        return SubsetSum_Greedy(S, n, t);
    }

    public static int SubsetSum_Greedy(Integer S[], int n, int t) {
        int total = 0;
        int i = 0;
//        List subset = new ArrayList<>();

        while (i <= n - 1) {
            if (total + S[i] <= t) {
                total = total + S[i];
//                subset.add(array[i]);
            }
            if (total == t) {
                break;
            }
            i++;
        }

//        for (int a = 0; a < subset.size(); a++) {
//            System.out.print(subset.get(a).toString() + " ");
//        }
        return t - total;
    }
}

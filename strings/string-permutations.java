 public  static void permutation(String str) { 
    permutation("", str); 
 }

 private static void permutation(String prefix, String str) {
    int n = str.length();
    if (n == 0) System.out.println(prefix);
    else {
        for (int i = 0; i < n; i++) {
        	// Important idea herer : we "recreate a set" of the remaining values to shake 
        	// by concatenating before(char) and after(char) (the substr(0, charpos) + substr(charpos+1, endofstr))
        	// We also add to the prefix this "i-th" element thus the prefis is shaken too
           permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
        }
    }

}
class Solution {
    public String convertToCamelCase(String s) {

        String[] a = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();

        sb.append(a[0]);

        for (int i = 1; i < a.length; i++) {
            sb.append(Character.toUpperCase(a[i].charAt(0)));
            sb.append(a[i].substring(1));
        }

        return sb.toString();
    }
}

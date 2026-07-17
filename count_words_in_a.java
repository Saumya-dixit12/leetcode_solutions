class Solution {
    public int countWords(String s) {
        
        int count = 0;
        boolean flag = false;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch==' ' || ch=='\t' || ch=='\n'){
                flag = false;
            }
            else if(!flag){
                count++;
                flag=true;
            }
        }
        return count;
    }
}

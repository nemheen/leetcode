bool detectCapitalUse(char * word){
    int c=0, i=0;
    char ch;
    while (word[i]) {
        ch = word[i];
        if (isupper(ch))
            c++;
 
        i++;
    }
    if(c==1 && isupper(word[0]))
        return true;
    if(c==i || c==0) 
        return true;
    else return false;
}

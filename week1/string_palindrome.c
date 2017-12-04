// https://www.interviewbit.com/problems/palindrome-string/

int isPalindrome(char* str) {
    char *s = str;
    char *e = str;

    while (*e)
        e++;
    e--;

    while (s < e) {
        if (!isalnum(*s)) {
            s++;
        } else if (!isalnum(*e)) {
            e--;
        } else if (toupper(*s) == toupper(*e)) {
            s++;
            e--;
        } else {
            return 0;
        }
    }
    return 1;
}
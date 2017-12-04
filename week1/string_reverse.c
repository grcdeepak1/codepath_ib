/*
 * @input A : String termination by '\0'
 *
 * @Output Void. Just modifies the args passed by reference
 *
 * https://www.interviewbit.com/problems/reverse-the-string/
 */

 void reverse(char *begin, char *end)
{
  char temp;
  while (begin < end)
  {
    temp = *begin;
    *begin++ = *end;
    *end-- = temp;
  }
}

void reverseWords(char* A) {
  char *word_begin = A;
  char *temp = A; /* temp is for word boundry */

  /*STEP 1 of the above algorithm */
  while( *temp )
  {
    temp++;
    if (*temp == '\0')
    {
      reverse(word_begin, temp-1);
    }
    else if(*temp == ' ')
    {
      reverse(word_begin, temp-1);
      word_begin = temp+1;
    }
  } /* End of while */

   /*STEP 2 of the above algorithm */
  reverse(A, temp-1);
}

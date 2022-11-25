# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>

/* THIS PROGRAM ANALYSES THE DIGITS OF A NUMBER TO DETERMINE IF IT IS SELF DESCRIBING OR NOT */


int main( ) {
	char first_line[1000]; // the first line of the input file 
	
	FILE * fpointer = fopen("SELF.txt","r");
	
	fgets(first_line,1000,stdin);
	
	int number_of_cases = atoi(first_line); // assignment and conversion(to integer) of first line to number of TEST CASES
	
	int n = 0; 
	while(n <= number_of_cases) {
	    char numb_string[100];
	    fgets(numb_string,100,stdin);
	    int trial = strlen(numb_string);
	    int numb_array;
	    int count = 0;
	    
	    char self_describing = 'T';
    
        for (int j = 0; j < trial; j++) {
        numb_array[j] = numb_string[j] - '0';
    }
    
        for (int j = 0; j < trial; j++) {
        printf("There are %d  %ds in the number \n", numb_array[j],j);
    }
        for (int m = 0; m< trial; m++) {
        for (int i = 0; i< trial; i++) {
            if (numb_array[i] == m) count++;
        }
            if(count == numb_array[m]){
            self_describing = 'T';
        }
            else{
            self_describing = 'F';
            printf("\n");
            printf("Not self-describing\n");
            break;
        }
        count = 0;
        if (self_describing != 'F'){
            printf("\n");
            printf("Self-describing\n");
            break;
        }
    }
    
}
	        
	    n++;
	}
	    
	    
	fclose(fpointer);
	
	return 0;
	}
	

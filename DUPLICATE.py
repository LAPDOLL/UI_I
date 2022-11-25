#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/* THIS PROGRAM REMOVES UNECESSARY DUPLICATE OF FILES FROM THE SYSTEM WHILE PRESERVING THE OLDEST/ORIGINAL COPY */

int main()
{
    char first_line[1000]; // the first line of the input file

    FILE *fpointer = fopen("FILES.txt", "r");

    fgets(first_line, 1000, stdin);

    int number_of_cases = atoi(first_line); // assignment and conversion(to integer) of first line to number of TEST CASES

    int n = 0;
    while (n <= number_of_cases)
    {
        int files[100];
        fgets(files, 100, stdin);
        int number_of_files = atoi(files);
        int O;
        for (O = 0, O <= number_of_files, O++)
        {
            int trials;
            int compareable = 0;
            int number_file;
            int t;
            int lowest_value = 0;
            char name_of_file[100][50];
            int file_id[100];

            printf("number of steps: ");
            scanf("%d", &trials);

            for (int p = 0; p < trials; p++)
            {
                printf("Number of files: ");
                scanf("%d", &number_file);

                int j = 0;

                while (j < number_file)
                {
                    scanf("%s %d", name_of_file[j], &file_id[j]);
                    j++;
                }
                printf("\n");
                lowest_value = file_id[0];
                for (int j = 0; j < number_file; j++)
                {
                    //            printf("%s %d\n", name_of_file[j], file_id[j]);
                    for (int p = j + 1; p < number_file; p++)
                    {
                        compareable = strcmp(name_of_file[j], name_of_file[p]);
                        if ((strcmp(name_of_file[j], name_of_file[p]) == 0) && (lowest_value > file_id[j]))
                        {
                            lowest_value = file_id[j];
                        }
                        else if ((strcmp(name_of_file[j], name_of_file[p]) != 0) && (file_id[j] > file_id[p]))
                        {
                            t = file_id[j];
                            file_id[j] = file_id[p];
                            file_id[p] = t;
                        }
                    }
                }
                for (int j = 0; j < number_file; j++)
                {
                    if (compareable != 0)
                    {
                        printf("%d\n", file_id[j]);
                    }
                }
                if (compareable == 0)
                {
                    printf("%d\n", lowest_value);
                }
            }
        }

        n++;
    }

    return 0;
}

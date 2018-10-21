#include<omp.h>
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* system, NULL, EXIT_FAILURE */
#include <string>
#include <iostream>
#include <time.h>

using namespace std;

int main (int argc, char **argv)
{
  std::string origindir = argv[1];
  std::string destdir = argv[2];
  printf ("Checking if processor is available...");
  if (system(NULL)) puts ("Ok");
    else exit (EXIT_FAILURE);
  printf ("Executing python command \n");
  
  
   time_t mytime = time(NULL);
   char * time_str = ctime(&mytime);
  printf("Current Time : %s\n", time_str);
  
  //contar la cantidad de frames
  //std::cout << count_files(destdir,"jpg") << std::endl;
  
  
  printf("enter to a parallel region");
 #pragma omp parallel for num_threads (4)
  for (int i=1;i<=329; i++){ //modificar la costante n para poder hacer independiente de los frames
    std::string my_command="python rgb_hsv.py " + destdir +"/"+ to_string(i) +".jpg";
    system ((my_command).c_str());    
  }

  
    time_t mytime2 = time(NULL);
    char * time_str2 = ctime(&mytime2);
    
    
    printf("Current Time : %s\n", time_str2);
  
  return 0;
}


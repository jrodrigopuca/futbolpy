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
  int cantidad = atoi(argv[3]);
  std::string cant_str = argv[3];
 
  printf ("Checking if processor is available...\n");
  time_t mytime = time(NULL);
  char * time_str = ctime(&mytime);
  printf("Current Time : %s\n", time_str);
  
  std::string my_command="python get_frames.py "+ origindir + " " + destdir;
  system ((my_command).c_str());
 

    
  printf("enter to a parallel region\n");
 #pragma omp parallel for num_threads (4)
  for (int i=1;i<=cantidad; i++){ //modificar la costante n para poder hacer independiente de los frames
      std::string name = to_string(i);
      while(cant_str.length() != name.length())
      {
          name= "0"+name;
      }
    std::string my_command2="python rgb_hsv.py " + destdir +"/"+ name +".jpg";
    system ((my_command2).c_str());    
  }

    my_command="python reconstruir.py "+ destdir +" .jpg "+destdir+"output.mp4 1 " + to_string(cantidad); //cambiar este hardcode
    system ((my_command).c_str());
  
    time_t mytime2 = time(NULL);
    char * time_str2 = ctime(&mytime2);
    
    
    printf("Current Time : %s\n", time_str2);
  
  return 0;
}


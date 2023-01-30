# falcon-prime-bulk-ip search function

This is repurposed code from a crowdstrike engineer to do what I needed. I re-wrote 5-10% how I would want to use it with one function and append to a data frame.

Need: If you have crowstrike falcon prime and need to search for a csv of malicious ip's, and want to append the intel to your csv of ip's. 

You need to get your base url, client secret and client id (remember not to hard code why I use getpass). 

![image](https://user-images.githubusercontent.com/50241257/215514710-5d5cfd2a-d71c-41b5-a6f5-9e34571f36c7.png)

### Operational overview
* 1. Change the csv paths
* 2. Install falconpy and other dependencies
* 3. Run
* 4. It will prompt you for the three things mentioned above


### Notes
* I was threat hunting over a huge area with little integration to crowd strikes tools. So, this saved me a ton of time gathering intel on malicous IP's that were fuzzing or attempting to exploit.  

 
### Contact
***If you have issues and need help reach out to colleybrb@gmail.com

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

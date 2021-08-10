# ifuzz
This tool is used for fuzzing API, directory fuzzing and sub domains fuzzing...




 
                      _  __
                     (_)/ _|_   _ ________
                     | | |_| | | |_  /_  /
                     | |  _| |_| |/ / / / 
                     |_|_|  \__,_/___/___|



			                  by @luffy27





-h --help for help

-u --url for url to test

-w --wordlist for wordlist used for fuzzing

Use: python ifuzz.py -u http://fuzz.test.com/ -w ./wordlist.txt

[root@test]-[~] python ifuzz.py -u http://127.0.0.1/fuzz.php -w ./words.txt


Also Contains my docker image for the latest version check it out




	docker pull luffy28/ifuzz
	docker run -it luffy28/ifuzz -h




# The third program exercise: Generate large enough random prime number

## The program was implemented by Nguyen Tien Anh

## Description:

The project allows to generate the large enough prime number for RSA Cryptosystem Purpose.
The main.py file contains source code of program.
The program makes sure that:
1. The number generated was 3072 bits (large enough) in length.
2. The number generated was randomly and hard enough to predict.
3. The average time to generate each number is fast enough.

In the main.py file, I used os.urandom(384) to generate 3072 bit random number. Then I set the highest and lowest bit of the number to 1. After, checked the number was prime or not by advanceRabin_Miller() function. The detail of function as described in the slide.
If the number was prime, then calculated time to generate from start time to the time in which the number was prime. If the time was in which range, increased counter of that range to 1. Finally, I consumed the result and print it to the console.

The result showed that:
- 18 numbers were generated in range 0 to 1 second
- 39 numbers were generated in range 1 to 2 seconds
- 25 numbers were generated in range 2 to 3 seconds
- 8 numbers were generated in range 3 to 4 seconds
- 2 numbers were generated in range 4 to 5 seconds
- 5 numbers were generated in range 5 to 6 seconds
- 3 numbers were generated in range 6 to 7 seconds
- and there was no number was generated in range 7 to 10 seconds

==> The program took 2.14 seconds in average to generate each prime number of the 100 first prime numbers.

## Requirement:

Python language with version 3.x
Then, run the command:
``` pip install gmpy2 ``` to install gmpy2 library.

## Usage:

From terminal, in the folder, type the following command:
``` python main.py ```

Wait for few minutes then the result will show in the console.

## Copyright by Nguyen Tien Anh

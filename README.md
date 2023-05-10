# Leaked-Password-Detector
This is a Python script that checks whether a password has been leaked before using the [Have I Been](https://haveibeenpwned.com/) Pwned API.

### Installation
1. Clone this repository to your local machine using 
```
git clone https://github.com/<username>/leaked-password-detector.git
```
2. Install the required libraries using 
```
pip install -r requirements.txt
```

### Usage
Run the script with one or more passwords as command line arguments, like so:
```python 
checkmypass.py password1 password2 password3
```
The script will then check each password against the Have I Been Pwned database and return a message indicating whether the password has been leaked before.

### How it works
1. The script generates the SHA-1 hash of the password.
2. The SHA-1 hash is split into two parts: the first 5 characters and the remaining characters.
3. Script uses the first 5 characters to send a request to the Have I Been Pwned API.
4. The API returns a list of hashes that start with the first 5 characters.
5. Script checks whether the remaining characters are contained in the list of hashes returned by the API.
6. If the remaining characters are found in the list, the script returns the number of times that password has been leaked.
7. If the remaining characters are not found in the list, the script returns 0.

### Conclusion
In summary, this Password Detector is a simple but useful Python script that helps users determine if their passwords have been leaked or compromised. By leveraging the Have I Been Pwned API, it provides a convenient way to check whether a password has been involved in a data breach and prompts users to change their passwords if necessary. 

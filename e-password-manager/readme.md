# Password Manager

 > A secure script that allows a user to view, add, and retrieve encrypted passwords from a file.
 
### Requirements :  
- Users must provide a Master Password to access the system.
- Use the cryptography.fernet library to encrypt and decrypt the saved passwords.
- Passwords must be saved to a persistent file (e.g., passwords.txt) along with the service name (e.g., Netflix | encrypted_value).
- Include functions for add() (to encrypt and save a new password) and view() (to retrieve and decrypt all saved passwords).
- Key Management The Fernet key must be saved to a separate, securely managed file (key.key). If this file is missing, the program should not run.
- Security Principle: The Master Password should not be stored, but rather compared against a securely hashed value (e.g., using hashlib) for verification.
- Clear Exit: Implement a clean way to exit the program after logging out or completing an action.
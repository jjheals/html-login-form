# html-login-form
A simple HTML login form and flask framework that takes into account security considerations. I will update over time as I consider/discover new vulnerabilities

- Uses python's pickle module to store user information in a dat file
- Maintains a list of taken usernames (server-side) to make the process of creating an account more efficient, where the script can check the list of taken usernames to see if a new username is taken, rather than iterating through every single saved user and then pulling each username which would be much less efficient
**Stores usernames in plaintext to make this process worth it. Usernames are to verify identity, where passwords are used to verify access permissions, so storing usernames in plaintext is not a major security concern. (At the time of writing) I'm also looking into creating a login attempt limit to prevent against brute force or dictionary attacks if the plaintext usernames were compromised. Plaintext usernames is also important to use the usernames for other organizational purposees, where hashed usernames would provide unncessary complexity.



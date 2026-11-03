I created three files (`public.txt`, `private.txt`, and `script.sh`) and three directories (`public_dir`, `private_dir`, and `shared_dir`) to experiment with Linux permissions.
Using the `chmod` command, I assigned different permission levels to files and directories.
For example:
- `chmod 777` allowed access to all users.
- `chmod 600` restricted file access to the owner.
- `chmod 700` allowed only the owner to read, write, and execute.
- `chmod 770` granted full access to the owner and group.
- I created a test user and group to demonstrate the commands `chown` and `chgrp`.
Using `chown`, I changed the owner of a file. Using `chgrp`, I changed its associated group.
After setting restrictive permissions, I verified that an unauthorized user could not read the file while its owner could.
The experiment demonstrated several security risks:
World-writable files: Files with permission `777` can be modified by unauthorized users, potentially compromising data integrity.
Exposed confidential information Files with overly permissive read access may disclose sensitive information.
Insecure directories Directories with permission `777` may allow unauthorized users to create, modify, or delete files.
This laboratory assignment demonstrated how Linux permissions and ownership mechanisms protect files and directories from unauthorized access.
By using `chmod`, `chown`, and `chgrp`, I learned how to configure access rights and understand the security consequences of incorrect permissions.
The experiment highlights the importance of secure permission configurations, regular auditing, and the principle of least privilege in maintaining system security.


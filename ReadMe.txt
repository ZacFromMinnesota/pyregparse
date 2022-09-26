You will have to change the path in parse.py if you want to execute it.

Notes from the exercise:
This is just a base level attempt to complete the task, If I spent more time I could make requests to pull and/or accept pushed logs from a particular device then parse but thats what a Siem already does so it didn't make sense to dive that deep. 

This basic script just opens the log file then searches the file for text that matches the regex then prints the output.

My regex could be cleaned up/ structured a bit better but for this particular case it did the job. If I was creating this for a production environment I would correct it before submitting for review or deployment to a log source.
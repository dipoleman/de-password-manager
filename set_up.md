# Set-Up Make File

 ran: make requirements 

 This installed all the dependencies in the requirements.txt 

 #### create task_one.py

 altered the make file to run this:

Run task one

one:

    \$(call execute_in_env, PYTHONPATH=${PYTHONPATH} python src/task_one.py)

NOTE: when naming the bucket have to use - not _ ie:

one-bucket NOT one_bucket




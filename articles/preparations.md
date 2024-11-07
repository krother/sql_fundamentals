
# Preparations

## The Baby Name Dataset

![](../images/babies.png)

The US authorities have registered the names of all US citizens born
since 1880. The record is `publicly available <http://www.ssa.gov/oact/babynames/limits.html>`__.

In this and the following chapters, you will analyze this data.
If you want to use the ``pandas`` library, you find a list of useful
functions at the bottom.

.. hint::

   The hints below require an account on `hackschule.de`.

## Preparations

1. Go to [hackschule.de]( https://workspace.hackschule.de/) 
2. Login with your email address
3. You will receive an email with a confirmation code 
4. Enter the confirmation code and press the green button **Workspace öffnen** to open your workspace[You should see this landing page](../images/landing_page.png)
6. VS Code opens automatically. [You should see this screen](../images/vscode_screen.png)
7. Click on the menu (three bars, top left) select "File -> New Text File" and save the file with "File -> Save" or Ctrl-s. Save the file name as `session1.sql`. [example screenshot](../images/new_text_file.png)
8. click on the menu (**"Terminal -> New Terminal"**)

## Connect to the Database

In the terminal window at the bottom ,copy-paste the following two commands:

    wget https://github.com/krother/sql_fundamentals/raw/refs/heads/main/select_queries/allnames.sql
    mysql < allnames.sql

Now connect to the SQL database with:

    mycli

You should see the prompt

    mysql>

![](preparations_done.png)


## Inspect the database

Type the following command into the prompt:

    SHOW TABLES;

Press <Enter>. You should see there is one table `babynames`.

You can display the columns of the table with:

    DESCRIBE babynames;

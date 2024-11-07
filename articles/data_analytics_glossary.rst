Data Analytics Glossary
=======================

The following keywords describe elementary operations on data. They help
you to:

-  plan and discuss steps in a data analysis
-  translate between data-centric technologies (e.g. SQL, Python/pandas,
   Tableau)
-  prompting an LLM

1. Data Types
-------------

Numeric / Scalar
~~~~~~~~~~~~~~~~

Values that are numbers, like integers, floating point numbers and
currency values. On numeric data you can do standard arithmetics.

Rank / Ordinal
~~~~~~~~~~~~~~

Values that are ordered, but only the relative position matters (first,
second, third). Although a rank is often stored as an integer number,
arithmetics make no sense here.

Category
~~~~~~~~

A clearly defined, often small set of allowed values. Categories can be
words or numbers.

Timestamp
~~~~~~~~~

Timestamps are a special type of numeric value. They are precisely
defined points in time, typically with a precision from nanoseconds to
seconds. It is worth noting that most computers use the POSIX format to
store timestamps (a very large integer number).

Timedelta
~~~~~~~~~

A duration or a difference between two timestamps.

String / Text
~~~~~~~~~~~~~

Any sequence of characters. Computers encode characters in different
ways. Sometimes you need to know which **encoding** is used. Examples of
encoding are ASCII (256 English and special characters), Unicode and
UTF-8 (large set of international characters and emoji).

Hash
~~~~

Sequence of characters generated from a string by an algorithm.
Frequently used for cryptographic keys and passwords. Most hashes cannot
be translated into the original text. SHA256 is an example of a hash
function.

UUID
~~~~

Secquence of characters that is unique. They are created for the sole
purpose of having a unique tag on something and carry no extra meaning.

Binary
~~~~~~

Raw data that has no particular meaning unless you know what it is for
(e.g. images, ZIP files or program files).

2. Inspect Data
---------------

Size
~~~~

The number of rows / columns is the first thing you may want to check in
a table. If it is a large body of data, you may want to check the
**memory size** as well.

Distinct values
~~~~~~~~~~~~~~~

The number of unique values in a column. Useful to find out how many
categories you are dealing with. With numeric data the number of
distinct values is less interesting.

Missing values
~~~~~~~~~~~~~~

Commonly, some fields are empty because that data is not available.
Missing values appear in different forms, e.g.: ``None``, ``NULL``,
``NaN``, ``-``, ``-1``, ``9999`` and others.

Outliers
~~~~~~~~

Outliers are statistically extreme values. Depending on the context, an
outlier can be a correct value or point to a data error.

Data Errors
~~~~~~~~~~~

Values that make no sense often make it into a data set. Examples would
be the value ``ABC`` in a numerical column, or the value ``70`` for the
population of a city.

3. Summaries
------------

Aggregation function
~~~~~~~~~~~~~~~~~~~~

A function that converts many values into one. Examples of aggregation
functions are the **sum** or the **count** for a set of values.

Measures of Centrality
~~~~~~~~~~~~~~~~~~~~~~

Statistically summarizes where a numerical column is. Mean, median and
mode are measures of centrality.

Measures of Spread
~~~~~~~~~~~~~~~~~~

Statistically summarizes how much the values in a numerical column
differ. Standard deviation, variance and range are measures of spread.

4. Rearrange data
-----------------

Aggregate
~~~~~~~~~

Summarizes data by condensing many values into one. Typical aggregations
are **sum**, **count**, **min**, **max**, **mean**.

Grouping
~~~~~~~~

Divides a dataset into multiple subgroups using a categorical column.
Typically each group is then aggregated using an aggregation function.

Crosstable or Pivot
~~~~~~~~~~~~~~~~~~~

Group the data according to two categorical columns, then summarize the
values of a third column using an aggregation function. The outcome is a
table with the the first category on the x-axis, the second on the
y-axis and the aggregated values populating the table.

Binning
~~~~~~~

Divides numerical data into multiple buckets by their values.
Effectively it converts numerical data into a category. Bins can be
equidistant (e.g. 1-10, 11-20, 21-30). Often you have to decide on the
number of bins.

If the buckets have the same number of data points, they are called
**quantiles**. If you have 4 quantiles, you can refer to them as
**quartiles**.

Impute
~~~~~~

Any procedure that fills empty or missing values. There are many
possible methods to fill a missing value, including **forward-filling**,
**backfilling**, **k-Nearest-Neighbor** and **interpolation**.

De-Duplication, dedup
~~~~~~~~~~~~~~~~~~~~~

Removing duplicate values from a dataset.

Transform
~~~~~~~~~

Change all values in a column of data without changing their number.
Often, transfomations are done with functions. Examples:

-  add 10 to each value in a column
-  reverse every string in a column

Transpose
~~~~~~~~~

Swap the rows and columns of a table, effectively turning the table by
90 degrees.

Long format
~~~~~~~~~~~

Arrange data in a way that all values are in one column, with labels in
another column next to them. A long format typically has very few
columns but many rows.

Wide format
~~~~~~~~~~~

In the wide format, every unique label is a column of its own. A wide
format typically has fewer rows but more columns than the long format.

.. note::

   Often, the wide and long format can be converted into each other without
   losing information.

5. Edit data
------------

Type conversion
~~~~~~~~~~~~~~~

Changes one data type into another, e.g. convert the string ``"33"``
into the number 33.

Normalize
~~~~~~~~~

**Warning:** the term **normalize** could refer to two things:

-  a method for scaling or mathematically transforming the data
-  changing the structure of tables in a SQL database

Because the two meanings have nothing to do with each other, I recommend
to use **scaling** or the name of the function for the first one, and
**normalize tables** for the second one.

Scale
~~~~~

Scaling changes numerical data so that it has known properties. E.g.:

-  **min-max-scaling** proportionally scales all numbers to values
   between 0 and 1
-  **standard scaling** proportionally scales all numbers so that they
   have a mean of 0.0 and a standard deviation of 1.0. Standard scaling
   assumes the data roughly follows a normal distrigution (bell-shaped
   curve).
-  **log scaling** or **log-normalization** applies the logarithm to
   convert exponential data into linear data.

Reindex
~~~~~~~

Assign a fresh set of id numbers to a dataset. Typically, one would
reindex with continuous integer numbers starting from 0 or 1.

Dummy Variable
~~~~~~~~~~~~~~

A column with boolean values (0/1) indicating some property in the
dataset. Often, dummy variables are derived from other data,
e.g. whether a row contains missing or erroneous values.

Factorize
~~~~~~~~~

Replace a category with integer numbers, e.g.

.. code::

   apple, banana, apple, cherry => 1, 2, 1, 3

One-Hot-Encoding
~~~~~~~~~~~~~~~~

Replace a category with multiple boolean columns, one for each distinct
value:

.. code::

   apple, banana, apple, cherry =>

   apple banana cherry 1 0 0 0 1 0 1 0 0 0 0 1

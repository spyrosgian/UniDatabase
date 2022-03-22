# UniDatabase
This is a Git repository that contains the Python script for
Assignment 4 of _Introduction in Python Programming_ Part Time Course of Cardiff University.

A university maintains a database, named CE3392, which contains the details of all students in the university studying module CE3392. There
is a similar database for each module studied. The details held on each student is as follows:
<pre>
number
title
forename
surname
module
coursemark
exammark
</pre>

The contents of a typical record might be: **1 Mr William Smith CE3392 23 45**.

Since many students may be attempting a module, a keyed database is used where the key is the student number.

_Menu option:_

Python script starts by presenting with the following menu to the user:
<pre>
Module Records

(1) Add a record
(2) Display a record
(3) Update a record
(4) Delete a record
(5) Display the details of all students on the module
(6) Exit
</pre>

_Select option:_

When adding a record, the user is prompted for the necessary information.

The fields number, coursemark and exammark should only contain decimal digits, the fields title, forename, surname should
only contain alphabetic characters and the field module should contain two uppercase alphabetic characters followed by four decimal digits.

_When a list of students on a module is to be displayed, the display of the list of students follows the following format:_

<pre>
List of students on module CE3392

Name                  Mark

Mr William Smith      68
</pre>

, where the mark displayed is the sum of the coursemark and exammark.

When a record is to be displayed, updated or deleted, the user is prompted for both the student module and the student number.

When arecord is to be updated, the only fields that cannot be changed are the student number and the student module.

When a record is to be deleted, its contents is first displayed and the user is then asked to confirm the deletion.

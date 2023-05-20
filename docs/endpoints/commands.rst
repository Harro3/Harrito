help
====
    Displays a little help message.

    * ``help``

alert
=====
    Makes the sense_hat blink rapidly for two seconds

    * ``alert``

echo <message>
==============
    Echos a message and desplays it on the sense_hat

    * ``echo <message>``

configure <parameter> <value>
=============================

    Changes the configuration of Harrito.
    For the list of available parameters, see the Config section.
    Usage example:

    * ``configure display_mode show_errors``

get <resource>
==============

    Retrieves some information about Harrito
    possible commands are:

    * ``get ip`` - returns Harrito's local ip address
    * ``get config`` - returns Harrito's configuration
    * ``get temerature``
    * ``get humidity``
    * ``get pressure``

shell [args]
============
    Runs a shell command in the bot's directory and displays its output.
    This command is usable by some users only.

    * ``shell [args]``
echo <message>
==============
    Echos a message and desplays it on the sense_hat

    * ``echo <message>``

get <resource>
==============

    Retrieves some information about Harrito
    possible commands are:

    * ``get ip`` - returns Harrito's local ip address
    * ``get config`` - returns Harrito's configuration
    * ``get temerature``
    * ``get humidity``
    * ``get pressure``

configure <parameter> <value>
=============================

    Changes the configuration of Harrito.
    For the list of available parameters, see the Config section.
    Usage example:

    * ``configure display_mode show_errors``
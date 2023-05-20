

display_mode
============
    ``configure display_mode <value>``

    Controls which responses are to be displayed on the sense hat led matrix.
    Possible values are:

    * ``default`` - Default display settings
    * ``never`` - **No** response will be displayed
    * ``always`` - **All** responses will be displayed
    * ``show_errors`` - On top of default, **all errors** will be displayed

text_color
==========
    ``configure text_color <red> <green> <blue>``

    Changes the color of the text displayed on the sense_hat from rgb values.
    For example:

    * ``configure text_color 0 255 0`` - Sets the color to green
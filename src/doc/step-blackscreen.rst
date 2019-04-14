*****************
Black Screen Step
*****************

The ``blackscreen`` step shows a black screen.

.. image:: images/blackscreen-screenshot.png

JSON Configuration for blackscreen Step
=======================================

Below is sample JSON for a survey step will all the options specified.

::

         {
           "action": "blackscreen",
           "duration": 30,
           "trigger_count": 5
        },


``duration``
   The number of seconds to show the step for. 
``trigger_count``
    The number of incoming trigger pulses until this step automatically advances. See :doc:`Trigger Inputs <input-trigger>` for how to configure input triggers. 


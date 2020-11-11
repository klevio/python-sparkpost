Events
=======

Retrieve a list of message events
---------------------------------

.. code-block:: python

    from sparkpost import SparkPost

    sp = SparkPost()

    sp.events.message.list()


Search for message events
---------------------------------

.. code-block:: python

    from sparkpost import SparkPost

    sp = SparkPost()

    sp.events.message.list(
        recipients='recipient@example.com',
        templates='example-template'
    )

See the `SparkPost search for Message Events API Reference`_.

.. _SparkPost search for Message Events API Reference: https://developers.sparkpost.com/api/events/#events-get-search-for-message-events


Retrieve a list of ingest events
--------------------------------

.. code-block:: python

    from sparkpost import SparkPost

    sp = SparkPost()

    sp.events.ingest.list()


Search for ingest events
---------------------------------

.. code-block:: python

    from sparkpost import SparkPost

    sp = SparkPost()

    sp.events.message.list(
        event_ids=['example_id_1', 'example_id_2']
    )

See the `SparkPost search for Ingest Events API Reference`_.

.. _SparkPost search for Ingest Events API Reference: https://developers.sparkpost.com/api/events/#events-get-search-for-ingest-events



API reference
-------------

:doc:`/api/events`


Additional documentation
------------------------

See the `SparkPost Events API Reference`_.

.. _SparkPost Events API Reference: https://developers.sparkpost.com/api/events/


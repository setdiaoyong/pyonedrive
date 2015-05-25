============
 pyonedrive
============

This is a bare-bones and badly-written [#]_ OneDrive batch uploader, using the
new API. For a more complete OneDrive solution in Python, see
`mk-fg/python-onedrive
<https://github.com/mk-fg/python-onedrive>`_. Unfortunately,
``python-onedrive`` does not support — and the maintainer has no plan to
support — the new OneDrive API (see `#52
<https://github.com/mk-fg/python-onedrive/issues/52>`_).

Two console scripts are bundled with this package, ``onedrive-upload`` and
``onedrive-geturl``.

``onedrive-upload``, according to my initial testing, is somewhat more reliable
than the CLI shipped with ``python-onedrive``, as I have implemented retries
and safeguards. It is also more likely to win out in the long run since
``python-onedrive`` uses a `semi-private BITS API
<https://gist.github.com/rgregg/37ba8929768a62131e85>`_ that is subject to
change. Howeever, speed is not great when few uploads are running concurrently
(this is also the case for ``python-onedrive``); better use the Web interface
in that case when it's not too much hessle (use ``onedrive-geturl`` to get a
direct link to a remote directory).

.. [#] Yes, I cooked up patches for a wide range of possible error scenarios
       along the way, resulting in horrible code. I will be able to do it much
       cleaner if I ever get to rewrite this.

Warnings
--------

* One needs to save the credentials to ``~/.config/onedrive/conf.ini``. The
  config file should be in the following format::

    [oauth]
    client_id = XXXXXXXXXXXXXXXX
    client_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    refresh_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

  I haven't implemented the authorization and code exchange process, so one
  needs to somehow obtain the refresh token on their own. ``python-onedrive``
  could help in this regard (in fact, I just copied the refresh token from my
  ``python-onedrive.yml``.

* Note that ``onedrive/cli.py`` depends on the ``zmwangx.colorout`` module
  (`link
  <https://github.com/zmwangx/pyzmwangx/blob/master/zmwangx/colorout.py>`_) for
  color printing of progress and errors. You may safely replace the
  ``cprogress``, ``cerror``, and ``cfatal_error`` calls with standard
  ``sys.stderr.write`` calls.

Best practices
--------------

* For whatever reason, the OneDrive resumable upload API responds slow or drops
  connection altogether quite often. Therefore, I have set a default timeout of
  15 seconds for each 10 MB chunk (add one second for each concurrent job). One
  may need to tweak the ``timeout`` parameter based on network condition to get
  best results.

* There are two modes of upload: streaming (each chunk) or not. The streaming
  mode uses less memory but is much more likely to hang (not forever since we
  have timeouts set in place) and generally slower.

  From my limited testing, a streaming worker uses ~15MB of memory, while a
  non-streaming one uses ~30MB at first and may grow to ~45MB for large files
  (maybe I have some hidden memory unreleased?). A streaming worker can be up
  to 30% slower (with timeouts accounted).

  Therefore, one should use nonstreaming workers (default) when there are only
  a few jobs, and streaming workers (specifying the ``-s, --streaming-upload``
  option) if there are a great number of concurrent jobs.

..
   Local Variables:
   fill-column: 79
   End:

Plans
-----

There are a couple of TODOs in the source code, waiting to be addressed.

Apart from that, I might implement other features in the future (and there
might be a rewrite, as I mentioned above). This is why I didn't name this as
``pyonedrive-upload``.
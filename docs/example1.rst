Example 1
---------

.. container:: left-col

    .. toggle-header::
        :header: Example 1 **Show/Hide Code**

        .. csv-table::
         :header: "Наименование", "Обязательный", "Описание"
         :widths: 5, 5, 15

          username,Да,Имя пользователя
          password,Да,Пароль

    .. toggle-header:: rubric
        :header: Example 2

        .. include:: /include/sdknet/Drivecred.Helium.Sdk.rst
                :start-after: T:Drivecred.Helium.Sdk.HeliumApi
                :end-before: --------------

.. container:: content-tabs right-col

        .. tab-container:: api
            :title: API (curl)

            .. code-block:: python

                import my-api

        .. tab-container:: net
            :title: C#

            .. code-block:: ruby

                require 'my-api'

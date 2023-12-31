# Инструкция пользования

***

## Предназначение

Приложение ***StudentAccounting*** создано для учёта посещений учеников занятия у репетитора.
Использование этого приложения позволит быстро подсчитывать заработок с одного/со всех учеников за определённый
промежуток времени.

# Использование

Главное окно приложения разделено на две части

1. Работа с учениками - правая рабочая область
2. Работа с посещениями учеников - левая рабочая область

Колонки разделены линией проходящей между ними.

## Работа со учениками (Правая рабочая область)

С учениками можно проводить такие операции:

1. Добавление нового ученика
2. Изменения данных ученика, указанных при его добавлении
3. Удаление ученика
4. Поиск ученика

Информация по выбранному ученику выводится в верхнем выделенном блоке

Следующий выделенный блок - **Фильтр**. 
Предназначен для посещений входящих в выбранный период периоду времени.

Фильтр поддерживает такие типы:

* _За всё время_ - выводятся все посещения
* _За этот год_ - выводятся все посещения за год дня, когда был выбран этот пункт
* _За этот месяц_ - выводятся все посещения за месяц дня, когда был выбран этот пункт
* _За выбранный период_ - выводятся все посещения за период, выбранный вами

Настроить свой период можно, ниже после выбора типа фильтра, как *За выбранный период*.
По кнопке выбрать вызывается окно с календарём, где вы выбираете нужную вам дату.

Следующий блок - **Суммарные результаты по всем ученикам**

Здесь выводится таблица из двух колонок.
В первой колонке сумма по ученикам с единой для них валютой.
Во второй колонке сумма часов затраченных на обучение учеников с единой для них валютой.
Данные в таблице зависят от фильтра, настраиваемого в блоке выше

## Работа с посещениями учеников (Левая рабочая область)

Левая рабочая область разделена на две части

1. Общая функциональность
2. Работа с посещениями

#### Общая функциональность

Этот раздел позволяет настроить

* Тему приложения - светлую или тёмную. По умолчанию стоит светлая.
* Вызвать окно помощи - указана информация об использовании данного приложения
* Вызвать окно информации о приложении - указана информация о разработчике данного приложения

Смена темы происходит при нажатии на кнопку с изображением

* Месяца - меняется светлую тему на тёмную
* Солнца - меняется тёмная тема на светлую

### Работа с посещениями

С посещениями студена можно проводить такие операции:

1. Добавление нового посещения для выбранного ученика
2. Редактирование данных указанных при создании выбранного посещения
3. Удаление посещения

Для этих операций в верхней части раздела приведены соответствующие кнопки.
Ниже расположена таблица отображающая все посещения выбранного ученика.
Посещения таблицы выводятся согласно фильтру.

## Взаимодействие с приложением

#### Давайте создадим тестового ученика:

1. Нажмите на кнопку **Добавить ученика**
2. В появившемся окне заполняем имя ученика.
    * Имя ученика должно быть отлично от пустого
    * Имя ученика не должно коррелировать с другими учениками
        + Например: Илья и илья - это два одинаковых имени
    * Давайте уникальные имена для ученика
        + Например: Илья Ростовский Мед ВУЗ - совпадения по имени минимальны
        + Например: Илья Ильич Ильин - вероятность совпадения больше
        + Например: Илья Ильич Ильин Ростовский Мед ВУЗ - совпадения по имени близки к нулю
        + **!** Если имя совпадёт появиться окно с сообщением об ошибке
3. Также в этом окне заполним поле цены за 1 час(60 минут) занятия
    * Цена должна быть отлична от нуля
    * Цена должна быть больше нуля
    * По умолчанию указана цена в 1 валютную единицу
4. Сбоку от цены можно выбрать одну из поддерживаемых валют
    * Поддерживаемые валюты:
        + **BYN** - Белорусский рубль
        + **RUB** - Российский рубль
        + **USD** - Американский доллар
        + **EUR** - Евро
5. Нажмите кнопку **Добавить**

Взгляните в выпадающем меню имён учеников появилось имя добавленного ученика.
В блоке информации о ученике появилось его имя и появились записи о доходе и длительности.
Добавьте ещё несколько учеников.

Теперь научимся выбирать ученика
Чуть выше блока с информацией об ученике есть мини-меню.
Найдите на тём стрелки **<** и **>** - это кнопки. Нажмите на них и выбудете выбирать предыдущего и следующего ученика
соответственно согласно списку.
Список можно увидеть там же, сейчас там выведено имя выбранного ученика.
Нажмите на стрелку направленную вниз - выпадет весь список добавленных в систему учеников.
Выберете нужного вам ученика, теперь чтобы его загрузить нажмите на кнопку с иконкой обновления **⟳**.

#### Теперь давайте изменим имя одного из учеников.

1. Нажмите на кнопку **Изменить ученика**
2. В появившемся окне заполняем имя ученика.
3. Можно изменить цену за 1 час занятия или выбрать другую валюту
4. Нажмите кнопку **Сохранить**, чтобы применить изменения

#### Давайте удалим лишнего ученика

1. Выберете ученика для удаления
2. Нажмите на кнопку **Удалить ученика**
3. Готово. Ученик удалён

Теперь вы умеете работать с данными об учениках в системе.
Давайте научимся работать с посещениями

#### Добавим ученику посещения

1. Нажмите на кнопку **Добавить посещение**
2. В появившемся окне выбираем дату.
3. Также в этом окне заполним поле длительности занятия за 1 час(60 минут) занятия
    * Длительность должна быть отлична от нуля
    * Длительность должна быть больше нуля
    * По умолчанию указана Длительность в 1 час
4. Сбоку от длительности можно выбрать тип оплаты занятия
    * Стандартная - этот тип рассчитывает стоимость занятия по формуле **Длительность * Цена одного часа**
    * Особая - этот тип позволяет указать цену, отличную от стандартной за всё занятие целиком
5. Если вы выберите стоимость занятия как особый, то появится поле для ввода цены за всё занятие
    * Цена должна быть отлична от нуля
    * Цена должна быть больше нуля
    * По умолчанию указана цена в 1 валютную единицу
6. Нажмите кнопку **Добавить**
7. В таблице посещений появится запись об этом посещении
8. В таблице по всем ученикам также появится строчка

#### Отредактируйте созданную запись

1. Выберете любую ячейку записи и нажмите кнопку **Изменить посещение**
2. Далее изменяйте информацию о посещении согласно правилам создания посещения
3. Нажмите на кнопку **Сохранить**
4. Изменения применились ко всем таблицам

#### Удалите изменённую запись

1. Выберете любую ячейку записи и нажмите кнопку **Удалить посещение**
2. Дынные выбранной записи будут удалены из системы и таблицы

## Фильтр и его настройки

Предварительно добавьте несколько посещений в разные года или месяцы для разных учеников
Теперь выберете одну из настроек фильтра:
Заметьте, что вывод строк посещений и суммарная таблица меняется в зависимости от фильтра


***

# Итог

Теперь вы изучили все возможность данного приложения. Успехов в его использовании
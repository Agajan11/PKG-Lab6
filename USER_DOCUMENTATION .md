# Пользовательская документация

## 1. Введение

Программа "3D буква 'Г'" предназначена для визуализации трёхмерной модели буквы 'Г' с возможностью её масштабирования, вращения и перемещения в пространстве. Приложение предоставляет пользователю удобный графический интерфейс, где параметры трансформации можно изменять с помощью слайдеров.

Программа будет полезна для обучения основам работы с трёхмерной графикой и трансформациями в Python. 

## 2. Системные требования

- **Операционная система:** Windows 7 и выше, macOS, Linux.
- **Программное обеспечение:** Python 3.8 и выше.
- **Библиотеки:**
  - `numpy`
  - `matplotlib`
  - `tkinter` (входит в стандартную библиотеку Python)
- **Аппаратные требования:**
  - Минимум 2 ГБ ОЗУ.
  - 200 МБ свободного места на диске.

## 3. Установка

### 3.1 Установка Python

1. Перейдите на официальный сайт Python: [python.org](https://www.python.org).
2. Скачайте последнюю версию Python 3.x.
3. Убедитесь, что при установке Python отмечен флажок "Add Python to PATH".
4. Завершите установку, следуя инструкциям установщика.

### 3.2 Установка библиотек

1. Убедитесь, что Python и менеджер пакетов `pip` установлены.
2. Установите необходимые библиотеки:
   ```bash
   pip install numpy matplotlib
   ```

### 3.3 Скачивание программы

1. Скачайте файл программы `3d_letter_g.py` из репозитория (или другого источника, предоставленного разработчиком).
2. Сохраните файл в удобной для вас директории.

### 3.4 Запуск программы

1. Откройте терминал или командную строку.
2. Перейдите в директорию с программой:
   ```bash
   cd путь/к/папке/с/файлом
   ```
3. Запустите программу:
   ```bash
   python 3d_letter_g.py
   ```

## 4. Использование приложения

### 4.1 Управление масштабированием

На панели управления доступны слайдеры для изменения масштаба модели буквы 'Г' по осям X, Y, Z. 

- **Слайдеры масштабирования:**
  - "Масштаб по X" — изменяет ширину модели.
  - "Масштаб по Y" — изменяет высоту модели.
  - "Масштаб по Z" — изменяет глубину модели.
- Диапазон изменения: от 0.1 до 10.0.

### 4.2 Перемещение модели

Для перемещения буквы 'Г' в пространстве используйте слайдеры:
- "Смещение по X" — перемещает модель влево или вправо.
- "Смещение по Y" — перемещает модель вверх или вниз.
- "Смещение по Z" — перемещает модель вперёд или назад.

Диапазон перемещения: от -15 до 15.

### 4.3 Вращение модели

Для поворота модели вокруг осей X, Y или Z используйте слайдеры:
- "Вращение по X" — вращает модель относительно горизонтальной оси.
- "Вращение по Y" — вращает модель относительно вертикальной оси.
- "Вращение по Z" — вращает модель относительно оси глубины.

Угол вращения задаётся в градусах. Диапазон: от -180° до 180°.

### 4.4 Сброс трансформаций

Для возврата модели к исходному состоянию нажмите кнопку "Начальный вид". Все параметры будут сброшены к значениям по умолчанию:
- Масштаб: 4.0 по всем осям.
- Смещение: 0.0.
- Вращение: 0°.

### 4.5 Визуализация модели

Модель буквы 'Г' отображается в трёхмерном графике, встроенном в интерфейс приложения. Обновления происходят в реальном времени при изменении параметров.

## 5. Пример использования

### Пример 1. Увеличение модели
1. Измените "Масштаб по X" до 6.0.
2. Измените "Масштаб по Y" до 5.0.
3. Нажмите и переместите "Смещение по Z" до 10.0.

Результат: модель буквы 'Г' станет больше и переместится вглубь экрана.

### Пример 2. Вращение модели
1. Установите "Вращение по X" на 45°.
2. Установите "Вращение по Y" на 30°.
3. Установите "Вращение по Z" на 90°.

Результат: модель повернётся вокруг всех трёх осей.

### Пример 3. Сброс параметров
1. После любых изменений нажмите кнопку "Начальный вид".
2. Модель вернётся к изначальному положению.

## 6. Часто задаваемые вопросы (FAQ)

### Вопрос: Программа не запускается. Что делать?
**Ответ:** Убедитесь, что Python установлен корректно, а библиотеки `numpy` и `matplotlib` установлены. Проверьте отсутствие ошибок в консоли.

### Вопрос: Можно ли изменить цвет модели?
**Ответ:** Да, вы можете изменить цвет, отредактировав параметр `facecolors` в функции `update_plot()`.

### Вопрос: Какой формат ввода для вращения?
**Ответ:** Углы вращения задаются в градусах через слайдеры интерфейса.

## 7. Обратная связь

Для вопросов, предложений или сообщений об ошибках обращайтесь по адресу: **agadjangarlyev@gmail.com**.

## 8. Лицензия

Программа распространяется на условиях лицензии MIT. Вы можете свободно использовать, изменять и распространять её при условии указания авторства.

## Приложения

### Приложение 1. Список библиотек
1. `numpy` — для работы с массивами и матрицами.
2. `matplotlib` — для построения трёхмерной графики.
3. `tkinter` — для создания графического интерфейса.

### Приложение 2. Полезные ссылки
- Официальный сайт Python: [python.org](https://www.python.org/)
- Документация Matplotlib: [matplotlib.org](https://matplotlib.org/)
- Документация NumPy: [numpy.org](https://numpy.org/)


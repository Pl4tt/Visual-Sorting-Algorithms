# Visual-Sorting-Algorithms
This is a visualization of sorting algorithms. It's a program that can visualize every sorting alorithm.

If you want to try visualize a sorting algorithm that's not in the algorithms folder, you just need to use the [``ColumnHolder.update(window, index, new_column)``](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/column_holder.py#L14) or [``ColumnHolder.swap(window, low, high)``](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/column_holder.py#L26) method whereever you update/swap your values.
In the [algorithms](https://github.com/Pl4tt/Visual-Sorting-Algorithms/tree/main/algorithms) folder you can see some examples for both cases.

Quick Description of the files and functionalities
--------------------------------------------------
- [visualization.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/visualization.py): Main file where everything is put together.
- [window.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/window.py): File with the Window class (used to control the window and ColumnHolder).
- [column.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/column.py): File with the Column class (used as list items).
- [column_holder.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/column_holder.py): File with the ColumnHolder class (used to control the columns).
- [config.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/config.py): File with all configurations (window size, caption, ...).
- [constants.py](https://github.com/Pl4tt/Visual-Sorting-Algorithms/blob/main/constants.py) File with all constants (colors, ...).
- [algorithms](https://github.com/Pl4tt/Visual-Sorting-Algorithms/tree/main/algorithms): Folder with a few sorting algorithms written for the visualization.

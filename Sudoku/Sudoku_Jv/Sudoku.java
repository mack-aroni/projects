import java.util.Arrays;

/*
 * Ethan Machleder
 * 
 * Sudoku.java
 * 
 * Project to create a more efficient recursive 
 * backtracking solver for Sudoku
 */

public class Sudoku {

    // static list that holds all Cells from 0-80
    private Cell[] list;

    // changing list that represents a priority queue
    private Cell[] sortedList;

    // used for printing at the end
    private int[][] grid;

    /*
     * merge - helper method for mergesort
     */
    private static void merge(Cell[] arr, Cell[] temp,
            int leftStart, int leftEnd, int rightStart, int rightEnd) {
        int i = leftStart; // index into left subarray
        int j = rightStart; // index into right subarray
        int k = leftStart; // index into temp

        while (i <= leftEnd && j <= rightEnd) {
            if (arr[i].compareTo(arr[j]) > 0) {
                temp[k] = arr[i];
                i++;
                k++;
            } else {
                temp[k] = arr[j];
                j++;
                k++;
            }
        }

        while (i <= leftEnd) {
            temp[k] = arr[i];
            i++;
            k++;
        }
        while (j <= rightEnd) {
            temp[k] = arr[j];
            j++;
            k++;
        }

        for (i = leftStart; i <= rightEnd; i++) {
            arr[i] = temp[i];
        }
    }

    /*
     * mSort - recursive method for mergesort
     */
    private static void mSort(Cell[] arr, Cell[] temp, int start, int end) {
        if (start >= end) {
            return;
        }
        int middle = (start + end) / 2;
        mSort(arr, temp, start, middle);
        mSort(arr, temp, middle + 1, end);
        merge(arr, temp, start, middle, middle + 1, end);
    }

    /*
     * mergesort - wrapper method
     */
    public static void mergeSort(Cell[] arr) {
        Cell[] temp = new Cell[arr.length];
        mSort(arr, temp, 0, arr.length - 1);
    }

    /*
     * initializes Sudoku class
     */
    public Sudoku() {
        // represents the sudoku grid
        this.grid = new int[9][9];
        // static Cell array with initialization
        this.list = new Cell[81];
        for (int i = 0; i < list.length; i++) {
            list[i] = new Cell(i);
        }
    }

    /*
     * placeVal - places the val at the specified value
     * and updates the puzzle accordingly
     */
    public void placeVal(int val, int row, int col) {
        grid[row][col] = val;
        if (val != 0) {
            addInvalids(val, row, col);
        }
    }

    /*
     * removeVal - removes the val at the specified
     * value and updates the puzzle accordingly
     */
    public void removeVal(int val, int row, int col) {
        grid[row][col] = 0;
        if (val != 0) {
            removeInvalids(val, row, col);
        }
    }

    /*
     * addInvalids - private helper method that updates
     * every Cell with the new added value in the static arr
     */
    private void addInvalids(int val, int row, int col) {
        for (Cell cell : list) {
            // checks if the Cell is fixed or is inPlay, if so, skip over
            if (!cell.isFixed()) {
                int cellRow = cell.getID() / 9;
                int cellCol = cell.getID() % 9;
                // checks if the Cell is affected by the added val
                if ((row == cellRow) || (col == cellCol) ||
                        (row / 3 == cellRow / 3 && col / 3 == cellCol / 3)) {
                    cell.addInvalid(val);
                }
            }
        }
        recreateSortedList();
    }

    /*
     * removeInvalids - private helper method that updates
     * every cell with the new added value
     */
    private void removeInvalids(int val, int row, int col) {
        for (Cell cell : list) {
            if (!cell.isFixed()) {
                int cellRow = cell.getID() / 9;
                int cellCol = cell.getID() % 9;
                if ((row == cellRow) || (col == cellCol) ||
                        (row / 3 == cellRow / 3 && col / 3 == cellCol / 3)) {
                    cell.removeInvalid(val);
                    System.out.println("Undo " + cell + " " + val);
                }
            }
        }
        recreateSortedList();
    }

    /*
     * recreateSortedList - private helper method that recreates
     * the sorted list that only contains the cells with a priority
     * less than 9 and aren't fixed and aren't inPlay
     */
    private void recreateSortedList() {
        int count = 0;
        // count finds the amount of cells that have priority less than 9
        for (Cell cell : list) {
            if (cell.getPriority() < 9 && !cell.isFixed()) { // && !cell.isInPlay()) {
                count++;
            }
        }
        // creates new list of size count
        Cell[] newList = new Cell[count];
        count = 0;
        // reiterates through the list again to apply the cells to new list
        for (Cell cell : list) {
            if (cell.getPriority() < 9 && !cell.isFixed()) { // && !cell.isInPlay()) {
                newList[count] = cell;
                count++;
            }
        }
        // assigns sortedList to newList and sorts it
        sortedList = newList;
        mergeSort(sortedList);
        if (COUNT != 0) {
            printCellArray();
        }
    }

    private void printCellArray() {
        int i = 0;
        while (sortedList.length > 0 && i < sortedList.length) {
            System.out.println(sortedList[i] + " ");
            i++;
        }
    }

    int COUNT = 0;

    /*
     * solve - main recursive-backtracking solving function
     */
    public boolean solve() {
        COUNT++;
        if (sortedList.length == 0) {
            return true;
        }

        Cell cell = sortedList[0];
        int row = cell.getID() / 9;
        int col = cell.getID() % 9;

        int[] options = cell.getNotInvalid();
        System.out.println(row + " " + col + " " + Arrays.toString(options));
        for (int val : options) {
            placeVal(val, row, col);
            if (solve()) {
                return true;
            }
            removeVal(val, row, col);
        }
        return false;
    }

    /*
     * readInput - reads the input in the form of a 2-d int array
     * and places their respective values onto the interior array
     */
    public void readInput(int[][] input) {
        int i = 0;
        // iterates through int[][] input
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int val = input[r][c];
                // places the val on the grid
                placeVal(val, r, c);
                // if val != 0 sets Cell to fixed
                if (val != 0) {
                    list[i].setFixed();
                }
                i++;
            }
        }
    }

    /*
     * printGrid - displays the state of the puzzle
     */
    public void printGrid() {
        for (int r = 0; r < 9; r++) {
            printRowSeparator();
            for (int c = 0; c < 9; c++) {
                System.out.print("|");
                if (this.grid[r][c] == 0) {
                    System.out.print("   ");
                } else {
                    System.out.print(" " + this.grid[r][c] + " ");
                }
            }
            System.out.println("|");
        }
        printRowSeparator();
    }

    /*
     * printRowSeparator - private helper method that
     * prints grid lines and separators
     */
    private static void printRowSeparator() {
        for (int i = 0; i < 9; i++) {
            System.out.print("----");
        }
        System.out.println("-");
    }

    public static void main(String[] args) {
        Sudoku puzzle = new Sudoku();
        int[][] input = {
                { 0, 4, 0, 0, 0, 3, 7, 0, 0 },
                { 0, 8, 9, 7, 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 4, 2, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                { 6, 0, 0, 5, 1, 8, 0, 0, 9 },
                { 2, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 5, 3, 0, 0, 0, 0, 0 },
                { 0, 0, 6, 0, 0, 1, 9, 4, 0 },
                { 0, 0, 1, 2, 0, 0, 0, 6, 0 },
        };
        int[][] input1 = {
                { 4, 3, 5, 2, 6, 9, 7, 8, 1 },
                { 6, 8, 2, 5, 7, 1, 4, 9, 3 },
                { 1, 9, 7, 8, 3, 4, 5, 6, 2 },
                { 8, 2, 6, 1, 9, 5, 3, 4, 7 },
                { 3, 7, 4, 6, 8, 2, 9, 1, 5 },
                { 9, 5, 1, 7, 4, 0, 0, 0, 0 },
                { 5, 1, 9, 3, 2, 0, 0, 0, 0 },
                { 2, 4, 8, 9, 5, 0, 0, 0, 0 },
                { 7, 6, 3, 4, 1, 0, 0, 0, 0 },
        };
        puzzle.readInput(input);

        System.out.println("Here is the initial puzzle: ");
        puzzle.printGrid();
        System.out.println();

        Arrays.toString(puzzle.sortedList);
        System.out.println();

        System.out.println("Here is the solution: ");
        puzzle.solve();
        puzzle.printGrid();
        System.out.println();
        System.out.println("Num Iterations: " + puzzle.COUNT);
    }
}